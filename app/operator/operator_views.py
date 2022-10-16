from flask_restful import Resource


class PostMeal(Resource):

    def post(self, food_id):
        data = PostMeal.parser.parse_args()

        name = data["name"]
        price = data["price"]
        subsidy = data["subsidy"]

