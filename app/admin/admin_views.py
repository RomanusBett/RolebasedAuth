from flask_restful import Resource, reqparse

"""
 Resource - Represents an abstract RESTful resource. Concrete resources should
    extend from this class and expose methods for each supported HTTP
    method. i.e POST, GET, DELETE, UPDATE. Non-supported HTTP methods will
    return a 405 error (Method Not Allowed);

 reqparse - Enables adding parsing and validating of multiple
 arguments in the context of a single API request.
"""


class CreateMeal(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("name", type=str, required=True,
                        help="This field can not be left bank")
    parser.add_argument("price", type=int, required=True,
                        help="This field can not be left bank")

    parser.add_argument("subsidy", type=int, required=True,
                        help="This field can not be left bank")

    parser.add_argument("meal_image", type=str, required=True,
                        help="This field can not be left bank")

    def post(self):
        data = CreateMeal.parser.parse_args()
        # TODO add logic to commit data to a dabatase
