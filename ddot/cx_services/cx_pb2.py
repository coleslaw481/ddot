# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cx.proto',
  package='cxpb',
  syntax='proto3',
  serialized_pb=_b('\n\x08\x63x.proto\x12\x04\x63xpb\"\xe8\x03\n\x07\x45lement\x12\x11\n\tnetworkId\x18\x01 \x01(\x03\x12$\n\tparameter\x18\x02 \x01(\x0b\x32\x0f.cxpb.ParameterH\x00\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x0b.cxpb.ErrorH\x00\x12\x36\n\x12numberVerification\x18\x04 \x01(\x0b\x32\x18.cxpb.NumberVerificationH\x00\x12\"\n\x08metadata\x18\x05 \x01(\x0b\x32\x0e.cxpb.MetaDataH\x00\x12\'\n\x06\x61spect\x18\x06 \x01(\x0b\x32\x15.cxpb.AnonymousAspectH\x00\x12\x1a\n\x04node\x18\x07 \x01(\x0b\x32\n.cxpb.NodeH\x00\x12\x1a\n\x04\x65\x64ge\x18\x08 \x01(\x0b\x32\n.cxpb.EdgeH\x00\x12,\n\rnodeAttribute\x18\t \x01(\x0b\x32\x13.cxpb.NodeAttributeH\x00\x12,\n\redgeAttribute\x18\n \x01(\x0b\x32\x13.cxpb.EdgeAttributeH\x00\x12\x32\n\x10networkAttribute\x18\x0b \x01(\x0b\x32\x16.cxpb.NetworkAttributeH\x00\x12\x30\n\x0f\x63\x61rtesianLayout\x18\x0c \x01(\x0b\x32\x15.cxpb.CartesianLayoutH\x00\x42\x07\n\x05value\"(\n\x12NumberVerification\x12\x12\n\nlongNumber\x18\x01 \x01(\x03\"\xa2\x01\n\x08MetaData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x11\n\tidCounter\x18\x03 \x01(\x03\x12\x14\n\x0c\x65lementCount\x18\x04 \x01(\x03\x12\x18\n\x10\x63onsistencyGroup\x18\x05 \x01(\x03\x12\x10\n\x08\x63hecksum\x18\x06 \x01(\x03\x12\"\n\nproperties\x18\x07 \x03(\x0b\x32\x0e.cxpb.Property\"\'\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"(\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"D\n\x05\x45rror\x12\x0e\n\x06status\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04link\x18\x04 \x01(\t\"?\n\x04Node\x12\x0f\n\x02id\x18\x01 \x01(\x03R\x03@id\x12\x0f\n\x04name\x18\x02 \x01(\tR\x01n\x12\x15\n\nrepresents\x18\x03 \x01(\tR\x01r\"Y\n\x04\x45\x64ge\x12\x0f\n\x02id\x18\x01 \x01(\x03R\x03@id\x12\x13\n\x08sourceId\x18\x02 \x01(\x03R\x01s\x12\x13\n\x08targetId\x18\x03 \x01(\x03R\x01t\x12\x16\n\x0binteraction\x18\x04 \x01(\tR\x01i\"l\n\rNodeAttribute\x12\x12\n\x06nodeId\x18\x01 \x01(\x03R\x02po\x12\x0f\n\x04name\x18\x02 \x01(\tR\x01n\x12\x10\n\x05value\x18\x03 \x01(\tR\x01v\x12\x0f\n\x04type\x18\x04 \x01(\tR\x01\x64\x12\x13\n\x08subnetId\x18\x05 \x01(\x03R\x01s\"l\n\rEdgeAttribute\x12\x12\n\x06\x65\x64geId\x18\x01 \x01(\x03R\x02po\x12\x0f\n\x04name\x18\x02 \x01(\tR\x01n\x12\x10\n\x05value\x18\x03 \x01(\tR\x01v\x12\x0f\n\x04type\x18\x04 \x01(\tR\x01\x64\x12\x13\n\x08subnetId\x18\x05 \x01(\x03R\x01s\"o\n\x10NetworkAttribute\x12\x12\n\x06\x65\x64geId\x18\x01 \x01(\x03R\x02po\x12\x0f\n\x04name\x18\x02 \x01(\tR\x01n\x12\x10\n\x05value\x18\x03 \x01(\tR\x01v\x12\x0f\n\x04type\x18\x04 \x01(\tR\x01\x64\x12\x13\n\x08subnetId\x18\x05 \x01(\x03R\x01s\"G\n\x0f\x43\x61rtesianLayout\x12\x0e\n\x06nodeid\x18\x01 \x01(\x03\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\x0e\n\x06viewid\x18\x04 \x01(\x03\"0\n\x0f\x41nonymousAspect\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0f\n\x07\x65lement\x18\x02 \x01(\x0c\x32\x41\n\tCyService\x12\x34\n\x0eStreamElements\x12\r.cxpb.Element\x1a\r.cxpb.Element\"\x00(\x01\x30\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ELEMENT = _descriptor.Descriptor(
  name='Element',
  full_name='cxpb.Element',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='networkId', full_name='cxpb.Element.networkId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='cxpb.Element.parameter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='cxpb.Element.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numberVerification', full_name='cxpb.Element.numberVerification', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='cxpb.Element.metadata', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aspect', full_name='cxpb.Element.aspect', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node', full_name='cxpb.Element.node', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edge', full_name='cxpb.Element.edge', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodeAttribute', full_name='cxpb.Element.nodeAttribute', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edgeAttribute', full_name='cxpb.Element.edgeAttribute', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='networkAttribute', full_name='cxpb.Element.networkAttribute', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cartesianLayout', full_name='cxpb.Element.cartesianLayout', index=11,
      number=12, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='cxpb.Element.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=19,
  serialized_end=507,
)


