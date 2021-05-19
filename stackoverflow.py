import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('stackoverflow.db')
c = conn.cursor()

# c.execute('''create table stack(title text,link text,votes int,date date)''')

# url = 'https://stackoverflow.com/questions/tagged/python'


def stack(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    questions = soup.find_all('div', {'class':'question-summary'})

    for item in questions:
        title = item.find('a', {'class':'question-hyperlink'}).text
        link = item.find('a', {'class':'question-hyperlink'})['href']
        votes = int(item.find('span', {'class':'vote-count-post'}).text)
        date = item.find('span', {'class':'relativetime'})['title']
        # c.execute('''insert into stack values(?,?,?,?)''',(title,link,votes,date))


stack('https://stackoverflow.com/questions/tagged/python')


c.execute('''select * from stack''')
a = c.fetchall()
print(a)

conn.commit()
conn.close()





