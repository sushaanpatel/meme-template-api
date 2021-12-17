from flask import Flask
from mongo import get_all, get_one
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class GetAll(Resource):
    def get(self):
        return get_all()

class GetOne(Resource):
    def get(self, name):
        return get_one(name)

api.add_resource(GetAll, '/getall')
api.add_resource(GetOne, '/getone/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)