import requests
from bs4 import BeautifulSoup

class Scraper():
	def __init__(self, name, url, link_attr="", link_value="", headers=[], excludes=[]):
		self.name = name
		page = requests.get(url)
		self.soup = BeautifulSoup(page.content, 'html.parser')
		self.titles = []
		self.links = []
		self.excludes = excludes
		if headers:
			self.find_links_by_header(headers)
		if link_attr:
			self.find_links_by_attr(link_attr, link_value)

	def find_links_by_header(self, headers):
		for header in headers:
			links = self.soup.find_all(header)
			for link in links:
				if link.find('a') and self.need_to_add_link(link.get_text(), link.find('a')):
					self.titles.append(link.get_text())
					self.links.append(link.find('a').get('href'))
			links = self.soup.find_all('a')
			for link in links:
				if link.find(header) and self.need_to_add_link(link.find(header).get_text(), link):
					self.titles.append(link.find(header).get_text())
					self.links.append(link.get('href'))

	def need_to_add_link(self, title, a_tag):
		if a_tag.get('class'):
			intersection = [c for c in a_tag.get('class') if c in self.excludes]
		else:
			intersection = []
		return (not self.contains(title, a_tag.get('href'))) and (not intersection)

	def find_links_by_attr(self, link_attr, link_value):
		links = self.soup.find_all('a')
		for link in links:
			title = link.get_text(": ", strip=True)
			link_url = link.get('href')
			if link.get(link_attr) == link_value and not self.contains(title, link_url):
				self.titles.append(title)
				self.links.append(link_url)

	def contains(self, title, link):
		if title in self.titles or link in self.links:
			return True
		return False

	def get_titles(self):
		return self.titles

	def get_links(self):
		return self.links

	def get_title(self, index):
		return self.titles[index]

	def get_link(self, index):
		return self.links[index]


RINGER = Scraper('The Ringer', "https://theringer.com/", headers=["h3"])
GUARDIAN = Scraper('The Guardian', "https://www.theguardian.com/us", "data-link-name", "article")

atlantic_url = "https://www.theatlantic.com/"
atlantic_link_value = "c-popular__link--article"
atlantic_headers = ["h1", "h2", "h3"]
atlantic_excludes = ["c-recent-issues__link", "c-section__link--section-heading"]
ATLANTIC = Scraper("The Atlantic", atlantic_url, "class", atlantic_link_value, atlantic_headers, atlantic_excludes)

ESPN = Scraper("ESPN", "http://www.espn.com/", headers=["h1"])
