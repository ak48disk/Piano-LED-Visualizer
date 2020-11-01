import mido
from mido.sockets import connect

host = 'raspberrypi.local'

def sleep():
    time.sleep(0.001)

while True:
    try:
        with connect(host, 8080) as server:
            with mido.open_input() as input:
                with mido.open_output() as output:
                    for msg in input.iter_pending():
                        server.send(msg)
                    for msg in server.iter_pending():
                        output.send(msg)

    except Exception as e:
        print(e)
