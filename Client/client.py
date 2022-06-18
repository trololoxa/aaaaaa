import socket
import asyncio as aio

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 16384  # The port used by the server


class Client:
    def __init__(self, host, port):
        self.con_host = host
        self.con_port = port
        self.reader = aio.StreamReader
        self.writer = aio.StreamWriter

    async def logic(self):
        self.reader, self.writer = await aio.open_connection(self.con_host, self.con_port)

        try:
            while True:
                pass
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            self.writer.close()
            await self.writer.wait_closed()
        finally:
            self.writer.close()
            await self.writer.wait_closed()

    def start(self):
        aio.run(self.logic())


client = Client(HOST, PORT)
client.start()

"""with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        inp = input()
        if inp.lower() == 'exit':
            break
        s.sendall(inp.encode('utf-8'))
        #data = s.recv(1024)


#print(f"Received {data.decode('utf-8')!r}")"""