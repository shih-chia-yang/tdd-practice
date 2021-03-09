import sys,unittest
sys.path.append("../src/tempure")
import clean

class TempureTests(unittest.TestCase):

    def test_get_line(self):
        contents=clean.get_line("../sample/tmpe_data_pipes_00a.txt")
        self.assertEqual(10,len(contents)+1)

    def test_get_header(self):
        headers=['州','觀察日期','平均溫度(°F)','紀錄數量']
        clean.get_line("../sample/tmpe_data_pipes_00a.txt")
        self.assertEqual(len(headers),len(clean.header_list))

    def test_content_type(self):
        clean.get_line("../sample/tmpe_data_pipes_00a.txt")
        types=["string","string",2.3,1]
        content=list(clean.content_list.values())
        for value in content:
            index=0
            for word in value:
                self.assertTrue(type(word)==type(types[index]))
                index+=1


if __name__ == '__main__':
    unittest.main()
    