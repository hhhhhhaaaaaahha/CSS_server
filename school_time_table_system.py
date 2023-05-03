class SchoolTimeTableSystem:
    def __init__(self):
        self.token_list = ["1111"]
        self.ClassTimeScedual = {
            "子瑩": [
                ["檔案與儲存系統", ["2,5", "2,6", "2,7"]],
                ["機器學習", ["2,8", "3,8", "3,9"]],
                ["物件導向分析與設計", ["4,3", "4,4", "4,6"]],
                ["專題討論", ["4,7", "4,8"]],
                ["字體設計與文字編碼", ["5,5", "5,6", "5,7"]],
            ],
            "成彥": [
                ["安全程式設計", ["1,2", "1,3", "1,4"]],
                ["檔案與儲存系統", ["2,5", "2,6", "2,7"]],
                ["物件導向分析與設計", ["4,3", "4,4", "4,6"]],
            ],
            "晨睿": [
                ["檔案與儲存系統", ["2,5", "2,6", "2,7"]],
                ["機器學習", ["2,8", "3,8", "3,9"]],
                ["物件導向分析與設計", ["4,3", "4,4", "4,6"]],
                ["專題討論", ["4,7", "4,8"]],
                ["字體設計與文字編碼", ["5,5", "5,6", "5,7"]],
            ],
        }

    def getMemberClassTimeSchedual(self, token: str, memberName):
        if token in self.token_list:
            return self.ClassTimeScedual[memberName]
        else:
            return "Permission denied."

    def getAllMembers(self, token: str):
        if token in self.token_list:
            return list(self.ClassTimeScedual.keys())
        else:
            return "Permission denied."
