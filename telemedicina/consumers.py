from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TelemedicinaConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sala = self.scope["url_route"]["kwargs"].get("sala", "default")
        await self.channel_layer.group_add(self.sala, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            self.sala, {
                "type": "broadcast_message",
                "message": text_data
            }
        )

    async def broadcast_message(self, event):
        await self.send(event["message"])
