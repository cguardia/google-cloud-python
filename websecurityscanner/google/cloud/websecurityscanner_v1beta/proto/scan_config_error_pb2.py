# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1beta/proto/scan_config_error.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/websecurityscanner_v1beta/proto/scan_config_error.proto",
    package="google.cloud.websecurityscanner.v1beta",
    syntax="proto3",
    serialized_options=_b(
        "\n*com.google.cloud.websecurityscanner.v1betaB\024ScanConfigErrorProtoP\001ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\312\002&Google\\Cloud\\WebSecurityScanner\\V1beta"
    ),
    serialized_pb=_b(
        '\nDgoogle/cloud/websecurityscanner_v1beta/proto/scan_config_error.proto\x12&google.cloud.websecurityscanner.v1beta"\xc7\x0b\n\x0fScanConfigError\x12J\n\x04\x63ode\x18\x01 \x01(\x0e\x32<.google.cloud.websecurityscanner.v1beta.ScanConfigError.Code\x12\x12\n\nfield_name\x18\x02 \x01(\t"\xd3\n\n\x04\x43ode\x12\x14\n\x10\x43ODE_UNSPECIFIED\x10\x00\x12\x06\n\x02OK\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x1f\n\x1b\x41PPENGINE_API_BACKEND_ERROR\x10\x02\x12 \n\x1c\x41PPENGINE_API_NOT_ACCESSIBLE\x10\x03\x12"\n\x1e\x41PPENGINE_DEFAULT_HOST_MISSING\x10\x04\x12!\n\x1d\x43\x41NNOT_USE_GOOGLE_COM_ACCOUNT\x10\x06\x12\x1c\n\x18\x43\x41NNOT_USE_OWNER_ACCOUNT\x10\x07\x12\x1d\n\x19\x43OMPUTE_API_BACKEND_ERROR\x10\x08\x12\x1e\n\x1a\x43OMPUTE_API_NOT_ACCESSIBLE\x10\t\x12\x37\n3CUSTOM_LOGIN_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT\x10\n\x12\x1e\n\x1a\x43USTOM_LOGIN_URL_MALFORMED\x10\x0b\x12\x33\n/CUSTOM_LOGIN_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS\x10\x0c\x12\x31\n-CUSTOM_LOGIN_URL_MAPPED_TO_UNRESERVED_ADDRESS\x10\r\x12\x30\n,CUSTOM_LOGIN_URL_HAS_NON_ROUTABLE_IP_ADDRESS\x10\x0e\x12.\n*CUSTOM_LOGIN_URL_HAS_UNRESERVED_IP_ADDRESS\x10\x0f\x12\x17\n\x13\x44UPLICATE_SCAN_NAME\x10\x10\x12\x17\n\x13INVALID_FIELD_VALUE\x10\x12\x12$\n FAILED_TO_AUTHENTICATE_TO_TARGET\x10\x13\x12\x1c\n\x18\x46INDING_TYPE_UNSPECIFIED\x10\x14\x12\x1d\n\x19\x46ORBIDDEN_TO_SCAN_COMPUTE\x10\x15\x12\x14\n\x10MALFORMED_FILTER\x10\x16\x12\x1b\n\x17MALFORMED_RESOURCE_NAME\x10\x17\x12\x14\n\x10PROJECT_INACTIVE\x10\x18\x12\x12\n\x0eREQUIRED_FIELD\x10\x19\x12\x1e\n\x1aRESOURCE_NAME_INCONSISTENT\x10\x1a\x12\x18\n\x14SCAN_ALREADY_RUNNING\x10\x1b\x12\x14\n\x10SCAN_NOT_RUNNING\x10\x1c\x12/\n+SEED_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT\x10\x1d\x12\x16\n\x12SEED_URL_MALFORMED\x10\x1e\x12+\n\'SEED_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS\x10\x1f\x12)\n%SEED_URL_MAPPED_TO_UNRESERVED_ADDRESS\x10 \x12(\n$SEED_URL_HAS_NON_ROUTABLE_IP_ADDRESS\x10!\x12&\n"SEED_URL_HAS_UNRESERVED_IP_ADDRESS\x10#\x12"\n\x1eSERVICE_ACCOUNT_NOT_CONFIGURED\x10$\x12\x12\n\x0eTOO_MANY_SCANS\x10%\x12"\n\x1eUNABLE_TO_RESOLVE_PROJECT_INFO\x10&\x12(\n$UNSUPPORTED_BLACKLIST_PATTERN_FORMAT\x10\'\x12\x16\n\x12UNSUPPORTED_FILTER\x10(\x12\x1c\n\x18UNSUPPORTED_FINDING_TYPE\x10)\x12\x1a\n\x16UNSUPPORTED_URL_SCHEME\x10*\x1a\x02\x10\x01\x42\xc7\x01\n*com.google.cloud.websecurityscanner.v1betaB\x14ScanConfigErrorProtoP\x01ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1betab\x06proto3'
    ),
)


