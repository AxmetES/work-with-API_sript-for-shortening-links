## Script for working with API Bite.ly

Project for shortening links and calculating the amount of clicks

## Getting Started

For the project to work, install all necessary packages 

```python
pip install -r requirements.txt
```
Register and get the TOKEN from the site https://dev.bitly.com/index.html

```python
TOKEN_BITLY='your token'
```
you extract it in the code with package import os

#### in module bit_ly.py

```python
import os

TOKEN = os.getenv('TOKEN')
headers = {"Authorization": f"Bearer {TOKEN}"}
```

## Motivation

The project is an assignment in online courses [Devman](https://dvmn.org/modules/)

## Running

The script is run from the command line
```python
python bit_ly.py (your link)
```

## License

You may copy, distribute and modify the software
