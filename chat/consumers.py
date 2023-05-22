# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('message_updates', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('message_updates', self.channel_name)

    async def send_message_update(self, event):
        message = event['message']
        await self.send(json.dumps({
            'type': 'message_update',
            'message': message,
        }))