from Packets.Packet import Packet
import random


class KeepAlivePacket(Packet):
    def __init__(self, kid=None, data=None):
        if data is None:
            super().__init__(0x01)
            if kid is None:
                kid = random.randint(10000000, 99999999)
            self.data['keep_alive_id'] = kid
        else:
            super().__init__(data=data)

