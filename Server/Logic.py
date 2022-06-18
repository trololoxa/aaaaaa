import asyncio as aio
from Packets.Packets.Keep_Alive import KeepAlivePacket


async def packet_handler(packet, client):
    packet = packet.decode()
    pid = packet.data['pack_id']
    if pid == 0x01:
        await keep_alive_in(client, packet)


async def keep_alive_out(clients):
    packet = KeepAlivePacket()
    async for client in clients:
        if len(client.kaBuffer) > 20:
            client.close()
        client.kaBuffer += packet.data['keep_alive_id']
        client.write(packet)
    await aio.sleep(1)


async def keep_alive_in(client, packet):
    if packet.data['keep_alive_id'] in client.kaBuffer:
        client.kaBuffer = []
    else:
        client.close()
