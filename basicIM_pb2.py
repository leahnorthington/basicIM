# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basicIM.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='basicIM.proto',
  package='basicIM',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\rbasicIM.proto\x12\x07\x62\x61sicIM\"0\n\x0e\x62\x61sicIMmessage\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08\x63ontents\x18\x02 \x02(\t')
)




_BASICIMMESSAGE = _descriptor.Descriptor(
  name='basicIMmessage',
  full_name='basicIM.basicIMmessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='basicIM.basicIMmessage.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='basicIM.basicIMmessage.contents', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['basicIMmessage'] = _BASICIMMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

basicIMmessage = _reflection.GeneratedProtocolMessageType('basicIMmessage', (_message.Message,), {
  'DESCRIPTOR' : _BASICIMMESSAGE,
  '__module__' : 'basicIM_pb2'
  # @@protoc_insertion_point(class_scope:basicIM.basicIMmessage)
  })
_sym_db.RegisterMessage(basicIMmessage)


# @@protoc_insertion_point(module_scope)
