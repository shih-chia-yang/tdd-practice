from unittest import TestCase
import unittest
#測試案例可以透過繼承unittest.TestCase類別來建立。
#定義了3個物件方法，名稱皆以test開頭，此命名方法告知test runner那些方法定義為測試
class TestStringMethods(TestCase):

    #setup()、tearDown()可以設置測試初始與結束需要執行的程式
    def setUp(self):
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

    def test_upper(self):
        #assertEqual()確認執行結果是否為期望結果
        self.assertEqual('foo'.upper(),'FOO')
    
    def test_isupper(self):
        #assertTrue(), assertFalse()驗證條件式
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_spilt(self):
        s="hello world"
        self.assertEqual(s.split(),["hello","world"])
        #assertRaises驗證是否觸發一個特定exception
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
    