class RouletteSyetem:
    def __init__(self):
        self.member_restaurant = {"1111": []}

    def getMemberRestaurantList(self, token: str):
        return self.member_restaurant[token]

    def addToMemberRestaurantList(self, token: str, restaurant: str):
        self.member_restaurant[token].append(restaurant)

    def clearMemberRestaurantList(self, token: str, restaurant: str):
        self.member_restaurant[token] = []
