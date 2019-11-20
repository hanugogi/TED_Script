from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = "https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript"
response_urllib = urlopen(url)
html_urllib = response_urllib.read() # 바이트코드 type으로 소스를 읽는다.

soup_urllib = BeautifulSoup(html_urllib, "html.parser") # 파싱할 문서를 BeautifulSoup 클래스의 생성자에 넘겨주어 문서 개체를 생성, 관습적으로 soup 이라 부름

p = open('response_urllib.txt', 'w')
p.write(str(response_urllib))
p.close()

response_urllib.close() # urlopen을 진행한 후에는 close를 한다.

p = open('html_urllib.txt', 'w')
p.write(str(html_urllib))
p.close()

p = open('soup_urllib.txt', 'w', encoding='UTF-8')
p.write(str(soup_urllib))
p.close()

r = requests.get(url)
p = open('source_requests.txt', 'w', encoding='UTF-8')
p.write(r.text)