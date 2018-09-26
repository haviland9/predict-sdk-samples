import time
import uuid
import sys, os
from riotsdk.atom_client import AtomClient

device_id = str("53300000-0000-0000-0000-000000000042")


def main():
    # Initialise connection to Atom service
    # atom_client = AtomClient('10.2.13.209', 44444)
    atom_client = AtomClient('127.0.0.1', 44444)

    # Create device on connected Atom service
    device = atom_client.add_device(device_id, { "color" : "red"})
    # Add sensors to Device. Returned Stream objects are handlers to added sensors
    stream1 = device.add_sensor("stream1", "First stream", int, 0, 1000000)
    stream2 = device.add_sensor("stream2", "Second stream", int, 0, 1000000)


    # Optional timestamp synchronization. Makes sens if you have relative timestamps
    device.synchronize(int(time.time() * 1000))


    for i in range(0, 10000):
        # Send data to Atom
        stream1.send(i)
        stream2.send(i+10)
        time.sleep(1)

    raw_input('>>>')
    # Cleanup connection
    atom_client.remove_device(device)


if __name__ == "__main__":
    main()
