# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dataproc_v1/proto/shared.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/dataproc_v1/proto/shared.proto",
    package="google.cloud.dataproc.v1",
    syntax="proto3",
    serialized_options=_b(
        "\n\034com.google.cloud.dataproc.v1B\013SharedProtoP\001Z@google.golang.org/genproto/googleapis/cloud/dataproc/v1;dataproc"
    ),
    serialized_pb=_b(
        "\n+google/cloud/dataproc_v1/proto/shared.proto\x12\x18google.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto*a\n\tComponent\x12\x19\n\x15\x43OMPONENT_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x41NACONDA\x10\x05\x12\x10\n\x0cHIVE_WEBHCAT\x10\x03\x12\x0b\n\x07JUPYTER\x10\x01\x12\x0c\n\x08ZEPPELIN\x10\x04\x42o\n\x1c\x63om.google.cloud.dataproc.v1B\x0bSharedProtoP\x01Z@google.golang.org/genproto/googleapis/cloud/dataproc/v1;dataprocb\x06proto3"
    ),
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)

_COMPONENT = _descriptor.EnumDescriptor(
    name="Component",
    full_name="google.cloud.dataproc.v1.Component",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="COMPONENT_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ANACONDA", index=1, number=5, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="HIVE_WEBHCAT", index=2, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="JUPYTER", index=3, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ZEPPELIN", index=4, number=4, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=103,
    serialized_end=200,
)
_sym_db.RegisterEnumDescriptor(_COMPONENT)

Component = enum_type_wrapper.EnumTypeWrapper(_COMPONENT)
COMPONENT_UNSPECIFIED = 0
ANACONDA = 5
HIVE_WEBHCAT = 3
JUPYTER = 1
ZEPPELIN = 4


DESCRIPTOR.enum_types_by_name["Component"] = _COMPONENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
