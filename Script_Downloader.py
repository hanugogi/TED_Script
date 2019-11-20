from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript"
response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "html.parser")

p_tags = soup.find_all('p')
remove_tag = str(p_tags[0:-3]).replace('</p>, <p>', '')
remove_tab = remove_tag.replace('\t\t\t\t\t\t\t\t\t\t', '')
remove_tab = remove_tab.replace('\t', '')
result = remove_tab.replace('\n', '').replace('.', '.\n').replace('?', '.\n')

print(result)

#print(str(soup.p.get_text()).replace('\t\t\t\t\t\t\t\t\t\t\t', '').replace('\n', ' ').replace('.', '.\n'))

#print(''.join(str(list(p_tags)[0]).split('\t\t\t\t\t\t\t\t\t\t\t')))

with open('result.txt', 'w', encoding = 'UTF-8') as f:
	f.write(result)

	with open('result.txt', 'r', encoding = 'UTF-8') as result:
		print(result.read())

#content > div > div:nth-child(4) > div.p\:2.p-t\:4\@md > section`