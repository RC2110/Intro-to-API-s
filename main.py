import requests
from functions import send_email

key = "bb13f04fd0464da994cc7fb34d2f0ace"
topic= "tesla"
url=f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&api" \
    f"Key={key}&language=en"
request = requests.get(url)
content = request.json()

mesg=""

for i in content['articles'][:15]:
    mesg = "Subject: Daily News" + '\n' + mesg + i['title']+ '\n' +\
           i['description'] + '\n' + i['url'] + 2*'\n'

mesg = mesg.encode('UTF-8')
send_email(mesg)



