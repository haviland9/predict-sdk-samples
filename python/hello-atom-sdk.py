import time
import uuid
import sys, os
from riotsdk.atom_client import AtomClient

device_id = str("33300000-0000-0000-0000-000000000042")

# Custom query string
query_string = {
    "type": "compute",
    "body": {
        "function": {
            "type": "avg",
            "args": ["base.stream1"]
        },
        "window": {
            "type": "sliding",
            "args": [10000]
        },
        "alias": "average",
        "groupBy": {
            "type": "device"
        }
    },
    "streams": {
        "base": {
            "type": "RAW_DATA",
            "value": {
                "predicate": {
                    "devices": {
                        "type": "in",
                        "args": ["device", device_id]
                    }
                }
            }
        }
    }
}

started = -1
count = 0.0


def query_callback(data):
    """Callback called on query data.

    :param data: Received data
    :type data: dict, list, str
    """

    # Print received data to standard output
    print("DATA CALLBACK: " + data)
    global started
    global count
    if started == -1:
        started = time.time()

    count += 1
    print("Received {0}, speed {1}".format(count, count / (time.time() - started)))




def query_state_callback(data, error):
    """Callback called on query creation.

    :param data: Received data
        :type data: str
    :param error: Set in case of error, otherwise 0
        :type error: int
    """

    # Print received data to standard output
    print("STATE CALLBACK: " + data)


def main():
    # Initialise connection to Atom service
    # atom_client = AtomClient('10.2.13.209', 44444)
    atom_client = AtomClient('127.0.0.1', 44444)

    # Create device on connected Atom service
    device = atom_client.add_device(device_id, { "color" : "red"})
    # Add sensors to Device. Returned Stream objects are handlers to added sensors
    stream1 = device.add_sensor("stream1", "First stream", int, 0, 1000000)
    stream2 = device.add_sensor("stream2", "Second stream", int, 0, 1000000)

    device.update_attr({"color": "blue"})

    time.sleep(1)

    # Optional timestamp synchronization. Makes sens if you have relative timestamps
    device.synchronize(int(time.time() * 1000))

    # Send to Atom command to add new query
    atom_client.send_query(query_string, query_callback, query_state_callback)

    # Sleep some time before sending events, to simulate real dataflow
    time.sleep(1)

    for i in range(0, 10000):
        # Send data to Atom
        stream1.send(i)
        # device.update_attr({"color": "{}".format(i)})
        time.sleep(1)

    raw_input('>>>')
    # Cleanup connection
    atom_client.remove_device(device)


if __name__ == "__main__":
    main()
