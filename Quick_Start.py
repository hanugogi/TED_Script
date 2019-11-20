from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.ted.com/talks/john_doerr_why_the_secret_to_success_is_setting_the_right_goals/transcript"
response = urlopen(url)
html = response.read()

soup = BeautifulSoup(html, "html.parser")

print(soup.title)
# <title>John Doerr: Why the secret to success is setting the right goals | TED Talk Subtitles and Transcript | TED</title>

print(soup.title.name)
# title

print(soup.title.string)
# John Doerr: Why the secret to success is setting the right goals | TED Talk Subtitles and Transcript | TED

print(soup.title.parent.name)
# meta

print(soup.p)
# None
print(soup.a)
# <a href="https://enable-javascript.com/">Here's how</a>

print(soup.a['href'])
# https://enable-javascript.com/

print(soup.find_all('h3'))
# [<h3 class="footer__title">
# Programs &amp; initiatives
# </h3>, <h3 class="footer__title">
# Ways to get TED
# </h3>, <h3 class="footer__title">Follow TED</h3>, <h3 class="footer__title">Our community</h3>, <h3 class="footer__title">Want personalized recommendations?</h3>, <h3 class="footer__title">Language Selector</h3>]

print(soup.find(property="og:description"))
# <meta content="TED Talk Subtitles and Transcript: Our leaders and institutions are failing us, but it's not always because they're bad or unethical, says venture capitalist John Doerr -- often, it's simply because they're leading us toward the wrong objectives. In this practical talk, Doerr shows us how we can get back on track with &quot;Objectives and Key Results,&quot; or OKRs -- a goal-setting system that's been employed by the likes of Google, Intel and Bono to set and execute on audacious goals. Learn more about how setting the right goals can mean the difference between success and failure -- and how we can use OKRs to hold our leaders and ourselves accountable." property="og:description"/>