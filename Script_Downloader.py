from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript"
response_urllib = urlopen(url)
html_urllib = response_urllib.read() # 바이트코드 type으로 소스를 읽는다.

soup_urllib = BeautifulSoup(html_urllib, "html.parser") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름

#with open('result.txt', 'w', encoding = 'UTF-8') as f:
#	f.write(str(soup_urllib.find_all('a')))

#	with open('result.txt', 'r', encoding = 'UTF-8') as result:
#		print(result.read())

#content > div > div:nth-child(4) > div.p\:2.p-t\:4\@md > section`