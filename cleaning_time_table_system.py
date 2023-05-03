class CleaningTimeTableSystem:
    def __init__(self):
        self.token_list = ["1111"]
        self.hatarakuMembersThisSemester = [
            "成彥",
            "晨睿",
            "旻昌",
            "上澤",
            "宇翔",
            "駿頤",
            "韋豪",
            "子龍",
        ]
        self.semesterStartD = [2, 19]
        self.semesterEndD = [6, 21]

    def getHatarakuMembers(self, token: str):
        if token in self.token_list:
            return self.hatarakuMembersThisSemester
        else:
            return "Permission denied."

    def getSemesterStartD(self, token: str):
        if token in self.token_list:
            return self.semesterStartD
        else:
            return "Permission denied."

    def getSemesterEndD(self, token: str):
        if token in self.token_list:
            return self.semesterEndD
        else:
            return "Permission denied."

    def setHatarakuMembers(self, token: str, members):
        if token in self.token_list:
            self.hatarakuMembersThisSemester = members
        else:
            return "Permission denied."

    def setsemesterStartD(self, token: str, monthDay):
        if token in self.token_list:
            self.semesterStartD = monthDay
        else:
            return "Permission denied."
        if len(monthDay)>2:
            return "invalid month and day"
        self.semesterStartD = monthDay
    def setsemesterEndD(self, monthDay):
        self.semesterEndD = monthDay