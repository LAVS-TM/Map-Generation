from area import Area, Category


class Castle(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.CASTLE, [])