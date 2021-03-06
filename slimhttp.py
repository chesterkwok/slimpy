#   (c) 2012 terual
#
#   This file is part of slimpy.
#
#   slimpy is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   slimpy is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with slimpy.  If not, see <http://www.gnu.org/licenses/>.

import logging
import socket

class SlimHttp():

    def __init__(self):

        self.logger = logging.getLogger("SlimHttp")
        self.s      = None
        self.read   = None

    def close(self):
        self.read = None
        try: # to close http connection
            self.s.close()
        except AttributeError:
            pass

    def connect(self, http_header_dict):

        ##
        # Create connection

        if self.read:
            self.close()
            
        http_header = http_header_dict['http_header']
        
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(1)
        self.s.connect((http_header_dict['server_ip'], http_header_dict['server_port']))
        self.s.sendall(http_header)

        print self.s.recv(1024)
        
        self.read   = self.s.recv
        #self.read = self.s.makefile('rb', 5*1024*1024).read
        self.recv_into = self.s.recv_into
