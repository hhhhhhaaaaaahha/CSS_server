from cleaning_time_table_system import CleaningTimeTableSystem
from meeting_time_table_system import MeetingTimeTableSystem
from member import Member
from roulette_system import RouletteSyetem
from school_time_table_system import SchoolTimeTableSystem

from flask import Flask, jsonify, request
from flask_restful import Resource, Api


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


@server.route("/get_restraunt", methods=["POST"])
def roulette3():
    return jsonify(
        {
            "name": system.roulette_system.getMemberRestaurant(
                request.headers["member_id"], int(request.values["index"])
            )
        }
    )


@server.route("/get_restraunt_count", methods=["POST"])
def roulette4():
    return jsonify(
        {
            "count": system.roulette_system.getMemberRestaurantCount(
                request.headers["member_id"]
            )
        }
    )


@server.route("/get_restraunt_list", methods=["POST"])
def roulette5():
    return jsonify(
        {
            "list": system.roulette_system.getMemberRestaurantList(
                request.headers["member_id"]
            )
        }
    )


if __name__ == "__main__":
    server.run()
