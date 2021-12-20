
from app import extensions

def querySelector(query, soup, output):
   nodes = soup
   selectors = query.split('|')
   for node in nodes:
      selector = selectors[0]
      if '.' in selector:
         results = node.findAll(selector.split('.')[0], { 'class': ' '.join(selector.split('.')[1:]) })
      elif '#' in selector:
         results = node.findAll(selector.split('#')[0], { 'id': ' '.join(selector.split('#')[1:]) })
      else:
         results = node.findAll(selector)
      if len(selectors) == 1:
         output.append(results)
         return results
      else:
        querySelector('|'.join(selectors[1:]), results, output)
   return output

