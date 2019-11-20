from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

url = "https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript"
response_urllib = urlopen(url)
html_urllib = response_urllib.read()

soup_urllib = BeautifulSoup(html_urllib, "html.parser")

p = open('response_urllib.txt', 'w')
p.write(str(response_urllib))
p.close()

response_urllib.close()

p = open('html_urllib.txt', 'w')
p.write(str(html_urllib))
p.close()

p = open('soup_urllib.txt', 'w', encoding='UTF-8')
p.write(str(soup_urllib))
p.close()

r = requests.get(url)
p = open('source_requests.txt', 'w', encoding='UTF-8')
p.write(r.text)