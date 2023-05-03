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


@server.route("/get_restraunt_list")
def Test():
    return jsonify(
        {
            "list": system.roulette_system.getMemberRestaurantList(
                request.headers["member_id"]
            )
        }
    )


@server.route("/add_restraunt", methods=["POST"])
def Test2():
    system.roulette_system.addToMemberRestaurantList(
        request.headers["member_id"], request.values["name"]
    )
    return "success"


if __name__ == "__main__":
    server.run()
