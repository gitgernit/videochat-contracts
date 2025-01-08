from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ping(_message.Message):
    __slots__ = ("counter",)
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    counter: int
    def __init__(self, counter: _Optional[int] = ...) -> None: ...

class Pong(_message.Message):
    __slots__ = ("counter",)
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    counter: int
    def __init__(self, counter: _Optional[int] = ...) -> None: ...

class ListenForRoomsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NewRoomNotification(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateRoomRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CreateRoomResponse(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "username")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    username: str
    def __init__(self, id: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class GetRoomUsers(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RoomUsers(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class SendMessageRequest(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class MessageReceivedNotification(_message.Message):
    __slots__ = ("text", "username")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    text: str
    username: str
    def __init__(self, text: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class SDP(_message.Message):
    __slots__ = ("type", "sdp", "username")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SDP_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    type: str
    sdp: str
    username: str
    def __init__(self, type: _Optional[str] = ..., sdp: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class SendSDP(_message.Message):
    __slots__ = ("sdp",)
    SDP_FIELD_NUMBER: _ClassVar[int]
    sdp: _containers.RepeatedCompositeFieldContainer[SDP]
    def __init__(self, sdp: _Optional[_Iterable[_Union[SDP, _Mapping]]] = ...) -> None: ...

class SDPReceivedNotification(_message.Message):
    __slots__ = ("type", "sdp", "to")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SDP_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    type: str
    sdp: str
    to: str
    def __init__(self, type: _Optional[str] = ..., sdp: _Optional[str] = ..., to: _Optional[str] = ..., **kwargs) -> None: ...

class SendIceCandidate(_message.Message):
    __slots__ = ("candidate",)
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    candidate: str
    def __init__(self, candidate: _Optional[str] = ...) -> None: ...

class IceCandidateReceivedNotification(_message.Message):
    __slots__ = ("candidate", "username")
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    candidate: str
    username: str
    def __init__(self, candidate: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class RoomMethod(_message.Message):
    __slots__ = ("send_message", "message_received", "send_sdp", "sdp_received", "send_ice_candidate", "ice_candidate_received", "get_room_users", "room_users")
    SEND_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    SEND_SDP_FIELD_NUMBER: _ClassVar[int]
    SDP_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    SEND_ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    ICE_CANDIDATE_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    GET_ROOM_USERS_FIELD_NUMBER: _ClassVar[int]
    ROOM_USERS_FIELD_NUMBER: _ClassVar[int]
    send_message: SendMessageRequest
    message_received: MessageReceivedNotification
    send_sdp: SendSDP
    sdp_received: SDPReceivedNotification
    send_ice_candidate: SendIceCandidate
    ice_candidate_received: IceCandidateReceivedNotification
    get_room_users: GetRoomUsers
    room_users: RoomUsers
    def __init__(self, send_message: _Optional[_Union[SendMessageRequest, _Mapping]] = ..., message_received: _Optional[_Union[MessageReceivedNotification, _Mapping]] = ..., send_sdp: _Optional[_Union[SendSDP, _Mapping]] = ..., sdp_received: _Optional[_Union[SDPReceivedNotification, _Mapping]] = ..., send_ice_candidate: _Optional[_Union[SendIceCandidate, _Mapping]] = ..., ice_candidate_received: _Optional[_Union[IceCandidateReceivedNotification, _Mapping]] = ..., get_room_users: _Optional[_Union[GetRoomUsers, _Mapping]] = ..., room_users: _Optional[_Union[RoomUsers, _Mapping]] = ...) -> None: ...
