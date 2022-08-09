from area import Area, Category

class Street(Area):

	def __init__(self, polygon):
		super().__init__(polygon, Category.STREET)
