# MovieLibraryScrapper
Python web Scrapper to get Infos from movie(s) file(s)

## Requirements
```bash
pip install imdbpy
pip install requests
pip install bs4
```
## Used library
```python
import os  
import sys
import requests
from bs4 import BeautifulSoup
from imdb import IMDb
import random
import string
import shutil
import json
```
## How to use ? 

```bash
    python MovieScrapper.py <directory path>
```

## How it works ?

Once you specify the *directory* where you want to scan movies, it will scan the directory content.
For *each file* in the directory, it will send HTTP request at http://www.imdb.com to retrieve movie *imdb ID* (which is required to request imdb API)

The script **parse the HTML code** to retrieve imdb ID which is associated with the actual movie.
One the ID is retrieve, it is easy to request *IMDB API*.

If every required field are present in API response, I store the data inside a tmp folder (each movie data is in a specific file)

Then I scan the tmp folder, and for each movie data file I parse it and generate a JSON file in another tmp folder wich represent movie data.

Finaly for each JSON file in this new tmp folder, I concat all of them to make a final JSON with all movie data from my scanned directory !

## Misc

Sometimes (and especially for movie saga) IMDB search engine can mismatch result, so to avoid double objects in JSON file (wich is not valid for **RFC 8259**) I use json library.


## Example

### Movie directory content

```bash
    tree <directory path>
```
```bash
.
├── Exam.avi
├── Haunter.mkv
├── The Shape of Water.avi
├── Gone.avi
└── Life.avi

0 directories, 5 files
```

### Running script

```bash
    python MovieScrapper.py <directory path>
```

### JSON output


```json
    {
    "Exam": {
        "name": "Exam",
        "year": "2009",
        "url": "https://m.media-amazon.com/images/M/MV5BNDg2NzM2NzIwNF5BMl5BanBnXkFtZTcwODE2ODc1Mg@@._V1_SY150_CR0,0,101,150_.jpg",
        "bigurl": "https://m.media-amazon.com/images/M/MV5BNDg2NzM2NzIwNF5BMl5BanBnXkFtZTcwODE2ODc1Mg@@.jpg",
        "kind": "movie",
        "genre": [
            "Mystery",
            "Thriller"
        ],
        "rating": "6.8",
        "director": [
            "Stuart Hazeldine"
        ],
        "writer": [
            "Stuart Hazeldine",
            "Simon Garrity",
            "Stuart Hazeldine"
        ],
        "cast": [
            "Adar Beck",
            "Gemma Chan",
            "Nathalie Cox",
            "John Lloyd Fillingham",
            "Chukwudi Iwuji",
            "Pollyanna McIntosh",
            "Luke Mably",
            "Jimi Mistry",
            "Colin Salmon",
            "Chris Carey"
        ]
    },
    "A Quiet Place": {
        "name": "A Quiet Place",
        "year": "2018",
        "url": "https://m.media-amazon.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_SY150_CR0,0,101,150_.jpg",
        "bigurl": "https://m.media-amazon.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@.jpg",
        "kind": "movie",
        "genre": [
            "Drama",
            "Horror",
            "Sci-Fi"
        ],
        "rating": "7.5",
        "director": [
            "John Krasinski"
        ],
        "writer": [
            "Bryan Woods",
            "Scott Beck",
            "John Krasinski"
        ],
        "cast": [
            "Emily Blunt",
            "John Krasinski",
            "Millicent Simmonds",
            "Noah Jupe",
            "Cade Woodward",
            "Leon Russom",
            "Rhoda Pell"
        ]
    },
    "Haunter": {
        "name": "Haunter",
        "year": "2013",
        "url": "https://m.media-amazon.com/images/M/MV5BMjEwNDc1MTI3Ml5BMl5BanBnXkFtZTgwNjI5ODU0MDE@._V1_SY150_CR0,0,101,150_.jpg",
        "bigurl": "https://m.media-amazon.com/images/M/MV5BMjEwNDc1MTI3Ml5BMl5BanBnXkFtZTgwNjI5ODU0MDE@.jpg",
        "kind": "movie",
        "genre": [
            "Fantasy",
            "Horror",
            "Mystery",
            "Thriller"
        ],
        "rating": "5.9",
        "director": [
            "Vincenzo Natali"
        ],
        "writer": [
            "Brian King"
        ],
        "cast": [
            "Abigail Breslin",
            "Peter Outerbridge",
            "Michelle Nolden",
            "Stephen McHattie",
            "Peter DaCunha",
            "Samantha Weinstein",
            "Eleanor Zichy",
            "David Hewlett",
            "Sarah Manninen",
            "Martine Campbell",
            "David Knoll",
            "Michelle Coburn",
            "Tadhg McMahon",
            "Marie Dame"
        ]
    },
    "Life": {
        "name": "Life",
        "year": "2017",
        "url": "https://m.media-amazon.com/images/M/MV5BMzAwMmQxNTctYjVmYi00MDdlLWEzMWUtOTE5NTRiNDhhNjI2L2ltYWdlXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_SY150_CR0,0,101,150_.jpg",
        "bigurl": "https://m.media-amazon.com/images/M/MV5BMzAwMmQxNTctYjVmYi00MDdlLWEzMWUtOTE5NTRiNDhhNjI2L2ltYWdlXkEyXkFqcGdeQXVyMTkxNjUyNQ@@.jpg",
        "kind": "movie",
        "genre": [
            "Horror",
            "Sci-Fi",
            "Thriller"
        ],
        "rating": "6.6",
        "director": [
            "Daniel Espinosa"
        ],
        "writer": [
            "Rhett Reese",
            "Paul Wernick"
        ],
        "cast": [
            "Hiroyuki Sanada",
            "Ryan Reynolds",
            "Rebecca Ferguson",
            "Jake Gyllenhaal",
            "Olga Dykhovichnaya",
            "Ariyon Bakare",
            "Jesus Del Orden",
            "Allen McLean",
            "Leila Grace",
            "Mari Gvelesiani",
            "David Muir",
            "Elizabeth Vargas",
            "Camiel Warren-Taylor",
            "Haruka Kuroda",
            "Naoko Mori",
            "Alexandre Nguyen",
            "Hiu Woong-Sin"
        ]
    },
    "Gone": {
        "name": "Gone",
        "year": "2011",
        "url": "https://m.media-amazon.com/images/M/MV5BNzQ5MTczNzEwNl5BMl5BanBnXkFtZTcwMzg2OTI4OQ@@._V1_SY150_CR6,0,101,150_.jpg",
        "bigurl": "https://m.media-amazon.com/images/M/MV5BNzQ5MTczNzEwNl5BMl5BanBnXkFtZTcwMzg2OTI4OQ@@.jpg",
        "kind": "tv movie",
        "genre": [
            "Crime",
            "Drama",
            "Mystery",
            "Thriller"
        ],
        "rating": "4.8",
        "director": [
            "Grant Harvey"
        ],
        "writer": [
            "Ron Oliver",
            "Jason Filiatrault"
        ],
        "cast": [
            "Molly Parker",
            "Lochlyn Munro",
            "Susan Hogan",
            "Natasha Calis",
            "Venus Terzo",
            "Adrian Holmes",
            "Sonja Bennett",
            "Peter Bryant",
            "John Shaw",
            "Kristina Agosti",
            "Andrew Airlie",
            "Jax Smith",
            "Buster Kane",
            "Lori Triolo",
            "Derek Lowe",
            "Alan Silverman",
            "Rondel Reynoldson",
            "Adam Bloch"
        ]
    }
}
```
