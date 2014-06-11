from flask import jsonify
from flask.ext import restful
from marshmallow import Serializer, fields, pprint
from hashgator_api import db
from hashgator_api.models.tag import Tag
from hashgator_api.serializers.tag_serializer import TagSerializer
from flask.ext.restful import reqparse
import uuid

parser = reqparse.RequestParser()

class Tags (restful.Resource):
  def get(self, tag=False):
    if(tag):
      tags = Tag.query.filter(Tag.tag.contains(tag)).all()
    else:
      tags = Tag.query.all()

    return TagSerializer(tags, many=True).data, 200

  def post(self):
    parser.add_argument('tag', type=str)
    args = parser.parse_args()
    tag = Tag(str(uuid.uuid4()), args['tag'])
    db.session.add(tag)
    db.session.commit()
    return TagSerializer(tag).data, 200
