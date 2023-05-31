from channels.consumer import AsyncConsumer

class ChatConsumer(AsyncConsumer):
     
    async def websocket_connect(self, message):
        room = 'room'
        self.room = room
        # await self.channel_layer.group_add(
        #     room, self.channel_name
        # )
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, message):
        initial_data = message.get("text", None)
        print(message)

        # await self.channel_layer.group_add(
        self.send({
            "type": "websocket.send",
            "text": "pong",
        })
        # )

    async def websocket_message(self, message):
        await self.send({
            "type": "websocket.send",
            "text": message['text0'],
        })
    
    async def websocket_disconnect(self, message):
        print('Disconnect', message)