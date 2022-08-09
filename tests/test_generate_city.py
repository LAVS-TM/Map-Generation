
import sys
sys.path.insert(0, '../src')

import pytest
import tools
from city import City

# Basic Generation Tests

def test_small_city():
	city = City(2000)
	tools.json(city, './generated_city/small_city.json')

def test_medium_city():
	city = City(10000)
	tools.json(city, './generated_city/medium_city.json')

def test_big_city():
	city = City(30000)
	tools.json(city, './generated_city/big_city.json')

def test_small_city_small_density():
	city = City(2000, 2000)
	tools.json(city, './generated_city/small_city_small_density.json')

def test_small_city_big_density():
	city = City(2000, 30000)
	tools.json(city, './generated_city/small_city_big_density.json')

def test_big_city_small_density():
	city = City(30000, 2000)
	tools.json(city, './generated_city/big_city_small_density.json')

def test_big_city_big_density():
	city = City(30000, 30000)
	tools.json(city, './generated_city/big_city_big_density.json')
    
def test_medium_city_small_density():
	city = City(10000, 2000)
	tools.json(city, './generated_city/medium_city_small_density.json')

def test_medium_city_big_density():
	city = City(10000, 30000)
	tools.json(city, './generated_city/medium_city_big_density.json')


# Option Test :

# Wall

def test_small_city_wall():
	city = City(2000, has_walls=True)
	tools.json(city, './generated_city/small_city_wall.json')

def test_medium_city_wall():
	city = City(10000, has_walls=True)
	tools.json(city, './generated_city/medium_city_wall.json')

def test_big_city_wall():
	city = City(30000, has_walls=True)
	tools.json(city, './generated_city/big_city_wall.json')


# Castle

def test_small_city_castle():
	city = City(2000, has_castle=True)
	tools.json(city, './generated_city/small_city_castle.json')

def test_medium_city_castle():
	city = City(10000, has_castle=True)
	tools.json(city, './generated_city/medium_city_castle.json')

def test_big_city_castle():
	city = City(30000, has_castle=True)
	tools.json(city, './generated_city/big_city_castle.json')
    

# Wall & Castle

def test_small_city_wall_castle():
	city = City(2000, has_walls=True, has_castle=True)
	tools.json(city, './generated_city/small_city_wall_castle.json')

def test_medium_city_castle():
	city = City(10000, has_walls=True, has_castle=True)
	tools.json(city, './generated_city/medium_city_wall_castle.json')

def test_big_city_castle():
	city = City(30000, has_walls=True, has_castle=True)
	tools.json(city, './generated_city/big_city_wall_castle.json')