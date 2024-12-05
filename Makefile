generate-rooms:
	protoc --proto_path=./proto --go_out=. --go-grpc_out=. --grpc-gateway_out . ./proto/rooms/rooms.proto
