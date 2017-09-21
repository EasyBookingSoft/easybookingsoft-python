import requests
from requests import Request


class BookingEngine:
    def __init__(self, token, endpoint='https://www.easybookingsoft.com/api/v1/'):
        endpoint = endpoint

    def get_api(self, method, payload=None, endpoint=None):
        url = "{}{}/".format(self.endpoint, endpoint)
        headers = {'Authorization': "Token {}".format(self.token)}

        return requests.get(url, headers=headers).json()

    def get_rooms(self):
        """Get all rooms"""
        resp = self.get_api('GET', None, 'rooms')
        return resp

    def get_room_types(self):
        """Get all Room types"""
        resp = self.get_api('GET', None, 'room-types')
        return resp

    def get_availability(self, roomtype, checkin, checkout):
        """Get available rooms for given date"""
        resp = self.get_api('GET', None, 'room-types')

    def make_reservation(self, data):
        """Makes reservation"""
        url = "{}{}/".format(self.endpoint, 'makereservation')
        headers = {'Authorization': "Token {}".format(self.token)}
        data = data
        json_data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email': data['last_name'],
            'date': [data['checkin'].strftime('%Y-%m-%d'), data['checkout'].strftime('%Y-%m-%d')]
        }
        resp = requests.post(url, json=json_data, headers=headers)
        if resp.status_code != 200:
            raise ValueError()

        if not resp.json():
            return False

        return resp
