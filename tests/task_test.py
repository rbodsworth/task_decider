import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task("cook dinner", 30.00)