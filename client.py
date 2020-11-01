import mido
from mido.sockets import PortServer, connect

host = 'raspberrypi.local'

while True:
    try:
        output = connect(host, 8080)
        with mido.open_input() as input:
            for msg in input:
                print(msg)
                output.send(msg)
    except Exception as e:
        print(e)
