import map
import tools

from area import Area, Category
from shapely.geometry import MultiPolygon, Polygon

from city_areas.district import District
from city_areas.street import Street
from city_areas.wall import Wall

from downtown.castle import Castle

class City(Area):

    def __init__(self, population, density=10000, has_walls=False, has_castle=False, has_river=False):
        super().__init__(None, Category.COMPOSITE, sub_areas=[])
        self.population = population
        # 10 000 ha/km2 par défaut mais peut baisser a 2000 ha/km2 avec les champs et monter a 30000 ha/km2
        self.density = density
        self.has_walls = has_walls
        self.has_castle = has_castle
        self.has_river = has_river
        self.district = []

        nb_people_by_districts = 8 + (density // 5000)
        nb_regions = 4 + (population // 5000)

        # Génere la carte et les Polygon représentant les districts
        regions = map.generate_regions(nb_regions)

        # Ajoute les murs si nécessaire
        walls = MultiPolygon(regions).buffer(0.05, join_style=2)
        if self.has_walls:
            self._sub_areas.append(Wall(walls))

        # Découpe la carte en différents district séparé par une route
        new_regions, streets = map.split_region(regions, 0.05)
        sorted_regions = map.sort_area(new_regions, walls)
        self.district += [District(r, []) for r in sorted_regions]
        self._sub_areas += [Street(s) for s in streets]

        # Crée des zones dans chaque district
        map_elements = []
        for d in self.district:
            buildings = map.generate_buildings(
                nb_people_by_districts, d.polygon)
            map_elements += buildings

        map.sort_area(map_elements, walls)
        nb_houses = population // 40

        city_elements = map_elements[:nb_houses]
        city_elements, _ = map.split_region(city_elements, 0.015)

        # Ajoute le chateau si nécessaire
        if has_castle:
            castle = city_elements[0]
            for i in range(1, len(city_elements) // 10):
                if (isinstance(city_elements[i], Polygon) and castle.area < city_elements[i].area):
                    castle = city_elements[i]
            city_elements.remove(castle)

            for d in self.district:
                if d._polygon.contains(castle.centroid):
                    d._sub_areas.append(Castle(castle))

        # Assigne les batiments aux zones de la carte
        self.district = map.build_map(self.district, map_elements, city_elements, nb_houses)
        self._sub_areas += self.district


if __name__ == "__main__":
    city = City(30000, has_castle=True)
    tools.json(city, './tests/generated_city/big_city_castle.json')
