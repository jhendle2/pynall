# Lasso
Lasso, (formerly PyNaLL, or "Python's Not A Layout Language"), is a Python based 
interpreter which allows for rapid prototyping of webpages
using a Python styled markdown language. Lasso supports both
frontend development and an automatic connection to a
Python backend framework.

# Installation
```
git clone github.com/jhendle2/pynall
cd to/pynall/directory
# python setup.py install # Not used (yet??)
python main.py # To create a new project or
python main.py -i src/test1.pypg -a -o test_file # To run the test file I included
# python main.py test # To run a test project
```

# Changelog

## Version 0.0.5 (10/12/2021):

---
**MAJOR OVERHAUL!!**
* Continued work with project directory system
* Scripts handler successfully imports scripts
  * Places temporary scripts file in project directory
* Layout handler successfully builds layout tree
  * Respects function arguments as well (this was agonizing to code)
  as well as some recursive function arguments (up to one layer)
* Code now successfully outputs HTML code
  * Only open/close tags, currently. Still a WIP
  * Debug variable in `debugs.py` for enabling interim
  JSON code output --> lets you see the structure
  of your files before HTML conversion
* Code is looking handsome as ever

## Version 0.0.4 (10/11/2021):

---
* Complete refactor of code. All old code moved to v002 and v003 folders
* Built-in project setup when no file-in / file-out args are passed
  * Helpful templates added for newbies

## Version 0.0.3 (10/7/2021):

---
* Refactored a bunch of code
* Broke the HTML converter ;.(
* But, a Flask app can now succesfully import scripts
and their functions put inside a .pypg file so that's cool.

## Version 0.0.2 (10/6/2021):

---
* PyNaLL to HTML converter works
* Prototyping for CSS and Python converters added

## Version 0.0.1 (9/30/2021):

___
* Initial commit