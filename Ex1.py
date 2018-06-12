import feedparser
from bottle import route, run , request, response, get
from datetime import datetime, timedelta
import bottle as b
import json


feed = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")

new_list = []

for i in range(len(feed)):
    title = feed["entries"][i]["title"]
    link = feed["entries"][i]["link"]
    new_list.append({"title": title, "link": link})

@route('/')
def index():
    return b.template('Ex1.html')

@get('/js/<filename:re:.*\.js>')
def javascript(filename):
    return b.static_file(filename, root='js')

@get('/cookie')
def cookie():
    date_last_visited = request.get_cookie("last_visited")
    if date_last_visited:
        my_dict = {
           "last_visited_at": date_last_visited
        }
    else:
        my_dict = {
            "last_visited_at": "now"
        }
    response.set_cookie(name="last_visited",
                        value=str(datetime.now()),
                        expires=datetime.now() + timedelta(days=30))
    return 'Hello again! Your last visited us on {}.'.format(json.dumps(my_dict["last_visited_at"]))

@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return b.static_file(filename, root='css')

@get('/Ex1')
def get():
    return json.dumps(new_list)

def main():
    run(host='localhost', port=7000)


if __name__ == '__main__':
    main()