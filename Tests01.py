import new
import unittest
from new import  *

class Tests01(unittest.TestCase):
    def test_ifemptyall(self): #если поле пустое
        print("---TEST 1")
        new.line.insert("")
        self.assertEqual(ыфввфыв, errordata)
    def test_ifnumb(self): #если введены цифры
        print("---TEST 2")
        new.line.insert("231231")
        new.main()
    def test_ifone(self): #если один символ
        print("---TEST 3")
        new.line.insert("ф")
        new.main()
    def test_chetn(self):
        print("---TEST 4") #если четное кол-во символов
        new.line.insert("выфвфывфыв")
        new.main()
    def test_nonechetn(self):
        print("---TEST 5")  # если нечетное кол-во символов
        new.line.insert("фвй")
        new.main()
    def test_lat(self):
        print("---TEST 5")  # если латиницей
        new.line.insert("dasdasddsa")
        new.main()
    def tearDown(self):
        print("Results:")
        print(restext.cget("text"))
        new.clear()