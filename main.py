
import requests, os;
from bs4 import BeautifulSoup;

sources = {
   'worldsubtitle': {
      'search': 'https://worldsubtitle.site/?s=[KEY]',
      'selector': {
         'title': 'div.cat-post-titel|a'
      } 
   },
   'subtitlestar': {
      'search': 'http://subtitlestar.com/?s=[KEY]&post_type=post',
      'selector': {
         'title': 'header.posts|div.title|a'
      }
   }
}

# download subtitle file from url
def get(url):
   if not os.path.exists('files'):
      os.mkdir('files')
   name = url.split('/')[-1];
   req = requests.get(url, allow_redirects=True, timeout=5);
   open('files/'+name, 'wb').write(req.content);
   return name;

# get string source of specific url
def reterive(src):
   resp=requests.get(src, timeout=5)
   if resp.status_code==200:
      return resp.text
   else:
      print('Error ', resp.status_code)
      return ''

def querySelector(query, soup, output):
   nodes = soup;
   selectors = query.split('|');
   for node in nodes:
      selector = selectors[0];
      results = node.findAll(selector.split('.')[0], { 'class': ' '.join(selector.split('.')[1:]) });
      if len(selectors) == 1:
         output.append(results);
         return results;
      else:
         querySelector('|'.join(selectors[1:]), results, output);
   return output;

def getSearchResult(key):
   for source in sources:
      soup = BeautifulSoup(reterive(sources[source]['search'].replace('[KEY]', key)), 'html.parser');
      titles = querySelector(sources[source]['selector']['title'], [soup], []);
      print('+'+source);
      for title in titles:
         print('\t'+title[0].text.strip());
         print('\t  '+title[0].get('href').strip());
getSearchResult('dumb and')