import sys,unittest
sys.path.append("../src")
from practice2 import TypedList

param_list=[(2,3),1,2.2]
initial_list=["list","of","strings"]

class TypedListTests(unittest.TestCase):

    def setUp(self):
        self.testList=TypedList("hello",initial_list)
        return super().setUp()

    def test_check_type(self):
        for value in param_list:
            with self.assertRaises(TypeError):
                self.testList.check(value)

    def test_getitem(self):
        for value in self.testList:
            self.assertTrue(bool(value))

    def test_setitem(self):
        self.testList[0]="hello"
        self.assertEqual("hello",self.testList[0])

    def test_len(self):
        self.assertEqual(len(initial_list),len(self.testList))

    def test_delitem(self):
        del self.testList[0]
        self.assertEqual(len(initial_list)-1,len(self.testList))

    def test_append(self):
        self.testList.append("2")
        self.assertTrue( "2" in self.testList)

if __name__ == '__main__':
    unittest.main()
    