from area import Area, Category

class Farm(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.FARM, [])
