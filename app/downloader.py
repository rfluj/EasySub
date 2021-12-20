
from app import extensions

def download(url, filename):
    number   = extensions.getfilenumber.getfilenumber()
    response = extensions.requests.get(url)
    if response.status_code == 200:
        filename = 'files/' + str(number) + "_$_" + filename.replace(' ', '-') + '.zip'
        file     = open(filename, 'wb')
        file.write(response.content)
        file.close()
        return filename
    else:
        print('error in download file.please retry.')
        return False







