import asyncio as aio
from Server.Clients import Client

HOST = "127.0.0.1"
PORT = 16384


class Server:
    addrs: str
    server = aio.AbstractServer

    def __init__(self, host: str, port: int) -> None:
        self.host: str = host
        self.port: int = port
        self.clients = []

    async def logic(self, reader: aio.StreamReader, writer: aio.StreamWriter) -> None:
        client = Client(reader, writer)

        while True:
            await client.client_handler()
#       TODO: Async client reading(mb aio.gather)

    async def start_server(self) -> None:
        self.server = await aio.start_server(self.logic, self.host, self.port)
        self.addrs = ', '.join(str(sock.getsockname()) for sock in self.server.sockets)

        async with server:
            await self.server.serve_forever()

    def start(self) -> None:
        aio.run(self.start_server())


server = Server(HOST, PORT)
server.start()

# TODO: 3D someshit using ursina

"""with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received {data.decode('utf-8')!r}")
            #conn.sendall(data)"""
