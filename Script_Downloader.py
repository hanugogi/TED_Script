from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript"
response_urllib = urlopen(url)
html_urllib = response_urllib.read()

soup_urllib = BeautifulSoup(html_urllib, "html.parser")

#with open('result.txt', 'w', encoding = 'UTF-8') as f:
#	f.write(str(soup_urllib.find_all('a')))

#	with open('result.txt', 'r', encoding = 'UTF-8') as result:
#		print(result.read())

#content > div > div:nth-child(4) > div.p\:2.p-t\:4\@md > section`