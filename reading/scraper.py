import requests
from bs4 import BeautifulSoup

class Scraper():
	def __init__(self, name, url):
		self.name = name
		page = requests.get(url)
		self.soup = BeautifulSoup(page.content, 'html.parser')
		self.titles = []
		self.links = []
		self.find_links()

	def find_links(self):
		links = self.soup.find_all('h3')
		for link in links:
			if link.find('a') and link.get_text() not in self.titles:
				self.titles.append(link.get_text())
				self.links.append(link.find('a').get('href'))
		links = self.soup.find_all('a')
		for link in links:
			if link.find('h3') and link.find('h3').get_text() not in self.titles:
				print link.find('h3').get_text()
				self.titles.append(link.find('h3').get_text())
				self.links.append(link.get('href'))
				print self.titles

	def get_titles(self):
		return self.titles

	def get_links(self):
		return self.links

	def get_title(self, index):
		return self.titles[index]

	def get_link(self, index):
		return self.links[index]


RINGER = Scraper('The Ringer', "https://theringer.com/")
