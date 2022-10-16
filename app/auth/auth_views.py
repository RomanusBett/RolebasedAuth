from flask_restful import Resource, reqparse


class Login(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("username", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("password", type=str, required=True,
                        help="This field can not be left bank")

    def post(self):
        data = Login.parser.parse_args()

        username = data["username"]
        password = data["password"]

        print(">>>>>>", {username, password})
