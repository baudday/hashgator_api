from marshmallow import Serializer, fields, pprint

class TagSerializer(Serializer):
  id  = fields.String()
  tag = fields.String()
  