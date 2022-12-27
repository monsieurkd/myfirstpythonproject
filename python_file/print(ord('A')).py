print(type(b'abc'))


import urllib.request, urllib.parse, urllib.error



from bs4 import BeautifulSoup

fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt').read()

bs = BeautifulSoup(fhand, 'html.parser')

tags = bs('h1')
for tag in tags:
    print(tag.get('', None))

print(bs.prettify())