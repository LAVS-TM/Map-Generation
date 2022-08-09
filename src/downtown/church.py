from area import Area, Category


class Church(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.CHURCH, [])