_NUMBERVERIFICATION = _descriptor.Descriptor(
  name='NumberVerification',
  full_name='cxpb.NumberVerification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='longNumber', full_name='cxpb.NumberVerification.longNumber', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=549,
)


_METADATA = _descriptor.Descriptor(
  name='MetaData',
  full_name='cxpb.MetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cxpb.MetaData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='cxpb.MetaData.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='idCounter', full_name='cxpb.MetaData.idCounter', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elementCount', full_name='cxpb.MetaData.elementCount', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='consistencyGroup', full_name='cxpb.MetaData.consistencyGroup', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='cxpb.MetaData.checksum', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='properties', full_name='cxpb.MetaData.properties', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=552,
  serialized_end=714,
)


_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='cxpb.Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cxpb.Property.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='cxpb.Property.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=755,
)


_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='cxpb.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='cxpb.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='cxpb.Parameter.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=757,
  serialized_end=797,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='cxpb.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cxpb.Error.status', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='cxpb.Error.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='cxpb.Error.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link', full_name='cxpb.Error.link', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=799,
  serialized_end=867,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='cxpb.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cxpb.Node.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='@id'),
    _descriptor.FieldDescriptor(
      name='name', full_name='cxpb.Node.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='n'),
    _descriptor.FieldDescriptor(
      name='represents', full_name='cxpb.Node.represents', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='r'),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=869,
  serialized_end=932,
)


