from area import Area, Category


class Market(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.MARKET, [])
