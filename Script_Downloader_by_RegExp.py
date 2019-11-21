from urllib.request import urlopen
from bs4 import BeautifulSoup
from parse import *
import re


url = "https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript" #input("URL 입력: ")

result = list()
paragraph = list()

link_compiler = re.compile('[a-z_ ]{7,}')
line_compiler = re.compile('[A-Z].+[.?!]')

topic = link_compiler.search(url.lower())
if topic is not None:
	url = "https://www.ted.com/talks/" + topic.group().replace(' ', '_') + "/transcript"
	print(url)

url = "https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals"
url = url + '/transcript'
response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "html.parser")
p_tags = soup.find_all('div', attrs={'class': 'Grid Grid--with-gutter d:f@md p-b:4'})

'''
remove_tag = str(p_tags[0:-3]).replace('</p>, <p>', '')

for tag in p_tags:
	for r in findall('\t{}\n', str(tag)):
		paragraph.append(r.fixed[0].replace('\t', '').replace('\n', '').replace('.', '. '))

	result.append(''.join(paragraph[0:-1]))
	del(paragraph[0:-1])
	del(paragraph[0])
'''
with open('result_by_Parsing.txt', 'w', encoding = 'UTF-16') as f:
	f.write(str(p_tags))#'\n\n'.join(result))

	with open('result_by_Parsing.txt', 'r', encoding = 'UTF-16') as r:
		print(r.read())

#content > div > div:nth-child(4) > div.p\:2.p-t\:4\@md > section`