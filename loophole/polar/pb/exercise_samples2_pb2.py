# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data/exercise_samples2.proto

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
  name='data/exercise_samples2.proto',
  package='data',
  syntax='proto2',
  serialized_pb=_b('\n\x1c\x64\x61ta/exercise_samples2.proto\x12\x04\x64\x61ta\x1a\x0btypes.proto\"\x8c\x03\n\x1aPbExerciseSamplesSyncPoint\x12\r\n\x05index\x18\x01 \x02(\r\x12\x19\n\x11heart_rate_sample\x18\x02 \x01(\r\x12\x16\n\x0e\x63\x61\x64\x65nce_sample\x18\x03 \x01(\r\x12\x14\n\x0cspeed_sample\x18\x04 \x01(\x02\x12\x17\n\x0f\x64istance_sample\x18\x05 \x01(\x02\x12#\n\x1b\x66orward_acceleration_sample\x18\x06 \x01(\x02\x12\x1f\n\x17\x61\x63\x63\x65leration_mad_sample\x18\n \x01(\x02\x12&\n\x18speed_sample_granularity\x18\x07 \x01(\r:\x04\x31\x30\x30\x30\x12\'\n\x1b\x64istance_sample_granularity\x18\x08 \x01(\r:\x02\x31\x30\x12\x34\n\'forward_acceleration_sample_granularity\x18\t \x01(\r:\x03\x31\x30\x30\x12\x30\n#acceleration_mad_sample_granularity\x18\x0b \x01(\r:\x03\x31\x30\x30\"\x9d\x03\n PbExerciseIntervalledSample2List\x12\"\n\x0bsample_type\x18\x01 \x02(\x0e\x32\r.PbSampleType\x12\x1d\n\x15recording_interval_ms\x18\x02 \x02(\r\x12\x34\n\nsync_point\x18\x03 \x03(\x0b\x32 .data.PbExerciseSamplesSyncPoint\x12&\n\rsample_source\x18\x04 \x03(\x0b\x32\x0f.PbSampleSource\x12\x1a\n\x12heart_rate_samples\x18\x05 \x03(\x11\x12\x17\n\x0f\x63\x61\x64\x65nce_samples\x18\x06 \x03(\x11\x12\x15\n\rspeed_samples\x18\x07 \x03(\x11\x12\x18\n\x10\x64istance_samples\x18\x08 \x03(\r\x12$\n\x1c\x66orward_acceleration_samples\x18\t \x03(\x11\x12 \n\x18\x61\x63\x63\x65leration_mad_samples\x18\x0b \x03(\x11\x12*\n\x13moving_type_samples\x18\n \x03(\x0e\x32\r.PbMovingType\"g\n\x12PbExerciseSamples2\x12Q\n!exercise_intervalled_sample2_list\x18\x01 \x03(\x0b\x32&.data.PbExerciseIntervalledSample2List')
  ,
  dependencies=[types__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBEXERCISESAMPLESSYNCPOINT = _descriptor.Descriptor(
  name='PbExerciseSamplesSyncPoint',
  full_name='data.PbExerciseSamplesSyncPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='data.PbExerciseSamplesSyncPoint.index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heart_rate_sample', full_name='data.PbExerciseSamplesSyncPoint.heart_rate_sample', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cadence_sample', full_name='data.PbExerciseSamplesSyncPoint.cadence_sample', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_sample', full_name='data.PbExerciseSamplesSyncPoint.speed_sample', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance_sample', full_name='data.PbExerciseSamplesSyncPoint.distance_sample', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward_acceleration_sample', full_name='data.PbExerciseSamplesSyncPoint.forward_acceleration_sample', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acceleration_mad_sample', full_name='data.PbExerciseSamplesSyncPoint.acceleration_mad_sample', index=6,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_sample_granularity', full_name='data.PbExerciseSamplesSyncPoint.speed_sample_granularity', index=7,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance_sample_granularity', full_name='data.PbExerciseSamplesSyncPoint.distance_sample_granularity', index=8,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward_acceleration_sample_granularity', full_name='data.PbExerciseSamplesSyncPoint.forward_acceleration_sample_granularity', index=9,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acceleration_mad_sample_granularity', full_name='data.PbExerciseSamplesSyncPoint.acceleration_mad_sample_granularity', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=100,
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
  serialized_start=52,
  serialized_end=448,
)


_PBEXERCISEINTERVALLEDSAMPLE2LIST = _descriptor.Descriptor(
  name='PbExerciseIntervalledSample2List',
  full_name='data.PbExerciseIntervalledSample2List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_type', full_name='data.PbExerciseIntervalledSample2List.sample_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recording_interval_ms', full_name='data.PbExerciseIntervalledSample2List.recording_interval_ms', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_point', full_name='data.PbExerciseIntervalledSample2List.sync_point', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sample_source', full_name='data.PbExerciseIntervalledSample2List.sample_source', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heart_rate_samples', full_name='data.PbExerciseIntervalledSample2List.heart_rate_samples', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cadence_samples', full_name='data.PbExerciseIntervalledSample2List.cadence_samples', index=5,
      number=6, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_samples', full_name='data.PbExerciseIntervalledSample2List.speed_samples', index=6,
      number=7, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance_samples', full_name='data.PbExerciseIntervalledSample2List.distance_samples', index=7,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward_acceleration_samples', full_name='data.PbExerciseIntervalledSample2List.forward_acceleration_samples', index=8,
      number=9, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acceleration_mad_samples', full_name='data.PbExerciseIntervalledSample2List.acceleration_mad_samples', index=9,
      number=11, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moving_type_samples', full_name='data.PbExerciseIntervalledSample2List.moving_type_samples', index=10,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=451,
  serialized_end=864,
)


_PBEXERCISESAMPLES2 = _descriptor.Descriptor(
  name='PbExerciseSamples2',
  full_name='data.PbExerciseSamples2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exercise_intervalled_sample2_list', full_name='data.PbExerciseSamples2.exercise_intervalled_sample2_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=866,
  serialized_end=969,
)

_PBEXERCISEINTERVALLEDSAMPLE2LIST.fields_by_name['sample_type'].enum_type = types__pb2._PBSAMPLETYPE
_PBEXERCISEINTERVALLEDSAMPLE2LIST.fields_by_name['sync_point'].message_type = _PBEXERCISESAMPLESSYNCPOINT
_PBEXERCISEINTERVALLEDSAMPLE2LIST.fields_by_name['sample_source'].message_type = types__pb2._PBSAMPLESOURCE
_PBEXERCISEINTERVALLEDSAMPLE2LIST.fields_by_name['moving_type_samples'].enum_type = types__pb2._PBMOVINGTYPE
_PBEXERCISESAMPLES2.fields_by_name['exercise_intervalled_sample2_list'].message_type = _PBEXERCISEINTERVALLEDSAMPLE2LIST
DESCRIPTOR.message_types_by_name['PbExerciseSamplesSyncPoint'] = _PBEXERCISESAMPLESSYNCPOINT
DESCRIPTOR.message_types_by_name['PbExerciseIntervalledSample2List'] = _PBEXERCISEINTERVALLEDSAMPLE2LIST
DESCRIPTOR.message_types_by_name['PbExerciseSamples2'] = _PBEXERCISESAMPLES2

PbExerciseSamplesSyncPoint = _reflection.GeneratedProtocolMessageType('PbExerciseSamplesSyncPoint', (_message.Message,), dict(
  DESCRIPTOR = _PBEXERCISESAMPLESSYNCPOINT,
  __module__ = 'data.exercise_samples2_pb2'
  # @@protoc_insertion_point(class_scope:data.PbExerciseSamplesSyncPoint)
  ))
_sym_db.RegisterMessage(PbExerciseSamplesSyncPoint)

PbExerciseIntervalledSample2List = _reflection.GeneratedProtocolMessageType('PbExerciseIntervalledSample2List', (_message.Message,), dict(
  DESCRIPTOR = _PBEXERCISEINTERVALLEDSAMPLE2LIST,
  __module__ = 'data.exercise_samples2_pb2'
  # @@protoc_insertion_point(class_scope:data.PbExerciseIntervalledSample2List)
  ))
_sym_db.RegisterMessage(PbExerciseIntervalledSample2List)

PbExerciseSamples2 = _reflection.GeneratedProtocolMessageType('PbExerciseSamples2', (_message.Message,), dict(
  DESCRIPTOR = _PBEXERCISESAMPLES2,
  __module__ = 'data.exercise_samples2_pb2'
  # @@protoc_insertion_point(class_scope:data.PbExerciseSamples2)
  ))
_sym_db.RegisterMessage(PbExerciseSamples2)


# @@protoc_insertion_point(module_scope)
