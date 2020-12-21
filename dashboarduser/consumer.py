import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from dashboarduser.detector import Detector
# from dashboarduser.views import image_view


class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        # print(self.scope)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.groupname, self.channel_name
        )

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val = datapoint['img']

        # Detector.image_processing(val)
        await self.channel_layer.group_send(
            self.groupname, {
                'type': 'deprocessing',
                'img': val
            }
        )

    async def deprocessing(self, event):
        valOther = event['img']
        await self.send(text_data=json.dumps({'img': valOther}))
