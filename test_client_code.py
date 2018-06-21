from unittest import TestCase
from unittest.mock import Mock, PropertyMock, call

from client_code import SomeClass


class TestSomeClass(TestCase):
    def test_some_function(self):
        celsius_mock = Mock()
        temparature_mock = PropertyMock(return_value=21)
        type(celsius_mock).temperature = temparature_mock
        celsius_mock.temperature = 23
        sc = SomeClass(celsius_mock)

        sc.some_function()

        self.assertEqual(temparature_mock.mock_calls, [call(23), call()])


