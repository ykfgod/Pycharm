import new
import unittest
from new import  *

class Tests01(unittest.TestCase):
    def test_ifemptyall(self): #если поле пустое
        print("---TEST 1")
        new.line.insert(0, "")
        new.main()
        self.assertEqual("Введите строку!", errordata)
    def test_ifnumb(self): #если введены цифры
        print("---TEST 2")
        new.line.insert(0, "231231")
        new.main()
    def test_ifone(self): #если один символ
        print("---TEST 3")
        new.line.insert(0, "ф")
        new.main()
    def test_chetn(self):
        print("---TEST 4") #если четное кол-во символов
        new.line.insert(0, "выфвфывфыв")
        new.main()
    def test_nonechetn(self):
        print("---TEST 5")  # если нечетное кол-во символов
        new.line.insert(0, "фвй")
        new.main()
    def test_lat(self):
        print("---TEST 6")  # если латиницей
        new.line.insert(0, "dasdasddsa")
        new.main()
    def tearDown(self):
        print("Results:")
        print(restext.cget("text"))
        new.clear()
if __name__ == '__main__':
        unittest.main()