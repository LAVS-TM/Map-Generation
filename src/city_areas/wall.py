from area import Area, Category


class Wall(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.WALL)