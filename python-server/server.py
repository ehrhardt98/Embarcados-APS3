from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Digital(Resource):
    def get(self):
        id = request.args.get("id")
        print(id)
        return {'digital': '1'}

class Afec(Resource):
    def get(self):
        id = request.args.get("id")
        print(id)
        pot = request.args.get("pot")
        return {'afec' : pot}

class Time(Resource):
    def get(self):
        id = request.args.get("id")
        hora = request.args.get("hora")
        min = request.args.get("min")
        sec = request.args.get("sec")
        print(id)
        return {"tempo" : "recebido"}

#class TodoSimple(Resource):
#    def get(self, todo_id):
#        return {todo_id: todos[todo_id]}
#
#    def put(self, todo_id):
#        todos[todo_id] = request.form['data']
#        return {todo_id: todos[todo_id]}

#api.add_resource(TodoSimple, '/<string:todo_id>')
#api.add_resource(HelloWorld, '/')
api.add_resource(Digital, '/d')
api.add_resource(Afec, '/afec')
api.add_resource(Time, '/time')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    #app.run(debug=True)

