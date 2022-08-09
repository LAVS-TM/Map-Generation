from area import Area, Category


class Townhall(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.TOWNHALL, [])