_EDGE = _descriptor.Descriptor(
  name='Edge',
  full_name='cxpb.Edge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cxpb.Edge.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='@id'),
    _descriptor.FieldDescriptor(
      name='sourceId', full_name='cxpb.Edge.sourceId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='s'),
    _descriptor.FieldDescriptor(
      name='targetId', full_name='cxpb.Edge.targetId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='t'),
    _descriptor.FieldDescriptor(
      name='interaction', full_name='cxpb.Edge.interaction', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='i'),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=934,
  serialized_end=1023,
)


_NODEATTRIBUTE = _descriptor.Descriptor(
  name='NodeAttribute',
  full_name='cxpb.NodeAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeId', full_name='cxpb.NodeAttribute.nodeId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='po'),
    _descriptor.FieldDescriptor(
      name='name', full_name='cxpb.NodeAttribute.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='n'),
    _descriptor.FieldDescriptor(
      name='value', full_name='cxpb.NodeAttribute.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='v'),
    _descriptor.FieldDescriptor(
      name='type', full_name='cxpb.NodeAttribute.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='d'),
    _descriptor.FieldDescriptor(
      name='subnetId', full_name='cxpb.NodeAttribute.subnetId', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='s'),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1025,
  serialized_end=1133,
)


_EDGEATTRIBUTE = _descriptor.Descriptor(
  name='EdgeAttribute',
  full_name='cxpb.EdgeAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edgeId', full_name='cxpb.EdgeAttribute.edgeId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='po'),
    _descriptor.FieldDescriptor(
      name='name', full_name='cxpb.EdgeAttribute.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='n'),
    _descriptor.FieldDescriptor(
      name='value', full_name='cxpb.EdgeAttribute.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='v'),
    _descriptor.FieldDescriptor(
      name='type', full_name='cxpb.EdgeAttribute.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='d'),
    _descriptor.FieldDescriptor(
      name='subnetId', full_name='cxpb.EdgeAttribute.subnetId', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='s'),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1135,
  serialized_end=1243,
)


_NETWORKATTRIBUTE = _descriptor.Descriptor(
  name='NetworkAttribute',
  full_name='cxpb.NetworkAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edgeId', full_name='cxpb.NetworkAttribute.edgeId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='po'),
    _descriptor.FieldDescriptor(
      name='name', full_name='cxpb.NetworkAttribute.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='n'),
    _descriptor.FieldDescriptor(
      name='value', full_name='cxpb.NetworkAttribute.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='v'),
    _descriptor.FieldDescriptor(
      name='type', full_name='cxpb.NetworkAttribute.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='d'),
    _descriptor.FieldDescriptor(
      name='subnetId', full_name='cxpb.NetworkAttribute.subnetId', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='s'),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1245,
  serialized_end=1356,
)


_CARTESIANLAYOUT = _descriptor.Descriptor(
  name='CartesianLayout',
  full_name='cxpb.CartesianLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodeid', full_name='cxpb.CartesianLayout.nodeid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='cxpb.CartesianLayout.x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='cxpb.CartesianLayout.y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='viewid', full_name='cxpb.CartesianLayout.viewid', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1358,
  serialized_end=1429,
)


_ANONYMOUSASPECT = _descriptor.Descriptor(
  name='AnonymousAspect',
  full_name='cxpb.AnonymousAspect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='cxpb.AnonymousAspect.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='element', full_name='cxpb.AnonymousAspect.element', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1431,
  serialized_end=1479,
)

_ELEMENT.fields_by_name['parameter'].message_type = _PARAMETER
_ELEMENT.fields_by_name['error'].message_type = _ERROR
_ELEMENT.fields_by_name['numberVerification'].message_type = _NUMBERVERIFICATION
_ELEMENT.fields_by_name['metadata'].message_type = _METADATA
_ELEMENT.fields_by_name['aspect'].message_type = _ANONYMOUSASPECT
_ELEMENT.fields_by_name['node'].message_type = _NODE
_ELEMENT.fields_by_name['edge'].message_type = _EDGE
_ELEMENT.fields_by_name['nodeAttribute'].message_type = _NODEATTRIBUTE
_ELEMENT.fields_by_name['edgeAttribute'].message_type = _EDGEATTRIBUTE
_ELEMENT.fields_by_name['networkAttribute'].message_type = _NETWORKATTRIBUTE
_ELEMENT.fields_by_name['cartesianLayout'].message_type = _CARTESIANLAYOUT
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['parameter'])
_ELEMENT.fields_by_name['parameter'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['error'])
_ELEMENT.fields_by_name['error'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['numberVerification'])
_ELEMENT.fields_by_name['numberVerification'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['metadata'])
_ELEMENT.fields_by_name['metadata'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['aspect'])
_ELEMENT.fields_by_name['aspect'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['node'])
_ELEMENT.fields_by_name['node'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['edge'])
_ELEMENT.fields_by_name['edge'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['nodeAttribute'])
_ELEMENT.fields_by_name['nodeAttribute'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['edgeAttribute'])
_ELEMENT.fields_by_name['edgeAttribute'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['networkAttribute'])
_ELEMENT.fields_by_name['networkAttribute'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_ELEMENT.oneofs_by_name['value'].fields.append(
  _ELEMENT.fields_by_name['cartesianLayout'])
_ELEMENT.fields_by_name['cartesianLayout'].containing_oneof = _ELEMENT.oneofs_by_name['value']
_METADATA.fields_by_name['properties'].message_type = _PROPERTY
DESCRIPTOR.message_types_by_name['Element'] = _ELEMENT
DESCRIPTOR.message_types_by_name['NumberVerification'] = _NUMBERVERIFICATION
DESCRIPTOR.message_types_by_name['MetaData'] = _METADATA
DESCRIPTOR.message_types_by_name['Property'] = _PROPERTY
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Edge'] = _EDGE
DESCRIPTOR.message_types_by_name['NodeAttribute'] = _NODEATTRIBUTE
DESCRIPTOR.message_types_by_name['EdgeAttribute'] = _EDGEATTRIBUTE
DESCRIPTOR.message_types_by_name['NetworkAttribute'] = _NETWORKATTRIBUTE
DESCRIPTOR.message_types_by_name['CartesianLayout'] = _CARTESIANLAYOUT
DESCRIPTOR.message_types_by_name['AnonymousAspect'] = _ANONYMOUSASPECT

Element = _reflection.GeneratedProtocolMessageType('Element', (_message.Message,), dict(
  DESCRIPTOR = _ELEMENT,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.Element)
  ))
_sym_db.RegisterMessage(Element)

NumberVerification = _reflection.GeneratedProtocolMessageType('NumberVerification', (_message.Message,), dict(
  DESCRIPTOR = _NUMBERVERIFICATION,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.NumberVerification)
  ))
_sym_db.RegisterMessage(NumberVerification)

MetaData = _reflection.GeneratedProtocolMessageType('MetaData', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.MetaData)
  ))
_sym_db.RegisterMessage(MetaData)

Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTY,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.Property)
  ))
_sym_db.RegisterMessage(Property)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETER,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.Parameter)
  ))
_sym_db.RegisterMessage(Parameter)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.Error)
  ))
