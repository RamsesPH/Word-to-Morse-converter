# MorseCode

A simple Python project to encode text into Morse code, with tests powered by `pytest`.

## Features

- Encode letters A–Z and digits 0–9 into Morse code
- Word separation using `///`
- Unknown characters encoded as `/?`
- Fully tested with `pytest`

## Project structure

```text
MorseCode/
├── src/
│   ├── __init__.py
│   ├── morse.py
│   └── main.py
├── tests/
│   └── test_morse.py
├── pytest.ini
├── README.md
└── LICENSE


## Installation

git clone <your-repo-url>.git
cd MorseCode
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt  # if you create one

## Running Tests
from root run 

pytest

## Usage 
( run from main.py )
