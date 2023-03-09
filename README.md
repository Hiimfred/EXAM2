# Dice Pig Game

## Rules
Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold":

If the player rolls a 1, they score nothing and it becomes the next player's turn.
If the player rolls any other number, it is added to their turn total and the player's turn continues.
If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
The first player to score 100 or more points wins.

For example, the first player, Donald, begins a turn with a roll of 5. Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1, and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-6, after which she chooses to hold, and adds her turn total of 23 points to her score.

Rules from wiki: https://en.wikipedia.org/wiki/Pig_(dice_game)


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
5. Activate the environment: 
```
# On windows
. .venv/Scripts/activate

# On Linux/mac:
. .venv/bin/activate
```
6. Use the following command to download all necessary plugins: 
```
make install
```
7. Run the game with the command: 
```
python pig_game/main.py
```

## Game commands!
#### Type <help> if you want to display available commands:
Starts a single player game with command:
```
# Enter one player name after typing solo
solo <player name>
```
Starts a Multiplayer game with command:
```
# Enter two player names after typing multiplayer
multiplayer <player name 1> <player name 2>
```
Change difficulty with the command:
```
# Switch between Easy and Hard difficulty
change_difficulty
```
Roll the dice with the command:
```
# Rolls the dice. If player rolls one, pass turn
roll
```
Hold your turn with the command:
```
# Hold to keep your accumulated score
hold
```
If you want to be cheaky.. you can cheat with the command:
```
# Player score set to 99.. cheater..
cheat
```
You can change color on your name with the command:
```
# Player can choose between red, blue, green, yellow, magenta, cyan
color <enter the color>
```
If you want to reset and continue with same player(s):
```
# Continue with same player in a new round of pig game
continue
```
To check the leaderboard:
```
# Display a leaderboard with player names and number of wins
highscore
```
Exit the game with the command:
```
# Stores the score and exit the game
quit
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