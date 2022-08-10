# Map-Generation [![Profile][title-img]][profile]

[title-img]:https://img.shields.io/badge/-LAVS-blue
[profile]:https://github.com/LAVS-TM

This goal of this project was to create a **medieval city generator** with python and several constraints. The repository is composed of the **source code**, the **documentation** and the **tests folder**.

### Usage

To configure the city generation, you need to open `city.py` in the `src` folder and modify the values assigned to the City object. The **City** class is of the form:

```python
City(population, density, has_walls=False, has_castle=False, has_river=False)
```

You can also change the path where the **generated city** will be saved. To do this, modify the character string passed as arguments to `tools.json`. This path will be important to be able to launch the visualization afterwards.

---
The **default path** used by the visualization is `/generated_city/city.json`

---

Here is an example of a possible **configuration** for the city to be generated:

```python
city = City(10000, 10000, has_walls=True, has_castle=True)
tools.json(city, '/generated_city/city.json')
```

To start the generation:

```python
python3 src/city.py
```

To visualize the generation:

```python
python3 src/viewer.py *file_path*
```

---
The above commands must be run from the **project database**. Otherwise you have to modify the path to the `.py` files.

---

Here is an example of a **city** generated with the parameters presented previously:

<img src="https://github.com/LAVS-TM/Map-Generation/blob/main/doc/CityExample.png" alt="Example city">

## Documentation

The full **documentation** of the project and the **technical implementation** are available in the repository in `/doc/_build/html/index.html`.

## Specifications

This project was carried out in Python, using the following libraries:

* attrs==21.2.0
* certifi==2021.5.30
* click==8.0.1
* click-plugins==1.1.1
* cligj==0.7.2
* cycler==0.10.0
* Fiona==1.8.20
* geopandas==0.9.0
* iniconfig==1.1.1
* kiwisolver==1.3.1
* matplotlib==3.4.2
* munch==2.5.0
* numpy==1.21.1
* packaging==21.0
* pandas==1.2.5
* Pillow==8.3.0
* pluggy==0.13.1
* py==1.10.0
* pyparsing==2.4.7
* pyproj==3.1.0
* PyQt5==5.15.4
* PyQt5-Qt5==5.15.2
* PyQt5-sip==12.9.0
* pytest==6.2.4
* python-dateutil==2.8.1
* pytz==2021.1
* scipy==1.7.0
* Shapely==1.7.1
* six==1.16.0
* toml==0.10.2
* userprovided==0.9.1