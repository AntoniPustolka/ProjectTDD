import unittest
import hello_world

class TestProgram(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(str(hello_world.print_hello), "Hello_World!")
