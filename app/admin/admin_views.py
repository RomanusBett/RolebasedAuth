from flask_restful import Resource, reqparse

"""

"""

class CreateMeal(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("price", type=str, required=True,
                        help="This field can not be left bank")

    def post(self):
        data = CreateMeal.parser.parse_args()

        print(">>>>>>>", data)

        # name = data["name"]
        # price = data["price"]
        # subsidy = data["subsidy"]
