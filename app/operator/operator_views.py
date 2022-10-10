

class PostMeal():

    def post(self, food_id):
        data = PostMeal.parser.parse_args()

        name = data["name"]
        price = data["price"]
        subsidy = data["subsidy"]

