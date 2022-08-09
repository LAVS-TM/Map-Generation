from area import Area, Category

class Lake(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.LAKE, [])
