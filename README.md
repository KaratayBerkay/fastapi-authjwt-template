## Project Mapping and Structure
* Create Virtual Environment:
```bash
virtualenv venv
```
* Windows OR Linux Activate Virtual Environment:
```bash
.\venv\Scripts\activate.bat
source venv\bin\activate
```
then clear prompt line :)
```bash
clear
```
* Upgrade your pip before install requirements (Recommended):

```bash
pip3 install --upgrade pip3
pip install --upgrade pip
```
* OR / install requirements /w Windows OR /w Linux::

```bash
pip install -r wrequirements.txt --upgrade
pip install -r lrequirements.txt --upgrade
pip3 install -r wrequirements.txt --upgrade
pip3 install -r lrequirements.txt --upgrade
```
---
* Run uvicorn at local
```bash
uvicorn app:app_run --host 127.0.0.1 --port 5001 --reload
uvicorn app:app_run --host 0.0.0.0 --port 5001 --reload
```
---
# Project Details
