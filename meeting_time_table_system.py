class MeetingTimeTableSystem:
    def __init__(self):
        self.meeting_time = self.meeting_time = {'子瑩':['1', '16:00'], '上澤': ['1', '17:00'], '宇翔': ['2', '11:00'], '如儀': ['2', '12:00'], '宗霖':['2', '16:00'], '晨睿':['3', '11:00'], '華暄':['3', '16:00'], '聖翊':['3', '17:00'], '成彥': ['4', '17:00'], '永誠':['5', '13:00'], '立軒':['5', '14:00'], '振洋':['5', '15:00']}
    def getmeeting_time(self):
        return list(self.meeting_time.items())
    def setmeeting_time(self, member, time):
        self.meeting_time[member] = time