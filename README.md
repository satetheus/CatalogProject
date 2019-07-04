# CatalogProject [![Build Status](https://travis-ci.org/satetheus/CatalogProject.svg?branch=master)](https://travis-ci.org/satetheus/CatalogProject)

A flask project creating a web-based catalog.

## Dependancies
If you have python 3 already installed, the following dependencies can all be installed with the following command (skip this step if you are installing the vagrant VM):
```bash
python3 -m pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```
| Dependency    | Supported Version |
| :--------:    | :---------------: |
| python        | 3.5, 3.6, 3.7     |
|chardet        | 2.3.0             |
|Click          | 7.0               |
|Flask          | 1.0.3             |
|Flask-HTTPAuth | 3.3.0             |
|httplib2       | 0.12.3            |
|itsdangerous   | 1.1.0             |
|Jinja2         | 2.10.1            |
|MarkupSafe     | 1.1.1             |
|oauth2client   | 4.1.3             |
|packaging      | 19.0              |
|passlib        | 1.7.1             |
|pyasn1         | 0.4.5             |
|pyasn1-modules | 0.2.5             |
|pyparsing      | 2.4.0             |
|requests       | 2.20.0            |
|rsa            | 4.0               |
|six            | 1.10.0            |
|SQLAlchemy     | 1.3.3             |
|urllib3        | 1.24.2            |
|Werkzeug       | 0.15.4            |

## Setup
### Vagrant Setup
The vagrantfile is included in this repository, so if you have vagrant installed, use the following command from the repo directory to setup, & connect to the VM:
```bash
vagrant up && vagrant ssh
```
### Database Setup
To Setup the database with a starting set of data, run the following command in the repo directory:
```bash
python addgames.py
```
### Starting the server
To start the server, run the following command in the repo directory:
```bash
python __init__.py
```
## Sources
@shyamgupta:
-  [post-google+ shutdown oauth flow](https://gist.github.com/shyamgupta/d8ba035403e8165510585b805cf64ee6)

@udacity:
- Some backend oauth pulled from lines in [this file](https://github.com/udacity/ud330/blob/master/Lesson4/step2/project.py)
