import unittest
from WebAPI_main import DropBox

global test
test = DropBox()

def test_upload():
    response = test.upload()
    assert response == 200, f"Error, status_code: {response}"

def test_getMetaData():
    response = test.getMetaData()
    assert response == 200, f"Error, status_code: {response}"

def test_delete():
    response = test.delete()
    assert response == 200, f"Error, status_code: {response}"

if __name__ == '__main__':
    unittest.main()

