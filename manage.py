# from sqlalchemy import create_engine
# from sshtunnel import SSHTunnelForwarder
# from sqlalchemy.orm import sessionmaker
# from ScholarConfig.config import DB_CONFIG
# # server = SSHTunnelForwarder(
# #         ('13.113.193.188',22),
# #         ssh_username="ubuntu",
# #         ssh_pkey="C:/Users/tonylu/Desktop/eb-web(1).pem",
# #         remote_bind_address=('localhost',3306)
# #         )
# # server.start()
# #
# # print(server.local_bind_port)
# # enginee = create_engine("mysql+pymysql://root:root@localhost:{}/eb".format(server.local_bind_port))
# # Session=sessionmaker(bind=enginee)
# # b=Session()
# # c=b.execute("select * from groups")
# # print(c.)
#
# # from requests import put,get,delete,post
# # data = {'task': 'hahaha'}
# # print(get('http://localhost:5000/todos').json())
# # print(get('http://localhost:5000/todos/todo3').json())
# # print(delete('http://localhost:5000/todos/todo2'))
# # print(post('http://localhost:5000/todos',data=data).json())
# # print(put('http://localhost:5000/todos/todo3',data=data).json())
# # print(get('http://localhost:5000/todos').json())
#
# # from flask_restful import fields, marshal
# # import json
# # resource_fields = {'name': fields.String}
# # resource_fields['address'] = {}
# # resource_fields['address']['line 1'] = fields.String(attribute='addr1')
# # resource_fields['address']['line 2'] = fields.String(attribute='addr2')
# # resource_fields['address']['city'] = fields.String
# # resource_fields['address']['state'] = fields.String
# # resource_fields['address']['zip'] = fields.String
# # data = {'name': 'bob', 'addr1': '123 fake street', 'addr2': '', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
# # print(json.dumps(marshal(data, resource_fields)))
#
# # from flask_restful import fields,marshal
# # import json
# # resource_fields = {'name': fields.String, 'first_names': fields.List(fields.String)}
# # data = {'name': 'Bougnazal', 'first_names' : ['Emile', 'Raoul']}
# # json.dumps(marshal(data, resource_fields))
#
# from flask_restful import fields, marshal
# import json
# from pprint import pprint
# from utils.pretty_dict import pretty_dict
# address_fields = {}
# address_fields['line 1'] = fields.String(attribute='addr1')
# address_fields['line 2'] = fields.String(attribute='addr2')
# address_fields['city'] = fields.String(attribute='city')
# address_fields['state'] = fields.String(attribute='state')
# address_fields['zip'] = fields.String(attribute='zip')
# resource_fields = {}
# resource_fields['name'] = fields.String
# resource_fields['billing_address'] = fields.Nested(address_fields)
# resource_fields['shipping_address'] = fields.Nested(address_fields)
# address1 = {'addr1': '123 fake street', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
# address2 = {'addr1': '555 nowhere', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
# data = { 'name': 'bob', 'billing_address': address1, 'shipping_address': address2}
# pretty_dict((marshal(data, resource_fields)))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
from flask import Flask
from flask_restplus import Api, Resource, fields, cors

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resource={"/api/*": {"origins": "*"}})
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('api', description='TODO operations')



@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@ns.route('/')

class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    #@ns.marshal_list_with()
    #
    def get(self):
        '''List all tasks'''
        return {
  "data": [
    { "id": 1, "name": "Windstorm" },
    { "id": 2, "name": "Bombasto" },
    { "id": 3, "name": "Magneta" },
    { "id": 4, "name": "Tornado" }
  ]
}

@ns.route('/<int:id>')
class Todo(Resource):
    def get(self,id):
        return {
            "data": {"id":id,"name":"wz"}
        }

    def put(self,id):
        return {
            "data": {"id": id, "name": "wz"}
        }



if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=3004)