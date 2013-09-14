from apiexception import ApiException

class Shows:

	def __init__(self):
		self.shows = []
		self.show_id = 0

	def get(self, show_id = None):
		if show_id == None:
			return self.shows
		else:
			search = filter(lambda s: s['id'] == show_id, self.shows)
			if len(search) == 0:
				raise ApiException(404, "Show not found")
			else:
				return search[0]

	def add(self, show):
		self.show_id += 1
		show['id'] = self.show_id
		self.shows.append(show)
		return show

	def update(self, show_id, data):
		show = self.get(show_id)
		show.update(data)
		return show

	def delete(self, show_id):
		show = self.get(show_id)
		self.shows.remove(show)
		return show