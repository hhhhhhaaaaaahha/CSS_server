class RouletteSyetem:
    def __init__(self):
        self.member_restaurant = {"1111": []}

    def addToMemberRestaurantList(self, token: str, restaurant: str):
        self.member_restaurant[token].append(restaurant)
        print(self.member_restaurant[token])

    def clearMemberRestaurantList(self, token: str):
        self.member_restaurant[token].clear()
        print(self.member_restaurant[token])

    def getMemberRestaurant(self, token: str, index: int):
        return self.member_restaurant[token][index]

    def getMemberRestaurantList(self, token: str):
        return self.member_restaurant[token]

    def getMemberRestaurantCount(self, token: str) -> int:
        return len(self.member_restaurant[token])
