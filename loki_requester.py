from google.protobuf import text_format
import zmq

import request_pb2

request_string = """
requested_api: places_nearby
places_nearby {
  uri: "coord:2.34273:48.91814"
  distance: 2016.0000000000002
  types: STOP_POINT
  depth: 2
  count: 5000
  start_page: 0
}
disable_feedpublisher: true
"""

req = request_pb2.Request()
text_format.Parse(request_string, req)


context = zmq.Context()
zmq_socket = ""

socket = context.socket(zmq.REQ)

socket.connect(zmq_socket)
socket.send(req.SerializeToString())
if socket.poll(timeout=5 * 1000) > 0:
    pb = socket.recv()
    print("ok!!!")
    print(pb)
else:
    print("Timeout!!!!")
