# EXAM2
Fredrik, Lucas och Carl
# Dice Pig Game

## Get Going

The following will be instructions on how to install, run and test our pig game.

- Make sure you have the latest python version.
- Install make. If you are using gitbash on Windows, then download the chocolatey package manager from https://chocolatey.org/install.
- Clone our repository containing the project: git clone https://github.com/Hiimfred/EXAM2.git.
- The next step is to create a virtual environment. Navigate to our repository EXAM2 in your gitbash terminal and then use the make venv command to create a new virtual environment.
- Activate the environment on Windows: source .venv/Scripts/activate
- Activate the environment on Linux/Mac: source .venv/bin/activate
- Then use the make install command to download all the necessary plugins.
- Now you can run the game with the command: python pig_game/main.py.

## Run the Validators

While still in the EXAM2 directory, you can run the validators by entering these make commands: execute them one by one with make flake8/ make pylint. Optionally, you can run them all at the same time with make lint.

## Run the Unittests

You can run the unittests without coverage using: make unittest.

Or you can run the unittests with coverage using: make coverage.

And you can run both linters and unittests with: make test.

If you install Graphviz (through Chocolatey using PowerShell on Windows) with the choco install graphviz command or with the brew package manager on macOS using the brew install graphviz command. Then you should be able to use the make pdoc command to produce documentation for the project and make pyreverse to produce UML diagrams.
