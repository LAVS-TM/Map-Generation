from area import Area, Category


class Cathedral(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.CATHEDRAL, [])