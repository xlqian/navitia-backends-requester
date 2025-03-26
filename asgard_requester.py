from google.protobuf import text_format
import zmq

import request_pb2

request_string = """
requested_api: direct_path
direct_path {
  origin {
    place: "coord:2.37715:48.846781"
    access_duration: 0
  }
  destination {
    place: "coord:2.356584144292068:48.85407484412556"
    access_duration: 0
  }
  datetime: 1742994198
  clockwise: true
  streetnetwork_params {
    origin_mode: "walking"
    destination_mode: "walking"
    walking_speed: 1.12
    bike_speed: 4.1
    car_speed: 11.11
    bss_speed: 4.1
    max_walking_duration_to_pt: 43200
    max_bike_duration_to_pt: 1800
    max_bss_duration_to_pt: 1800
    max_car_duration_to_pt: 1800
    language: "en-US"
  }
}"""

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
