import numpy as np
import random

from scipy.spatial import Voronoi
from shapely.geometry import Polygon, LineString, Point, MultiPolygon
from shapely.ops import polygonize, unary_union

from downtown.cathedral import Cathedral
from downtown.church import Church
from downtown.fort import Fort
from downtown.garden import Garden
from downtown.house import House
from downtown.mansion import Mansion
from downtown.market import Market
from downtown.monastry import Monastry
from downtown.park import Park
from downtown.townhall import Townhall
from downtown.university import University

from countrysides.farm import Farm
from countrysides.field import Field
from countrysides.forest import Forest
from countrysides.lake import Lake
from countrysides.land import Land

def generate_regions(regions_size):
    '''
    Crée la carte et la découpe en Polygon qui deviendront nos district

    Args:
        regions_size: int - taille des régions généré
    Returns:
        regions: List - liste de Polygon représentant les districts crées
    Tests:
        >>> district = generate_regions(10)
    '''
    N = regions_size
    radius = (N-2)
    points = np.array([[x, y] for x in np.linspace(-1, 1, N)
                      for y in np.linspace(-1, 1, N)])
    points *= radius
    points += np.random.random((len(points), 2)) * (radius / 3)
    vor = Voronoi(points)

    regions = [r for r in vor.regions if -1 not in r and len(r) > 0]
    regions = [Polygon([vor.vertices[i] for i in r]) for r in regions]

    zone = Polygon((2 * np.random.random((8, 2)) - 1) *
                   radius).convex_hull.buffer(radius/2)

    regions = [r for r in regions if zone.contains(r)]

    return regions

def generate_buildings(regions_size, district):
    '''
    Génere les emplacements d'élément de la carte dans le district donné.

    Args:
        regions_size: int - taille des régions généré
        district: Polygon - Le district dans lequel les régions sont généré
    Returns:
        regions: List - liste de Polygon représentant les zones crées
    Tests:
        >>> district = Polygon([(0.75, -0.98), (0.66, -1), (-0.3, -0.88), (-0.88, -0.19), (-0.95, 0.20), (-0.89, 0.48), (0.53, 1.07), (1.11, 0.19), (0.74, -0.97)])
        >>> batiment = generate_buildings(10, district)
    '''
    N = regions_size
    bounds = district.bounds
    radius = 1

    points = []

    for x in np.linspace(bounds[0], bounds[2], N):
        for y in np.linspace(bounds[1], bounds[3], N):
            p = Point(x, y)
            if district.contains(p):
                points.append([x, y])

    points = np.array(points)
    points += np.random.random((len(points), 2)) * (radius / 9)

    l = list(district.exterior.coords)
    for i in range(len(l)):
        np.append(points, [l[i][0], l[i][1]])

    vor = Voronoi(points)

    lines = [
        LineString(vor.vertices[line])
        for line in vor.ridge_vertices if -1 not in line
    ]

    result = MultiPolygon(
        [poly.intersection(district) for poly in polygonize(lines)])
    if isinstance(result, MultiPolygon):
        diff = district.difference(unary_union(result))
        if isinstance(diff, MultiPolygon):
            result = MultiPolygon(
                [p for p in result]
                + [p for p in diff])
        else:
            result = MultiPolygon([p for p in result] + [diff])
    else:
        result = [district.difference(unary_union(result))]

    regions = []
    for r in result:
        if isinstance(r, Polygon):
            regions.append(r)

    return MultiPolygon(regions)


