from area import Area, Category


class Garden(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.GARDEN)