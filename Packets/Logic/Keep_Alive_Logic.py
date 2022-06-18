# TODO: Keep alive logic

"""
Client logic:
    got packet -> send same packet
    if server don't send for 20 seconds: server timeout
Server logic:
    1 sec = 1 packet to every client
    If client don't respond for 20 seconds: client timeout
    If client sent wrong packet: client timeout
"""