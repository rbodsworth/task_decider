import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task("cook dinner", 30.00)

    def test_task_has_description(self):
        self.assertEqual("cook dinner", self.task.description)

    def test_task_has_duration(self):
        self.assertEqual(30.00, self.task.duration)