import asyncio as aio
from Server.Logic import packet_handler


# TODO: Something about client class
class Client:
    def __init__(self, reader: aio.StreamReader, writer: aio.StreamWriter):
        self.reader = reader
        self.writer = writer
        self.disconnected = False
#       TODO: Keep Alive buffer and disconnection
        self.kaBuffer = []

    async def client_handler(self):
        inp = None
        try:
            inp = await aio.wait_for(self.read(), 30)
        except aio.TimeoutError as e:
            await self.close(e)

        await packet_handler(inp, self)

    async def read(self, n: int = -1):
        packet = await self.reader.read(n)
        await packet_handler(packet, self)

    async def write(self, packet):
        self.writer.write(packet)
        await self.writer.drain()

#   TODO: Append keep alive buffer & disconnection (nah, we have read timeout, just do next)
#   TODO: kab=[1,2,3,4,5]. got kid=3. kab=[4,5]
    async def pas(self):
        pass

#   TODO: Disconnect reason
    async def close(self, reason):
        await self.writer.drain()
        self.writer.close()
        await self.writer.wait_closed()
        self.disconnected = True
