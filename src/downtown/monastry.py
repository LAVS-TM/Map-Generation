from area import Area, Category


class Monastry(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.MONASTRY, [])