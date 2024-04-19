# BetWatch Parser

## About parser

This Parser uses for getting information from BetWatch<br>
This parser has writen with python<br>
You can get information about pre matches and live matches<br>
The matches information can be got with filters<br>

## How to use this parser
Firstly you must to download this project to your project<br>
Download necessary packages with command
```shell
pip install -r requirements.txt
```

After that you need to import parser.py in your project
```python
from parser import BetWatchParser
```

then you have to create the parser object with filters <br>
but you can change the filters while the program is working

you can send filters with params
```python
parser = BetWatchParser('filters')
```

param pre_matches: bool, default False use for pre matches<br>
param live_matches: bool, default False use for live matches<br>
param from_price: start price<br>
param to_price: end price<br>
param from_percentage: start percentage<br>
param to_percentage: end percentage<br>
param from_coefficient: start coefficient<br>
param to_coefficient: end coefficient<br>
param from_time_1: start time 1<br>
param to_time_1: end time 1<br>
param from_time_2: start time 2<br>
param to_time_2: end time 2<br>
param block_list: block list for filters<br>

if you want to get matches, you will write this
```python
parser.get_matches('filters')
```
but you can write the filters to get_matches with params<br>

all of the matches is kept in ```parser.matches```<br>
this is a dict with name and id matches


