import requests
import json
AccessToken = 'Access Token'

class DropBox():
    def __init__(self):
        self.accessToken = AccessToken
        self.urlUpload = 'https://content.dropboxapi.com/2/files/upload'
        self.urlGetMetaData = 'https://api.dropboxapi.com/2/files/get_metadata'
        self.urlDelete = 'https://api.dropboxapi.com/2/files/delete_v2'
        self.fileName = 'test file'
        self.file = 'Uploaded file.txt'
    

    def upload(self):
        parameters = {
                    'Authorization': 'Bearer {}'.format(self.accessToken),
                    'Dropbox-API-Arg': json.dumps({"path": "/homework/{}.txt".format(self.fileName), "mode": "add", "autorename": True, "mute": False, "strict_conflict": False}),
                    'Content-Type': 'application/octet-stream'
                }
        fileText = open(self.file, 'r')
        response = requests.post(self.urlUpload, headers=parameters, data = fileText)
        fileText.close()
        return response.status_code

    def getMetaData(self):
        parameters = {
            'Authorization': 'Bearer {}'.format(self.accessToken),
            'Content-Type': 'application/json'
        }
        
        inf = json.dumps({'path': "/homework/{}.txt".format(self.fileName)})
        response = requests.post(self.urlGetMetaData, headers=parameters, data=inf)
        return response.status_code

    def delete(self):
        headers = {
            'Authorization': 'Bearer {}'.format(self.accessToken),
            'Content-Type': 'application/json'
        }
        inf = json.dumps({'path': "/homework/{}.txt".format(self.fileName)})
        response = requests.post(self.urlDelete, headers=headers, data=inf)
        return response.status_code


