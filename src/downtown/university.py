from area import Area, Category


class University(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.UNIVERSITY, [])