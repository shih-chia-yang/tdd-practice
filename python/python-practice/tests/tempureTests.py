import sys,unittest
sys.path.append("../src/temperature")
import clean,extract,export

class TempureTests(unittest.TestCase):

    def test_get_line(self):
        contents=clean.get_line("../sample/temp_data_pipes_00a.txt")
        self.assertEqual(10,len(contents)+1)

    def test_get_header(self):
        headers=['州','觀察日期','平均溫度(°F)','紀錄數量']
        clean.get_line("../sample/temp_data_pipes_00a.txt")
        self.assertEqual(len(headers),len(clean.header_list))

    def test_content_type(self):
        clean.get_line("../sample/temp_data_pipes_00a.txt")
        types=["string","string",2.3,1]
        content=list(clean.content_list.values())
        for value in content:
            index=0
            for word in value:
                self.assertTrue(type(word)==type(types[index]))
                index+=1
    
    def test_content_by_csv(self):
        path="../sample/temp_data_pipes_00a.txt"
        self.assertTrue(len(extract.getdata(path))>0)

    def test_readcsv(self):
        path="../sample/temp_data.csv"
        self.assertTrue(len(extract.readcsv(path))>0)

    def test_export_csv(self):
        path="../sample/output1.csv"
        # export.output_csv(['a','b','c','d']{'a':1,'b':2,'c':3,'d':4},path)
        export.output_csv(['a','b','c','d'],[1,2,3,4],path)
    
    def test_export_xlsx(self):
        export.output_xlsx("../../sample/output1.csv","../sample/output.xlsx")

if __name__ == '__main__':
    unittest.main()
    