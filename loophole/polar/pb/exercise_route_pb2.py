# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data/exercise_route.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2 as types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='data/exercise_route.proto',
  package='data',
  syntax='proto2',
  serialized_pb=_b('\n\x19\x64\x61ta/exercise_route.proto\x12\x04\x64\x61ta\x1a\x0btypes.proto\"\xa8\x02\n\x16PbExerciseRouteSamples\x12\x10\n\x08\x64uration\x18\x01 \x03(\r\x12\x10\n\x08latitude\x18\x02 \x03(\x01\x12\x11\n\tlongitude\x18\x03 \x03(\x01\x12\x14\n\x0cgps_altitude\x18\x04 \x03(\x11\x12\x18\n\x10satellite_amount\x18\x05 \x03(\r\x12\x14\n\x0cOBSOLETE_fix\x18\x06 \x03(\x08\x12.\n\x14OBSOLETE_gps_offline\x18\x07 \x03(\x0b\x32\x10.PbSensorOffline\x12\x31\n\x16OBSOLETE_gps_date_time\x18\x08 \x03(\x0b\x32\x11.PbSystemDateTime\x12.\n\x13\x66irst_location_time\x18\t \x01(\x0b\x32\x11.PbSystemDateTime')
  ,
  dependencies=[types__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBEXERCISEROUTESAMPLES = _descriptor.Descriptor(
  name='PbExerciseRouteSamples',
  full_name='data.PbExerciseRouteSamples',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration', full_name='data.PbExerciseRouteSamples.duration', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='data.PbExerciseRouteSamples.latitude', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='data.PbExerciseRouteSamples.longitude', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_altitude', full_name='data.PbExerciseRouteSamples.gps_altitude', index=3,
      number=4, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='satellite_amount', full_name='data.PbExerciseRouteSamples.satellite_amount', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OBSOLETE_fix', full_name='data.PbExerciseRouteSamples.OBSOLETE_fix', index=5,
      number=6, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OBSOLETE_gps_offline', full_name='data.PbExerciseRouteSamples.OBSOLETE_gps_offline', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='OBSOLETE_gps_date_time', full_name='data.PbExerciseRouteSamples.OBSOLETE_gps_date_time', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_location_time', full_name='data.PbExerciseRouteSamples.first_location_time', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=345,
)

_PBEXERCISEROUTESAMPLES.fields_by_name['OBSOLETE_gps_offline'].message_type = types__pb2._PBSENSOROFFLINE
_PBEXERCISEROUTESAMPLES.fields_by_name['OBSOLETE_gps_date_time'].message_type = types__pb2._PBSYSTEMDATETIME
_PBEXERCISEROUTESAMPLES.fields_by_name['first_location_time'].message_type = types__pb2._PBSYSTEMDATETIME
DESCRIPTOR.message_types_by_name['PbExerciseRouteSamples'] = _PBEXERCISEROUTESAMPLES

PbExerciseRouteSamples = _reflection.GeneratedProtocolMessageType('PbExerciseRouteSamples', (_message.Message,), dict(
  DESCRIPTOR = _PBEXERCISEROUTESAMPLES,
  __module__ = 'data.exercise_route_pb2'
  # @@protoc_insertion_point(class_scope:data.PbExerciseRouteSamples)
  ))
_sym_db.RegisterMessage(PbExerciseRouteSamples)


# @@protoc_insertion_point(module_scope)
