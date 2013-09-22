#!/usr/bin/env python

import json, webbrowser, requests, os
from termcolor import colored

class Potluck():
    def __init__(self):
        self.auth_info = {}
        self.extra_headers = {}
        self.rooms = []
        self.base_route = 'https://www.potluck.it'
        self.potluck_config_file_name = '.potluck_config'

    def _get_and_set_login_file_creds(self):
        home_dir = os.path.expanduser("~")
        potluck_config_file_name = '.potluck_config'

        with open(os.path.join(home_dir, potluck_config_file_name)) as f:
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


    def open(self, roomNumber):
        import pdb
        pdb.set_trace()
        if not len(self.rooms):
            print "Error"
            return

        roomNumber = roomNumber + 1
        room = self.rooms[roomNumber]



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



    def stir(self):
        logged_in = self.login()

        if logged_in:
            self.get_set_rooms()

            if len(self.rooms):
                self.print_output()
        else:
            print "Whoah - something went wrong."
            return;
