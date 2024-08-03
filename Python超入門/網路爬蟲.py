import requests
from bs4 import BeautifulSoup

#html_data = requests.get('http://tw.yahoo.com')
#soup = BeautifulSoup(html_data.text, "html.parser")
#print(soup.title)

# 获取网页内容
game_ranking_html = requests.get('https://www.kamatari.org/blog/2021/best-games-of-2021/')
soup = BeautifulSoup(game_ranking_html.text, 'html.parser')

# 查找并打印所有游戏标题
for game in soup.findAll('h2'):
    print(game.text)