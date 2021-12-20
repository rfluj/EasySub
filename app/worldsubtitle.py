
from app import extensions

def worldsubtitlesearch(key, dic=extensions.globalvariables.worldsubtitle):
    response = extensions.reterive.reterive(dic['search'].replace('[KEY]', key))
    if response:
        soup     = extensions.BeautifulSoup(response, 'html.parser')
        titles   = extensions.querySelector.querySelector(dic['selector']['title'], [soup], [])
        result = []
        for title in titles:
            result.append({title[0].text.strip() : title[0].get('href').strip()})
        return result
    else:
        print("error in load page.please retry.")
        return False

def getdownloadurl(url, dic=extensions.globalvariables.worldsubtitle):
    response = extensions.reterive.reterive(url)
    if response:
        result      = []
        soup        = extensions.BeautifulSoup(response, 'html.parser')
        titleurls   = extensions.querySelector.querySelector(dic['selector']['download']['titleurl'], [soup], [])
        downloadurl = extensions.querySelector.querySelector(dic['selector']['download']['downloadurl'], [soup], [])
        print(downloadurl)
        for i in range(len(downloadurl[0])):
            result.append({titleurls[i].text.strip() : downloadurl[0][i].get('href').strip()})
        return result
    else:
        print("error in load page.please retry.")
        return False





