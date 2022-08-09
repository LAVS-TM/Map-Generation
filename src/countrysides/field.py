from area import Area, Category

class Field(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.FIELD, [])