def split_region(regions, road_size):
    '''
    Sépare les régions et créé une route à l'endroit de l'intersection.

    Args:
        regions: List - liste de Polygon à séparer au niveau de leurs intersections
        road_size: float - taille de la route créé
    Returns:
        new_regions: List - liste de Polygon représentant les régions crées
        streets - liste de Polygon représentant les routes crées
    Tests:
        >>> regions = [Polygon([(-2.3, 0.6), (-2.3, -0.1) , (-1.6, -1.1),(0.2, -0.5), (-1.9, 0.8), (-2.3, 0.63)]), Polygon([(-1.65, -1.09), (-1.69, -1.38), (-0.18, -2.65), (0.52, -2.48), (0.59, -1.09), (0.26, -0.50), (0.21, -0.50), (-1.65, -1.09)])]
        >>> new_regions, streets = split_region(regions, 0.01)
        >>> new_regions[0] != regions[0]
        True
        >>> new_regions[1] != regions[1]
        True
        >>> inter = regions[0].intersection(regions[1])
        >>> inter_d = inter.buffer(0.01, cap_style=3, join_style=3)
        >>> streets[0] == inter_d
        True
    '''
    routes = None
    new_regions = []
    for i in range(len(regions)):
        poly = regions[i]
        for j in range(len(regions)):
            if (i != j and regions[i].distance(regions[j]) == 0):
                inter = regions[i].intersection(regions[j])
                inter_d = inter.buffer(road_size, cap_style=3, join_style=3)
                if isinstance(inter_d, MultiPolygon):
                    for p in inter_d:
                        poly = poly.difference(p)
                        res = Polygon(p)
                        if routes == None:
                            routes = res
                        else:
                            routes = routes.union(res)
                else:
                    poly = poly.difference(inter_d)
                    res = Polygon(inter_d)
                    if routes == None:
                        routes = res
                    else:
                        routes = routes.union(res)
        if isinstance(poly, MultiPolygon):
            for p in poly:
                new_regions.append(p)
        else:
            new_regions.append(poly)
    streets = [routes]
    if isinstance(routes, MultiPolygon):
        streets = list(routes)
    return new_regions, streets



def sort_area(buildings, walls):
    '''
    Trie une liste de batiments en fonction de leur distance par rapport au centre de la ville.

    Args:
        buildings: List - liste de Polygon représentant des buildings
        walls: Polygon - Le Polygon correspondant au murs qui va nous donner le centre de la ville
    Returns:
        buildings: List - La liste de buildings triée par rapport au centre de la ville
    Tests:
        >>> walls = Polygon([(0,0), (10,0), (10,10), (0,10)])
        >>> p1 = Polygon([(0,0), (1,0), (1,1), (0,1)])
        >>> p2 = Polygon([(4,4), (4,5), (5,4), (5,5)])
        >>> buildings = [p1, p2]
        >>> res = sort_area(buildings, walls)
        >>> res[0] == p2
        True
    '''
    center = walls.centroid
    for i in range(len(buildings)):
        for j in range(len(buildings) - 1):
            dist_j = buildings[j].distance(center)
            dist_jp = buildings[j + 1].distance(center)

            if (dist_jp < dist_j):
                buildings[j], buildings[j+1] = buildings[j+1], buildings[j]

    return buildings

def build_map(district, map_elements, city_elements, nb_houses):
	'''
	Assigne un type de batiments/zones a toutes les zones de la carte.

	Args:
		district: List - liste des districts dans la ville
		map_elements: List - liste des éléments dans toute la ville
		city_elements: List - liste des éléments dans le centre-ville
		nb_houses: Int - Le nombre de maison nécessaire dans la ville
	Returns:
		district - Les district de la ville, update avec leurs batiments.  
	'''
	for d in district:
		district_buildings = []
		for b in city_elements:
			if isinstance(b, Polygon) and d._polygon.contains(b.centroid):
				district_buildings.append(b)
		for h in district_buildings:
			if isinstance(h, Polygon):
				rand = random.randint(0, 100)
				if rand > 97:
					d._sub_areas.append(Fort(h))
				elif rand > 95:
					d._sub_areas.append(Townhall(h))
				elif rand > 90:
					d._sub_areas.append(University(h))
				elif rand > 85:
					d._sub_areas.append(Monastry(h))
				elif rand > 83:
					d._sub_areas.append(Cathedral(h))
				elif rand > 80:
					d._sub_areas.append(Market(h))
				elif rand > 75:
					d._sub_areas.append(Park(h))
				elif rand > 70:
					d._sub_areas.append(Church(h))
				else:
					house = None
					if rand > 65:
						house = Mansion(h)
					else:
						house = House(h)
					d._sub_areas.append(house)
					interior_coords = []
					for interior in house._polygon.interiors:
						interior_coords += interior.coords[:]
					d._sub_areas.append(Garden(Polygon(interior_coords)))
					
	if len(map_elements) > nb_houses:
		to_not_split_buildings = map_elements[nb_houses:]

		for d in district:
			for f in to_not_split_buildings:
				if isinstance(f, Polygon) and d._polygon.contains(f.centroid):
					rand = random.randint(0, 50)
					if rand > 48:
						d._sub_areas.append(Farm(f))
					elif rand > 45:
						d._sub_areas.append(Lake(f))
					elif rand > 40:
						d._sub_areas.append(Forest(f))
					elif rand > 30:
						d._sub_areas.append(Land(f))
					else:
						d._sub_areas.append(Field(f))
	return district