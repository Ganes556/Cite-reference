from newspaper import Article
from babel.dates import format_date, format_datetime, format_time
from datetime import date,datetime,time
url = "https://id.wikipedia.org/wiki/Informasi"
a = Article(url)
a.download()
a.parse()
print(format_date(a.publish_date,format="long",locale="in"))
# date2 = date(date.day,date.month,date.year)
# print(format_date(a.publish_date,format="long",locale="in").split(" ")[0])

# dateEntrys = {"Day" : [1,2],"Month" : [2,12],"Year" : [2222,2221]}

# def test(**data):
#     print(data["Day"])
# test(**dateEntrys)

# print(datetime.datetime.today().hour)