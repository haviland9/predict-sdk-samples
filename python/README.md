Prerequisites

Note: You must be registered with the Edge Developer Community to download Atom SDK.

- Python 2.7.x installed.
- Pip installed (latest version for your environment and Python version).
- AXON Predict Atom and Cloud installed and running on local machine. (Compatable with version available at Edge Developer Community.)

---

1. Download the ATOM SDK Python library from github (LINK??) https://edgedevrepo.greenwavesystems.com/repository/pypi-public/packages/riotsdk/2.0.0rc23/riotsdk-2.0.0rc23.tar.gz.

2. Install Predict Atom SDK Python library, using the following command. (Note: This installs all dependencies, including msgpack.)

```bash
pip install riotsdk -i https://edgedevrepo.greenwavesystems.com/repository/pypi-public/simple
```
3. When prompted, authenticate by using you Edge Developer Commununity portal account. 

Tip:
Use 'Pip list' to confirm the Atom SDK libraries are installed. 

4. Run the Python sample application, using the following command: 

```bash
python hello-atom-sdk.py
```

If started successfully, you'll see messages similar to the following:

```bash
Adding device: 33300000-0000-0000-0000-000000000042
Creating data stream stream1: First stream
Added stream1 sensor into 33300000-0000-0000-0000-000000000042 device
Creating data stream stream2: Second stream
Added stream2 sensor into 33300000-0000-0000-0000-000000000042 device
('Info: Received response with no callback for it: {}', {'errorCode': 0, 'body': '{}', 'errorMessage': 'Device successfully added', 'type': 'RESPONSE', 'correlationId': 2})
('Info: Received response with no callback for it: {}', {'errorCode': 0, 'body': '{}', 'errorMessage': 'Successfully updated device metadata', 'type': 'RESPONSE', 'correlationId': 3})
('Info: Received response with no callback for it: {}', {'errorCode': 0, 'body': '{}', 'errorMessage': 'Successfully updated device metadata', 'type': 'RESPONSE', 'correlationId': 4})
('Info: Received response with no callback for it: {}', {'errorCode': 0, 'body': '{}', 'errorMessage': 'Successfully updated device metadata', 'type': 'RESPONSE', 'correlationId': 5})
Sending query
STATE CALLBACK: Success. Query has been started
DATA CALLBACK: {"value": {"average": 0}, "timestamp": 1537907834370, "groupType": "device", "groupKey": "33300000-0000-0000-0000-000000000042"}
...
```
