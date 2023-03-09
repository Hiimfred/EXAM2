# Dice Pig Game

## Getting Started
The following are instructions on how to install, run, and test our pig game.

1. Make sure you have the latest version of Python.
2. Install make. If you are using gitbash on Windows, download the chocolatey package manager from https://chocolatey.org/install.
3. Clone our repository containing the project: 
```
git clone https://github.com/Hiimfred/EXAM2.git
```
4. Create a virtual environment. Navigate to our repository EXAM2 in your gitbash terminal and use the following command to create a new virtual environment: 
```
make venv
```
5. Activate the environment on Windows: 
```
. .venv/Scripts/activate
```
6. Activate the environment on Linux/Mac: 
```
. .venv/bin/activate
```
7. Use the following command to download all necessary plugins: 
```
make install
```
8. Run the game with the command: 
```
python pig_game/main.py
```

## Running the Validators
While still in the EXAM2 directory, you can run the validators by entering the following commands:
```
make flake8
make pylint
```
```
# You can run them all at the same time with 
make lint
```

## Running the Unittests
You can run the unittests without coverage using: 
```
make unittest
```
Run the unittests with coverage using: 
```
make coverage
```
Run both linters and unittests with coverage using:
```
make test
```

## Producing Documentation and UML Diagrams

To install graphviz on Windows, use the choco install graphviz command in PowerShell:
```
choco install graphviz
```
To install on macOS, use the command:
```
brew install graphviz
``` 

If you install graphviz, you should be able to use the following commands to produce documentation and UML diagrams:
```
# to produce documentation for the project
make pdoc 
```
```
# to produce UML diagrams
make pyreverse
```