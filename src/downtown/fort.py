from area import Area, Category


class Fort(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.FORT, [])