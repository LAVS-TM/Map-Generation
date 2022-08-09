from area import Area, Category

class District(Area):

	def __init__(self, polygon, sub_areas):
		super().__init__(polygon, Category.COMPOSITE, sub_areas=sub_areas)

	
		