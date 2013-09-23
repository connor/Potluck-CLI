#!/usr/bin/env python

from argparse import ArgumentParser

import json, webbrowser, requests, os
from termcolor import colored

class Potluck():

    def environment(self):
        """Parse any command line arguments."""
        parser = ArgumentParser(add_help=False)
        parser.add_argument('-o', nargs='+', help="Open browser to a room.")
        parser.add_argument('-h', nargs='+', help="Heart a room.")
        args = parser.parse_args()
        return args

    def __init__(self):
        self.auth_info = {}
        self.extra_headers = {}
        self.rooms = []
        self.base_route = 'https://www.potluck.it'
        self.potluck_config_file_name = '.potluck_config'
        self.potluck_cache_file_name = '.potluck_cache'


    def _get_and_set_login_file_creds(self):
        home_dir = os.path.expanduser("~")
        
        with open(os.path.join(home_dir, self.potluck_config_file_name)) as f:
            content = f.readlines()
        
        if not len(content) is 2:
            print "Whoah there - make a ~/.potluck file with\nyour email on the first line and your password\non the second line."
            return;

        self.auth_info['user[email]'] = content[0].rstrip('\n')
        self.auth_info['user[password]'] = content[1]

        return self.auth_info


    def set_auth_token(self, auth_token):
        self.auth_info['auth_token'] = auth_token


    def set_headers(self):
        self.extra_headers['X-Auth-Token'] = self.auth_info.get('auth_token')
        self.extra_headers['X-Application-Name'] = "Potluck CLI, by Connor Montgomery"


    def login(self):
        auth_info = self._get_and_set_login_file_creds()
        if not auth_info:
            return

        request = requests.post("%s/sessions.json" % self.base_route, data=auth_info)

        if not request.ok:
            print "Whoah there - authentication didn't work."
            return;

        response = json.loads(request.text)
        self.set_auth_token(response.get('auth_token'))
        self.set_headers()

        return True


    def get_set_rooms(self):
        request = requests.get("%s/rooms.json" % self.base_route, headers=self.extra_headers)
        if not request.ok:
            print "Whoah there - the request for rooms failed..."

        response = json.loads(request.text)
        self.rooms = response
        self.set_cached_rooms_data(json.dumps(self.rooms))


    def set_cached_rooms_data(self, rooms):
        home_dir = os.path.expanduser("~")
        potluck_cache_file_name = '.potluck_cache'

        with open(os.path.join(home_dir, potluck_cache_file_name), 'w+') as f:
            f.write(rooms)


    def get_cached_rooms_data(self):
        home_dir = os.path.expanduser("~")
        
        with open(os.path.join(home_dir, self.potluck_cache_file_name)) as f:
            content = f.readlines()

        return content


    def open(self, roomNumber):
        rooms = self.get_cached_rooms_data()
        rooms = json.loads(rooms[0])

        if not len(rooms):
            print "Whoah - no cached rooms"
            return

        roomNumber = roomNumber - 1
        room = rooms[roomNumber]

        if not room:
            print "Something went wrong"
            return

        room_id = room.get('identifier')
        url = "%s/rooms/%s" % (self.base_route, room_id)
        webbrowser.open_new_tab(url)


    def print_output(self):
        output = []

        for idx, room in enumerate(self.rooms):
            topic = room.get('topic')
            output += topic
            output_string = ''
            if idx <= 8:
                prefixed_space = ' '
            else:
                prefixed_space = ''
            output_string = "%s%s - %s" % (prefixed_space, idx + 1, topic)

            if room.get('unread'):
                output_string = colored(output_string, 'green')

            print output_string


    def heart(self, roomNumber):
        rooms = self.get_cached_rooms_data()
        rooms = json.loads(rooms[0])

        if not len(rooms):
            print "Whoah - no cached rooms"
            return

        roomNumber = roomNumber - 1
        room = rooms[roomNumber]

        if not room:
            print "Something went wrong"
            return

        room_id = room.get('identifier')
        url = "%s/stars?format=json" % self.base_route
        post_data = {
            'room_identifier': room_id
        }
        request = requests.post(url, data=post_data)

        if not request.ok:
            print "Whooops - something went wrong :("

        return


    def stir(self, env):
        if env.o:
            room_to_open = int(env.o[0])
            self.open(room_to_open)
            return

        if env.h:
            room_to_heart = int(env.h[0])
            self.heart(room_to_heart)
            return
    
        logged_in = self.login()

        if logged_in:
            self.get_set_rooms()

            if len(self.rooms):
                self.print_output()

        else:
            return;


    def main(self):
        args = self.environment()
        self.stir(args)
