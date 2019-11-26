from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input("URL: ")
result = []

link_compiler = re.compile('[a-z_ ]{7,}')
line_compiler = re.compile('[\t\n][0-9a-z A-Z\',.?!@\-\'\"():]+')

topic = link_compiler.search(url.lower())
path = 'Scripts\\' + topic.group().replace('_', ' ') + '.txt'
if topic is not None:
	url = "https://www.ted.com/talks/" + topic.group().replace(' ', '_') + "/transcript"
	print(url)
	response = urlopen(url)
	html = response.read()

	soup = BeautifulSoup(html, "html.parser")
	p_tags = soup.find_all('div', attrs={'class': 'Grid Grid--with-gutter d:f@md p-b:4'})

	for tag in p_tags:
		lines = line_compiler.findall(str(tag))
		result.append(' '.join(lines).replace('\n', ''))

	with open(path, 'w', encoding='UTF-16') as f:
		f.write('\n\n'.join(result).replace('\t', ''))
		print('Script is saved at .\\' + path)
		#with open(path, 'r', encoding='UTF-16') as r:
		#	print(r.read())
else:
	print('Input is not correct')
#content > div > div:nth-child(4) > div.p\:2.p-t\:4\@md > section`