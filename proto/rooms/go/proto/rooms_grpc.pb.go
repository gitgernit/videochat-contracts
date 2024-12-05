// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v5.28.3
// source: rooms/rooms.proto

package proto

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	RoomsService_PingPong_FullMethodName = "/proto.RoomsService/PingPong"
)

// RoomsServiceClient is the client API for RoomsService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type RoomsServiceClient interface {
	PingPong(ctx context.Context, opts ...grpc.CallOption) (grpc.BidiStreamingClient[Ping, Pong], error)
}

type roomsServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewRoomsServiceClient(cc grpc.ClientConnInterface) RoomsServiceClient {
	return &roomsServiceClient{cc}
}

func (c *roomsServiceClient) PingPong(ctx context.Context, opts ...grpc.CallOption) (grpc.BidiStreamingClient[Ping, Pong], error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	stream, err := c.cc.NewStream(ctx, &RoomsService_ServiceDesc.Streams[0], RoomsService_PingPong_FullMethodName, cOpts...)
	if err != nil {
		return nil, err
	}
	x := &grpc.GenericClientStream[Ping, Pong]{ClientStream: stream}
	return x, nil
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type RoomsService_PingPongClient = grpc.BidiStreamingClient[Ping, Pong]

// RoomsServiceServer is the server API for RoomsService service.
// All implementations must embed UnimplementedRoomsServiceServer
// for forward compatibility.
type RoomsServiceServer interface {
	PingPong(grpc.BidiStreamingServer[Ping, Pong]) error
	mustEmbedUnimplementedRoomsServiceServer()
}

// UnimplementedRoomsServiceServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedRoomsServiceServer struct{}

func (UnimplementedRoomsServiceServer) PingPong(grpc.BidiStreamingServer[Ping, Pong]) error {
	return status.Errorf(codes.Unimplemented, "method PingPong not implemented")
}
func (UnimplementedRoomsServiceServer) mustEmbedUnimplementedRoomsServiceServer() {}
func (UnimplementedRoomsServiceServer) testEmbeddedByValue()                      {}

// UnsafeRoomsServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to RoomsServiceServer will
// result in compilation errors.
type UnsafeRoomsServiceServer interface {
	mustEmbedUnimplementedRoomsServiceServer()
}

func RegisterRoomsServiceServer(s grpc.ServiceRegistrar, srv RoomsServiceServer) {
	// If the following call pancis, it indicates UnimplementedRoomsServiceServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&RoomsService_ServiceDesc, srv)
}

func _RoomsService_PingPong_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(RoomsServiceServer).PingPong(&grpc.GenericServerStream[Ping, Pong]{ServerStream: stream})
}

// This type alias is provided for backwards compatibility with existing code that references the prior non-generic stream type by name.
type RoomsService_PingPongServer = grpc.BidiStreamingServer[Ping, Pong]

// RoomsService_ServiceDesc is the grpc.ServiceDesc for RoomsService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var RoomsService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "proto.RoomsService",
	HandlerType: (*RoomsServiceServer)(nil),
	Methods:     []grpc.MethodDesc{},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "PingPong",
			Handler:       _RoomsService_PingPong_Handler,
			ServerStreams: true,
			ClientStreams: true,
		},
	},
	Metadata: "rooms/rooms.proto",
}
