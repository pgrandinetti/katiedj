from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from channels import Group
import json


@method_decorator(csrf_exempt, name='dispatch')
class PublisherView(View):

    def post(self, request):
        """ Called by a publisher, to broadcast its data.

            Request parameters (in json format):

            Headers:
                `API-KEY` - a valid key to access the endpoint (HEADERS)
            POST data:
                `network` - a valid network channel name
                `data` - the actual data to be broadcasted, in valid json
        """
        try:
            key = request.META['HTTP_API_KEY']
            if not key in settings.API_KEYS:
                return JsonResponse(
                    {'error': 'API-KEY not valid'}, status=400)
        except:
            return JsonResponse(
                {'error': 'API-KEY missing in headers'}, status=400)
        try:
            body = json.loads(request.body.decode('utf-8'))
        except:
            return JsonResponse(
                {'error': 'POST data is not JSON'}, status=400)
        try:
            group = body['network']
        except:
            return JsonResponse(
                {'error': '*network* key missing'}, status=400)
        if group not in settings.API_KEYS[key]:
            return JsonResponse(
                {'error': 'You cannot broadcast to this channel'}, status=403)
        if not 'data' in body:
            return JsonResponse(
                {'error': '*data* key missing'}, status=400)
        if not isinstance(body['data'], dict):
            return JsonResponse(
                {'error': 'Can only broadcast json data'}, status=400)
        Group(group).send({'text': json.dumps(body['data'])})
        return JsonResponse({}, status=200)
