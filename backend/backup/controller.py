

@api.route('/usuarios')
class UserController(Resource):
    @api.marshal_list_with(usuario)
    def get(self):
        '''List all tasks'''
        return 'todo', 200

    @api.expect(usuario)
    @api.marshal_with(usuario, code=201)
    def post(self):
        return api.payload, 201

if __name__ == '__main__':
    app.run(debug=True)