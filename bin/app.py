import web
import datetime
import calendar
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from reading.scraper import *
from reading.article import Article

urls = (
	'/ringer', 'ringer',
	'/', 'index',
	'/guardian', 'guardian',
	'/atlantic', 'atlantic',
	'/espn', 'espn'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

articles = []

class index:
	def GET(self):
		today = datetime.date.today()
		month = calendar.month_name[today.month].capitalize()
		weekday = calendar.day_name[today.weekday()].capitalize()
		return render.index(month=month, weekday=weekday, today=today, articles=articles)

class ringer:
	def GET(self):
		return render.source(scraper=RINGER, action='/ringer')

	def POST(self):
		form = web.input()
		for article in form:
			new_article = Article(RINGER.get_title(int(article)), RINGER.get_link(int(article)))
			if new_article not in articles:
				articles.append(new_article)
		raise web.seeother('/')

class guardian:
	def GET(self):
		return render.source(scraper=GUARDIAN, action='/guardian')

	def POST(self):
		form = web.input()
		for article in form:
			new_article = Article(GUARDIAN.get_title(int(article)), GUARDIAN.get_link(int(article)))
			if new_article not in articles:
				articles.append(new_article)
		raise web.seeother('/')

class atlantic:
	def GET(self):
		return render.source(scraper=ATLANTIC, action='/atlantic')

	def POST(self):
		form = web.input()
		for article in form:
			new_article = Article(ATLANTIC.get_title(int(article)), ATLANTIC.get_link(int(article)))
			if new_article not in articles:
				articles.append(new_article)
		raise web.seeother('/')

class espn:
	def GET(self):
		return render.source(scraper=ESPN, action='/espn')

	def POST(self):
		form = web.input()
		for article in form:
			new_article = Article(ESPN.get_title(int(article)), ESPN.get_link(int(article)))
			if new_article not in articles:
				articles.append(new_article)
		raise web.seeother('/')

if __name__ == "__main__":
	app.run()
