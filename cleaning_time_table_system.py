class CleaningTimeTableSystem:
    def __init__(self):
        self.hatarakuMembersThisSemester= ['成彥', '晨睿', '旻昌', '上澤', '宇翔', '駿頤', '韋豪', '子龍']
        self.semesterStartD = [2, 19]
        self.semesterEndD = [6, 21]

    def getHatarakuMembers(self):
        return self.hatarakuMembersThisSemester
    def getSemesterStartD(self):
        return self.semesterStartD
    def getSemesterEndD(self):
        return self.semesterEndD
    def setHatarakuMembers(self, members):
        self.hatarakuMembersThisSemester = members
    def setsemesterStartD(self, monthDay):
        self.semesterStartD = monthDay
    def setsemesterEndD(self, monthDay):
        self.semesterEndD = monthDay