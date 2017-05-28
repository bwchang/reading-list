import web
import datetime
import calendar
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from reading.scraper import RINGER
from reading.article import Article

urls = (
	'/ringer', 'ringer',
	'/', 'index',
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

articles = []

class index:
	def GET(self):
		print articles
		today = datetime.date.today()
		month = calendar.month_name[today.month].capitalize()
		weekday = calendar.day_name[today.weekday()].capitalize()
		return render.index(month=month, weekday=weekday, today=today, articles=articles)

class ringer:
	def GET(self):
		return render.ringer(scraper=RINGER)

	def POST(self):
		form = web.input()
		for article in form:
			new_article = Article(RINGER.get_title(int(article)), RINGER.get_link(int(article)))
			if new_article not in articles:
				articles.append(new_article)
		raise web.seeother('/')

if __name__ == "__main__":
	app.run()