_sym_db.RegisterMessage(Error)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), dict(
  DESCRIPTOR = _NODE,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.Node)
  ))
_sym_db.RegisterMessage(Node)

Edge = _reflection.GeneratedProtocolMessageType('Edge', (_message.Message,), dict(
  DESCRIPTOR = _EDGE,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.Edge)
  ))
_sym_db.RegisterMessage(Edge)

NodeAttribute = _reflection.GeneratedProtocolMessageType('NodeAttribute', (_message.Message,), dict(
  DESCRIPTOR = _NODEATTRIBUTE,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.NodeAttribute)
  ))
_sym_db.RegisterMessage(NodeAttribute)

EdgeAttribute = _reflection.GeneratedProtocolMessageType('EdgeAttribute', (_message.Message,), dict(
  DESCRIPTOR = _EDGEATTRIBUTE,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.EdgeAttribute)
  ))
_sym_db.RegisterMessage(EdgeAttribute)

NetworkAttribute = _reflection.GeneratedProtocolMessageType('NetworkAttribute', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKATTRIBUTE,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.NetworkAttribute)
  ))
_sym_db.RegisterMessage(NetworkAttribute)

CartesianLayout = _reflection.GeneratedProtocolMessageType('CartesianLayout', (_message.Message,), dict(
  DESCRIPTOR = _CARTESIANLAYOUT,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.CartesianLayout)
  ))
_sym_db.RegisterMessage(CartesianLayout)

AnonymousAspect = _reflection.GeneratedProtocolMessageType('AnonymousAspect', (_message.Message,), dict(
  DESCRIPTOR = _ANONYMOUSASPECT,
  __module__ = 'cx_pb2'
  # @@protoc_insertion_point(class_scope:cxpb.AnonymousAspect)
  ))
_sym_db.RegisterMessage(AnonymousAspect)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class CyServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.StreamElements = channel.stream_stream(
          '/cxpb.CyService/StreamElements',
          request_serializer=Element.SerializeToString,
          response_deserializer=Element.FromString,
          )


  class CyServiceServicer(object):

    def StreamElements(self, request_iterator, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_CyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'StreamElements': grpc.stream_stream_rpc_method_handler(
            servicer.StreamElements,
            request_deserializer=Element.FromString,
            response_serializer=Element.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'cxpb.CyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaCyServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def StreamElements(self, request_iterator, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaCyServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def StreamElements(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()


  def beta_create_CyService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('cxpb.CyService', 'StreamElements'): Element.FromString,
    }
    response_serializers = {
      ('cxpb.CyService', 'StreamElements'): Element.SerializeToString,
    }
    method_implementations = {
      ('cxpb.CyService', 'StreamElements'): face_utilities.stream_stream_inline(servicer.StreamElements),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_CyService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('cxpb.CyService', 'StreamElements'): Element.SerializeToString,
    }
    response_deserializers = {
      ('cxpb.CyService', 'StreamElements'): Element.FromString,
    }
    cardinalities = {
      'StreamElements': cardinality.Cardinality.STREAM_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'cxpb.CyService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)