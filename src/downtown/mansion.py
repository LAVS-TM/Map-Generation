from shapely.geometry.polygon import Polygon
from area import Area, Category


class Mansion(Area):
	def __init__(self, polygon):
		super().__init__(polygon, Category.MANSION, [])

		# Création du jardin intérieur au manoir
		vertices = list(polygon.exterior.coords)
		interior = []
		bounds = polygon.bounds
		center = polygon.centroid
		for v in vertices:
			interior.append(((v[0] + center.x)/2, (v[1] + center.y) /2))
		
		new_poly = Polygon(interior)
		if polygon.contains(new_poly):
			self._polygon = Polygon(polygon.exterior.coords, [interior[::-1]])