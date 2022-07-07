import requests
from bs4 import BeautifulSoup
base = 'https://www.acmicpc.net/user/'

user_name = 'tevem1207' # 여기에 아이디 입력
url = base + user_name

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    number = soup.find("span", id="u-solved").get_text()
    print(number)
    print(user_name)

else:
    print(response.status_code)
