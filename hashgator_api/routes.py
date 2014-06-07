from hashgator_api import api

from controllers.hello_world import HelloWorld
api.add_resource(HelloWorld, '/hello-world')
