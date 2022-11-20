from bs4 import BeautifulSoup
import requests



html_text = requests.get('https://www.topuniversities.com/university-rankings/world-university-rankings/2022').text

print(html_text)