class Article():
	def __init__(self, title, link):
		self.title = title
		self.link = link

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.title == other.title and self.link == other.link
		else:
			return False
