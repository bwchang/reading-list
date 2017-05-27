import web
import datetime
import calendar

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base='layout')

class index:
	# def POST(self):
	# 	form = web.input(name='Nobody', greet=None)
	# 	greeting = "%s, %s" % (form.greet, form.name)
	# 	return render.index(greeting=greeting)

	def GET(self):
		today = datetime.date.today()
		month = calendar.month_name[today.month].capitalize()
		weekday = calendar.day_name[today.weekday()].capitalize()
		return render.index(month=month, weekday=weekday, today=today)

if __name__ == "__main__":
	app.run()
