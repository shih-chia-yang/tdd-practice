import os
from unittest import TestCase
import challenge

class ChallengeTests(TestCase):
    def setUp(self) :
        self.challenge=challenge
        return super().setUp()

    def test_os_path_should_be_return_path(self):
        self.challenge.ospath_get_path('test.log','test.log.old')
        self.assertEqual(os.path.abspath("./test.log"),self.challenge.ospath_log_path)
        self.assertEqual(os.path.abspath("./test.log.old"),self.challenge.ospath_old_log_path)

    def test_pathlib_path_should_be_equql_ospath(self):
        self.challenge.ospath_get_path('test.log','test.log.old')
        self.challenge.pathlib_get_path('test.log','test.log.old')
        self.assertEqual(self.challenge.ospath_log_path,self.challenge.another_join_path)
        self.assertEqual(self.challenge.ospath_old_log_path,self.challenge.another_join_new_path)