_SCANCONFIGERROR_CODE = _descriptor.EnumDescriptor(
    name="Code",
    full_name="google.cloud.websecurityscanner.v1beta.ScanConfigError.Code",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CODE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="OK", index=1, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="INTERNAL_ERROR", index=2, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="APPENGINE_API_BACKEND_ERROR",
            index=3,
            number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPENGINE_API_NOT_ACCESSIBLE",
            index=4,
            number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPENGINE_DEFAULT_HOST_MISSING",
            index=5,
            number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CANNOT_USE_GOOGLE_COM_ACCOUNT",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CANNOT_USE_OWNER_ACCOUNT",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPUTE_API_BACKEND_ERROR",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPUTE_API_NOT_ACCESSIBLE",
            index=9,
            number=9,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CUSTOM_LOGIN_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT",
            index=10,
            number=10,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CUSTOM_LOGIN_URL_MALFORMED",
            index=11,
            number=11,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CUSTOM_LOGIN_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS",
            index=12,
            number=12,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CUSTOM_LOGIN_URL_MAPPED_TO_UNRESERVED_ADDRESS",
            index=13,
            number=13,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CUSTOM_LOGIN_URL_HAS_NON_ROUTABLE_IP_ADDRESS",
            index=14,
            number=14,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="CUSTOM_LOGIN_URL_HAS_UNRESERVED_IP_ADDRESS",
            index=15,
            number=15,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="DUPLICATE_SCAN_NAME",
            index=16,
            number=16,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="INVALID_FIELD_VALUE",
            index=17,
            number=18,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="FAILED_TO_AUTHENTICATE_TO_TARGET",
            index=18,
            number=19,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="FINDING_TYPE_UNSPECIFIED",
            index=19,
            number=20,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="FORBIDDEN_TO_SCAN_COMPUTE",
            index=20,
            number=21,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="MALFORMED_FILTER",
            index=21,
            number=22,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="MALFORMED_RESOURCE_NAME",
            index=22,
            number=23,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="PROJECT_INACTIVE",
            index=23,
            number=24,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="REQUIRED_FIELD",
            index=24,
            number=25,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="RESOURCE_NAME_INCONSISTENT",
            index=25,
            number=26,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SCAN_ALREADY_RUNNING",
            index=26,
            number=27,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SCAN_NOT_RUNNING",
            index=27,
            number=28,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEED_URL_DOES_NOT_BELONG_TO_CURRENT_PROJECT",
            index=28,
            number=29,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEED_URL_MALFORMED",
            index=29,
            number=30,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEED_URL_MAPPED_TO_NON_ROUTABLE_ADDRESS",
            index=30,
            number=31,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEED_URL_MAPPED_TO_UNRESERVED_ADDRESS",
            index=31,
            number=32,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEED_URL_HAS_NON_ROUTABLE_IP_ADDRESS",
            index=32,
            number=33,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SEED_URL_HAS_UNRESERVED_IP_ADDRESS",
            index=33,
            number=35,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="SERVICE_ACCOUNT_NOT_CONFIGURED",
            index=34,
            number=36,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="TOO_MANY_SCANS",
            index=35,
            number=37,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNABLE_TO_RESOLVE_PROJECT_INFO",
            index=36,
            number=38,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNSUPPORTED_BLACKLIST_PATTERN_FORMAT",
            index=37,
            number=39,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNSUPPORTED_FILTER",
            index=38,
            number=40,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNSUPPORTED_FINDING_TYPE",
            index=39,
            number=41,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="UNSUPPORTED_URL_SCHEME",
            index=40,
            number=42,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=_b("\020\001"),
    serialized_start=229,
    serialized_end=1592,
)
_sym_db.RegisterEnumDescriptor(_SCANCONFIGERROR_CODE)


_SCANCONFIGERROR = _descriptor.Descriptor(
    name="ScanConfigError",
    full_name="google.cloud.websecurityscanner.v1beta.ScanConfigError",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="code",
            full_name="google.cloud.websecurityscanner.v1beta.ScanConfigError.code",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="field_name",
            full_name="google.cloud.websecurityscanner.v1beta.ScanConfigError.field_name",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_SCANCONFIGERROR_CODE],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=113,
    serialized_end=1592,
)

_SCANCONFIGERROR.fields_by_name["code"].enum_type = _SCANCONFIGERROR_CODE
_SCANCONFIGERROR_CODE.containing_type = _SCANCONFIGERROR
DESCRIPTOR.message_types_by_name["ScanConfigError"] = _SCANCONFIGERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanConfigError = _reflection.GeneratedProtocolMessageType(
    "ScanConfigError",
    (_message.Message,),
    dict(
        DESCRIPTOR=_SCANCONFIGERROR,
        __module__="google.cloud.websecurityscanner_v1beta.proto.scan_config_error_pb2",
        __doc__="""Defines a custom error message used by CreateScanConfig and
  UpdateScanConfig APIs when scan configuration validation fails. It is
  also reported as part of a ScanRunErrorTrace message if scan validation
  fails due to a scan configuration error.
  
  
  Attributes:
      code:
          Output only. Indicates the reason code for a configuration
          failure.
      field_name:
          Output only. Indicates the full name of the ScanConfig field
          that triggers this error, for example "scan\_config.max\_qps".
          This field is provided for troubleshooting purposes only and
          its actual value can change in the future.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanConfigError)
    ),
)
_sym_db.RegisterMessage(ScanConfigError)


DESCRIPTOR._options = None
_SCANCONFIGERROR_CODE._options = None
# @@protoc_insertion_point(module_scope)
