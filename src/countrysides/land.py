from area import Area, Category

class Land(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.LAND, [])