import struct
import json


class Packet:
    def __init__(self, pack_id: int = 0, data=None):
        if data is None:
            self.data = {}
            self.data['pack_id'] = pack_id
        else:
            self.data = data

    def encode(self) -> bytes:
        datastruct = bytes(json.dumps(self.data), 'utf-8')
        return struct.pack("I%ds" % (len(datastruct),), len(datastruct), datastruct)

    @classmethod
    def decode(cls, pack):
        (i,), data = struct.unpack("I", pack[:4]), pack[4:]
        data = data[:i]
        return cls(data=json.loads(data.decode('utf-8')))

