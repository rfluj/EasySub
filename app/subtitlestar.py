
from app import extensions

def subtitlestarsearch(key, dic=extensions.globalvariables.subtitlestar):
    response = extensions.reterive.reterive(dic['search'].replace('[KEY]', key))
    if response:
        soup   = extensions.BeautifulSoup(response, 'html.parser')
        # print(soup.prettify())
        # print('0000000000000000')
        titles = extensions.querySelector.querySelector(dic['selector']['title'], [soup], [])
        # print('1111111111111111')
        result = []
        for title in titles:
            result.append({title[0].text.strip() : title[0].get('href').strip()})
        return result
    else:
        print("error in load page.please retry.")
        return False

def getdownloadurl(url, dic=extensions.globalvariables.subtitlestar):
    response = extensions.reterive.reterive(url)
    if response:
        result = []
        soup   = extensions.BeautifulSoup(response, 'html.parser')
        urls   = extensions.querySelector.querySelector(dic['selector']['download'], [soup], [])
        for url in urls:
            result.append({url.text.strip() : url.get('href').strip()})
        return result
    else:
        print("error in load page.please retry.")
        return False
    






