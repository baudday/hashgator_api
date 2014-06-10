from hashgator_api import api

from controllers.hello_world import HelloWorld
api.add_resource(HelloWorld, '/hello-world')

from controllers.tags import Tags
api.add_resource(Tags,
  '/tag',
  '/tag/<string:tag>',
  '/tags')
