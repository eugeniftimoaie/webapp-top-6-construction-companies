# Webapp Top 6 Construction Companies
Webapp with Analysis of Trends and Growths of the 6 largest European Construction Companies between the years 2007 and 2019.

The webapp is available on the web under following url: https://top-construction-companies.herokuapp.com/

## Configuration
* HTML, CSS, Javascript
* Python 3 with libraries bootstrap + plotly (Front-end) and flask (Back-end)

## Installation on local computer
This webapp can be opened on local windows computer with following terminal commands:
* change directory to folder with top6_app.py
```bash
$ cd ...path.../web_app
```
* start web app with following command
```bash
$ python top6_app.py
```
* open browser and type in following url: http://localhost:5000/

## File Manifest
folder **data** containing:
* **construction_top_6_europe_2020.csv** - csv file with cleaned data of companies

folder **top6_app** containing:
* folder **static** containing img files for social media buttons
* folder **template** containing **index.html** with content of webpage
* **__init__.py** - python file to execute webapp when loading the module
* **routes.py** - python file to connect back-end with front-end content

folder **wrangling_scripts** containing:
* **wrangle_data.py** - python file for wrangling and compiling data into graphs of the webapp

**LICENSE.md** - markdown file with license.md for this software package

**README.md** - markdown file with instructions how to install and use this python package

## Copyright and Licencing
This project is licensed under the terms of the MIT license

## Contact
Author: Eugen Iftimoaie

For questions feel free to contact me on my e-mail adress: eugen.iftimoaie@gmx.de
