class SchoolTimeTableSystem:
    # def __init__(self):
    #     self.member_school_time_table = {"1111": [], "2222": [], "3333": []}

    # def getMemberRestaurantList(self, token: str):
    #     return self.member_school_time_table[token]

    def __init__(self):
        self.ClassTimeScedual = {'子瑩':[['檔案與儲存系統', ['2,5', '2,6', '2,7']], ['機器學習', ['2,8', '3,8', '3,9']], ['物件導向分析與設計', ['4,3', '4,4', '4,6']], ['專題討論', ['4,7', '4,8']], ['字體設計與文字編碼', ['5,5', '5,6', '5,7']]], 
                                 '成彥':[['安全程式設計', ['1,2', '1,3', '1,4']], ['檔案與儲存系統', ['2,5', '2,6', '2,7']], ['物件導向分析與設計', ['4,3', '4,4', '4,6']]], 
                                 '晨睿':[['檔案與儲存系統', ['2,5', '2,6', '2,7']], ['機器學習', ['2,8', '3,8', '3,9']], ['物件導向分析與設計', ['4,3', '4,4', '4,6']], ['專題討論', ['4,7', '4,8']], ['字體設計與文字編碼', ['5,5', '5,6', '5,7']]]}
    def getMemberClassTimeScedual(self, memberName):
        return self.ClassTimeScedual[memberName]
    
    # def addToMemberSchoolTimeTable(self, token: str, restaurant: str):
    #     pass
    