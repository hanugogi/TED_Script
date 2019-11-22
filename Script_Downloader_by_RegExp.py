from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'john_doerr_why_the_secret_to_success_is_setting_the_right_goals'#input("URL: ")
result = []

link_compiler = re.compile('[a-z_ ]{7,}')
line_compiler = re.compile('[\t\n][0-9a-z A-Z\',.?!@\-\'\"():]+')

topic = link_compiler.search(url.lower())
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

	with open('result_by_RegExp.txt', 'w', encoding='UTF-16') as f:
		f.write('\n\n'.join(result).replace('\t', ''))
		with open('result_by_RegExp.txt', 'r', encoding='UTF-16') as r:
			print(r.read())
else:
	print('Input is not correct')
#content > div > div:nth-child(4) > div.p\:2.p-t\:4\@md > section`