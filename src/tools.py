from shapely.geometry import mapping
from shapely.geometry import mapping, MultiPolygon
import fiona

SCHEMA = {
    'geometry': 'Polygon',
    'properties': {'category': 'int'},
}


def json(what, filename):
    with fiona.open(filename, 'w', 'GeoJSON', SCHEMA) as c:
        districts = what.components()
        for d in districts:
            if type(d._polygon) == MultiPolygon:
                for p in d._polygon:
                    c.write({
                        'geometry': mapping(p),
                        'properties': {'category': d._category.value},
                    })
            else:
                c.write({
                    'geometry': mapping(d._polygon),
                    'properties': {'category': d._category.value},
                })
            for b in d.components():
                if type(b._polygon) == MultiPolygon:
                    for p in b._polygon:
                        c.write({
                            'geometry': mapping(p),
                            'properties': {'category': b._category.value},
                        })
                else:
                    c.write({
                        'geometry': mapping(b._polygon),
                        'properties': {'category': b._category.value},
                    })
            
