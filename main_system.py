from cleaning_time_table_system import CleaningTimeTableSystem
from meeting_time_table_system import MeetingTimeTableSystem
from member import Member
from roulette_system import RouletteSyetem
from school_time_table_system import SchoolTimeTableSystem

from flask import Flask, jsonify, request


class MainSystem:
    def __init__(self):
        self.cleaning_time_table_system = CleaningTimeTableSystem()
        self.meeting_time_table_system = MeetingTimeTableSystem()
        self.roulette_system = RouletteSyetem()
        self.school_time_table_system = SchoolTimeTableSystem()
        self.member_list: list[Member] = []


system = MainSystem()
server = Flask(__name__)


@server.route("/add_restraunt", methods=["POST"])
def roulette1():
    system.roulette_system.addToMemberRestaurantList(
        request.headers["member_id"], request.values["name"]
    )
    return "success"


@server.route("/clear_restraunt", methods=["POST"])
def roulette2():
    system.roulette_system.clearMemberRestaurantList(request.headers["member_id"])
    return "success"


@server.route("/get_restraunt_list", methods=["POST"])
def roulette3():
    return jsonify(
        {
            "list": system.roulette_system.getMemberRestaurantList(
                request.headers["member_id"]
            )
        }
    )


@server.route("/cleaning_get_members", methods=["POST"])
def cleaning1():
    return jsonify(
        {
            "list": system.cleaning_time_table_system.getHatarakuMembers(
                request.headers["member_id"]
            )
        }
    )


@server.route("/cleaning_get_startD", methods=["POST"])
def cleaning2():
    return jsonify(
        {
            "startD": system.cleaning_time_table_system.getSemesterStartD(
                request.headers["member_id"]
            )
        }
    )


@server.route("/cleaning_get_endD", methods=["POST"])
def cleaning3():
    return jsonify(
        {
            "endD": system.cleaning_time_table_system.getSemesterEndD(
                request.headers["member_id"]
            )
        }
    )


@server.route("/meeting_get_time", methods=["POST"])
def meeting1():
    return jsonify(
        {
            "time": system.meeting_time_table_system.getmeeting_time(
                request.headers["member_id"]
            )
        }
    )


@server.route("/course_get_time", methods=["POST"])
def course1():
    return jsonify(
        {
            "time": system.school_time_table_system.getMemberClassTimeSchedual(
                request.headers["member_id"], request.values["name"]
            )
        }
    )


@server.route("/course_get_members", methods=["POST"])
def course2():
    return jsonify(
        {
            "members": system.school_time_table_system.getAllMembers(
                request.headers["member_id"]
            )
        }
    )


if __name__ == "__main__":
    server.run()
