from unittest import TestCase
from unittest.mock import patch

from server import Server


class Test(TestCase):

    @patch('server.Telnet')
    def test_init(self, mock_telnet):
        Server('a', '2222', 'c', 'd')
        mock_telnet.assert_called()

    @patch('server.Telnet')
    @patch('server.Server.send')
    def test_connect(self, mock_send, mock_telnet):
        s = Server('a', '2222', 'c', 'd')
        s.connect()
        mock_telnet().open.assert_called_with('a', 2222)

    @patch('server.Telnet')
    @patch('server.Server.send')
    def test_disconnect(self, mock_send, mock_telnet):
        s = Server('a', '2222', 'c', 'd')
        s.disconnect()
        mock_send.assert_called_with('quit')

    @patch('server.Telnet')
    @patch('server.sleep')
    def test_send_with_prompt(self, mock_sleep, mock_telnet):
        s = Server('a', '2222', 'c', 'd')
        s.send('Test message')
        mock_telnet().read_until.assert_called_with('> ')

    @patch('server.Telnet')
    @patch('server.sleep')
    def test_send_without_prompt(self, mock_sleep, mock_telnet):
        s = Server('a', '2222', 'c', 'd')
        s.send('Test message', prompt=None)
        mock_telnet().read_very_lazy.assert_called()
