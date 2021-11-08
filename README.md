# RPS: Rock Paper Scissors Game

Rock- Paper- Scissors is a game for two players. Each player simultaneously opens his/her hand to
display a symbol:

• Fist equals rock

• Open hand equals paper

• Showing the index and middle finger equals scissors.

The winner is determined by the following schema:

• paper beats (wraps) rock

• rock beats (blunts) scissors

• scissors beats (cuts) paper.

-------------------------------------------
The project requires Python3.9
------------------------------------------

## Installation
cd into the project directory
```bash
cd rps
```
Create a virtual environment by running the command below
```bash
py -3.9 -m venv --clear env
```
Activate the environment by running
```bash
'env\scripts\activate' or 'source env/bin/activate' (for Mac or Linux)
```
rps uses poetry as the dependency management system. Please install poetry first by running the command below
```bash
pip install poetry
```
To install the defined dependencies for the project, just run the poetry install command
```bash
poetry install
```
To run the code use the poetry run command
```bash
python rps/rps.py
```
The unit tests, formatting checks using black and coding style checks using flake8 can be executed by running tox using the command below
```bash
tox
```