import unittest
from PayGrades_main import NewRecordPayGrades

def test_init():
    global test
    test = NewRecordPayGrades() 

def test_Login():
    test.LoginPage()

def test_Path():
    test.PathToGrades()

def test_AddRecord():
    test.AddRecord()

def test_CheckRecord():
    test.CheckRecord()

def test_DeleteRecord():
    test.DeleteRecord()

if __name__ == '__main__':
    unittest.main()