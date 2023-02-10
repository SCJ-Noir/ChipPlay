from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import render

from .connection import SocketConnection


def check_params(required_params, data):
    req = []
    for param in required_params:
        if param not in data:
            req.append(param)

    return req

def get_400(req):
    return Response(f'{req} not in request', status.HTTP_400_BAD_REQUEST)

class RoomCreationAPI(APIView):
    def post(self, request: Request):
        required_params = [
            'room_creation_id',
            'member_limit',
            'time_limit',
            'lower_betting',
            'bet_attribute'
        ]
        
        req = check_params(required_params, request.data)

        if len(req) != 0:
            return get_400(req)
        
        room_info = {
            "room_code": "vcsadf35ew1531f32cc",
            "room_pw": "fjklcvjkl132"
        }
        return Response(room_info)


class RoomJoinAPI(APIView):
    def post(self, request):
        required_params = [
            'room_code',
            'room_pw',
            'player_id'
        ]

        req = check_params(required_params, request.data)

        if len(req) != 0:
            return get_400(req)

        room_info = {
            "member_limit": 15,
            "time_limit": 20,
            "lower_betting": 5000,
            "bet_attribute": "fdsf"
        }
        return Response(room_info)
