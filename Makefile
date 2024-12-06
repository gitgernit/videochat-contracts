generate-go-rooms:
	protoc --proto_path=./proto --go_out=. --go-grpc_out=. --grpc-gateway_out . ./proto/rooms/rooms.proto

generate-python-rooms:
	python -m grpc_tools.protoc --proto_path=./proto  --python_out=./proto/rooms/python/proto --grpc_python_out=./proto/rooms/python/proto ./proto/rooms/rooms.proto
