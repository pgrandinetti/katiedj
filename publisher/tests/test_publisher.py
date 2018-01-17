from django.test import TestCase
from django.test import Client
from django.urls import reverse
from channels.test import WSClient
from django.conf import settings
import json

channel_name = 'sample_net'
VALID_KEY = [k for k in settings.API_KEYS.keys()
                if channel_name in settings.API_KEYS[k]][0]
ENDPOINT = reverse('publisher:main')


class PublisherTest(TestCase):

    """ Uses the sample_net channel to perform some tests"""

    path = '/macro/sample/'

    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)

    def test_wrong_key(self):
        """ The API-KEY is not valid"""
        data = {'network': 'ch_1',
                'data':
                {'one': '1',
                 'two': '2',
                 }
                }
        res = self.client.post(ENDPOINT,
                               data=json.dumps(data),
                               content_type="application/json",
                               HTTP_API_KEY='axdae')
        self.assertEqual(res.status_code, 400)

    def test_wrong_channel(self):
        """ The channel associated to this API-KEY is not accepted"""
        client1 = WSClient()
        client1.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client1.receive())
        data = {'network': 'ch_1',
                'data':
                {'one': '1',
                 'two': '2',
                 }
                }
        res = self.client.post(ENDPOINT,
                               data=json.dumps(data),
                               content_type="application/json",
                               HTTP_API_KEY=VALID_KEY)
        self.assertEqual(res.status_code, 403)
        self.assertIsNone(client1.receive())

    def test_ok_1(self):
        client1 = WSClient()
        client1.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client1.receive())
        data = {'network': 'sample_net',
                'data':
                {'one': '1',
                 'two': '2',
                 }
                }
        res = self.client.post(ENDPOINT,
                               data=json.dumps(data),
                               content_type="application/json",
                               HTTP_API_KEY=VALID_KEY)
        self.assertEqual(res.status_code, 200)
        stream = client1.receive()
        self.assertEqual(stream, data['data'])

    def test_missing_data(self):
        """ Key `data' is missing """
        client1 = WSClient()
        client1.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client1.receive())
        data = {'network': 'sample_net',
                'dataa':
                {'one': '1',
                 'two': '2',
                 }
                }
        res = self.client.post(ENDPOINT,
                               data=json.dumps(data),
                               content_type="application/json",
                               HTTP_API_KEY=VALID_KEY)
        self.assertEqual(res.status_code, 400)
        self.assertIsNone(client1.receive())

    def test_missing_channel(self):
        """ Key `network` is missing """
        client1 = WSClient()
        client1.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client1.receive())
        data = {'netwo': 'sample_net',
                'data':
                {'one': '1',
                 'two': '2',
                 }
                }
        res = self.client.post(ENDPOINT,
                               data=json.dumps(data),
                               content_type="application/json",
                               HTTP_API_KEY=VALID_KEY)
        self.assertEqual(res.status_code, 400)
        self.assertIsNone(client1.receive())

    def test_not_dict_2(self):
        """ Only Json data can be broadcasted"""
        client1 = WSClient()
        client1.send_and_consume('websocket.connect', path=self.path)
        self.assertIsNone(client1.receive())
        data = {'network': channel_name,
                'data': 'asd'
                }
        res = self.client.post(ENDPOINT,
                               data=json.dumps(data),
                               content_type="application/json",
                               HTTP_API_KEY=VALID_KEY)
        # Streaming must be JSON (not single string)
        self.assertEqual(res.status_code, 400)
        self.assertIsNone(client1.receive())
