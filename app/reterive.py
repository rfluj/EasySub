
from app import extensions

def reterive(url):
   resp = extensions.requests.get(url, timeout=5)
   if resp.status_code==200:
      return resp.text
   else:
      print('Error.status code : ', resp.status_code)
      return False

