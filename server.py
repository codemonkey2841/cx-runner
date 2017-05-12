from random import uniform
from telnetlib import Telnet
from time import sleep


class Server(object):

    def __init__(self, host, port, user, password, connect=False):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.conn = Telnet()

        if connect:
            self.connect()

    def connect(self):
        """
        Run through the authentication procedure
        """

        self.conn.open(self.host, self.port)
        self.conn.read_until('What is your name: ')
        self.send(self.user, prompt=None)
        self.send(self.password, prompt=None)
        sleep(1)

    def disconnect(self):
        """
        Disconnect from MUD.
        """

        self.send('quit')

    def send(self, message, prompt='> ', delay=0, jitter=1):
        """
        Send a message to the telnet server.
        """

        preamble = self.conn.read_very_eager()
        msg = '{}\n'.format(message).encode('ascii', 'ignore')
        self.conn.write(msg)
        if prompt:
            result = self.conn.read_until(prompt)
        else:
            result = self.conn.read_very_lazy()
        sleep(delay + uniform(0, jitter))
        return (preamble, result)
