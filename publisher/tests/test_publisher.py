import json
import pytest

from django.test import Client
from django.urls import reverse
from django.conf import settings

from channels.testing import WebsocketCommunicator

from asgiref.sync import sync_to_async, async_to_sync

from main.consumers import SampleNetwork

channel_name = 'sample_net'
path = '/macro/sample/'
VALID_KEY = [k for k in settings.API_KEYS.keys()
                if channel_name in settings.API_KEYS[k]][0]
ENDPOINT = reverse('publisher:main')


# pytest publisher/tests/test_publisher_channels2.py --ds=main.settings.dev

def test_wrong_key():
    """ The API-KEY is not valid"""
    client = Client(enforce_csrf_checks=True)
    data = {'network': 'ch_1',
            'data':
            {'one': '1',
             'two': '2',
             }
            }
    res = client.post(ENDPOINT,
                      data=json.dumps(data),
                      content_type="application/json",
                      HTTP_API_KEY='axdae')
    assert (res.status_code == 400)


@pytest.mark.asyncio
async def test_wrong_channel():
    """ The channel associated to this API-KEY is not accepted"""
    client = Client(enforce_csrf_checks=True)
    communicator = WebsocketCommunicator(SampleNetwork, path)
    connected, _ = await communicator.connect()
    assert await communicator.receive_nothing()
    data = {'network': 'ch_1',
            'data':
            {'one': '1',
             'two': '2',
             }
            }
    res = await sync_to_async(client.post)(
                    ENDPOINT,
                    data=json.dumps(data),
                    content_type="application/json",
                    HTTP_API_KEY=VALID_KEY)
    assert (res.status_code == 403)
    assert await communicator.receive_nothing()
    await communicator.disconnect()


@pytest.mark.asyncio
async def test_ok_1():
    client = Client(enforce_csrf_checks=True)
    communicator = WebsocketCommunicator(SampleNetwork, path)
    connected, _ = await communicator.connect()
    assert await communicator.receive_nothing()
    data = {'network': 'sample_net',
            'data':
            {'one': '1',
             'two': '2',
             }
            }
    res = await sync_to_async(client.post)(
                    ENDPOINT,
                    data=json.dumps(data),
                    content_type="application/json",
                    HTTP_API_KEY=VALID_KEY)
    assert (res.status_code == 200)
    response =  await communicator.receive_json_from()
    assert (response == data['data'])
    await communicator.disconnect()


@pytest.mark.asyncio
async def test_missing_data():
    """ Key `data' is missing """
    client = Client(enforce_csrf_checks=True)
    communicator = WebsocketCommunicator(SampleNetwork, path)
    connected, _ = await communicator.connect()
    assert await communicator.receive_nothing()
    data = {'network': 'sample_net',
            'dataa':
            {'one': '1',
             'two': '2',
             }
            }
    res = await sync_to_async(client.post)(
                    ENDPOINT,
                    data=json.dumps(data),
                    content_type="application/json",
                    HTTP_API_KEY=VALID_KEY)
    assert (res.status_code == 400)
    assert await communicator.receive_nothing()
    await communicator.disconnect()


@pytest.mark.asyncio
async def test_missing_channel():
    """ Key `network` is missing """
    client = Client(enforce_csrf_checks=True)
    communicator = WebsocketCommunicator(SampleNetwork, path)
    connected, _ = await communicator.connect()
    assert await communicator.receive_nothing()
    data = {'netwo': 'sample_net',
            'data':
            {'one': '1',
             'two': '2',
             }
            }
    res = await sync_to_async(client.post)(
                    ENDPOINT,
                    data=json.dumps(data),
                    content_type="application/json",
                    HTTP_API_KEY=VALID_KEY)
    assert (res.status_code == 400)
    assert await communicator.receive_nothing()
    await communicator.disconnect()


@pytest.mark.asyncio
async def test_not_dict():
    """ Only Json data can be broadcasted"""
    client = Client(enforce_csrf_checks=True)
    communicator = WebsocketCommunicator(SampleNetwork, path)
    connected, _ = await communicator.connect()
    assert await communicator.receive_nothing()
    data = {'network': 'sample_net',
            'data': 'asd'
            }
    res = await sync_to_async(client.post)(
                    ENDPOINT,
                    data=json.dumps(data),
                    content_type="application/json",
                    HTTP_API_KEY=VALID_KEY)
    assert (res.status_code == 400)
    assert await communicator.receive_nothing()
    await communicator.disconnect()
