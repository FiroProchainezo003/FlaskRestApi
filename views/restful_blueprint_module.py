from flask import request, Response
from flask_restful import Resource
import json


class Example1(Resource):
    def get(self):
        return {'test': 'get'}, 200

    def post(self):
        ret = request.get_data()
        param = json.loads(ret.decode('utf-8'))
        if 'line' in param:
            return {'test': 'post'}, 200
        else:
            return Response(response=json.dumps({'message': 'hello response'}), status=400)

    def put(self):
        return {'test': 'put'}, 200

    def delete(self):
        return {'test': 'delete'}, 200


# 複数作成可能
class Example2(Resource):
    def get(self, name):
        ret = request.get_json()
        print(ret)
        print(name)
        return {'test': 'Example2 get'}, 200
