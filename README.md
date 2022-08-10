# Map-Generation [![Profile][title-img]][profile]

[title-img]:https://img.shields.io/badge/-LAVS-blue
[profile]:https://github.com/LAVS-TM

This is the repository for a python chess engine with an **Q-Learning** IA. The goal was to have fun with artificial intelligence and to step up our knowledge on **reinforcement learning** !


## Chess Engine

The Chess Engine is available in the file `board.py`. It is a really simple engine that let us play chess game.

There is two different way to launch a game.

### CLI Game

To launch the CLI chess game, you need to run :

```python
python main.py
```

A **CLI** interface will let you moove your pieces with some input.

<img src="https://github.com/Bictole/ChessAI/blob/master/readme_images/cli.png" alt="CLI">

### Pygame Interface

To launch the pygame chess game, you need to run :

```python
python display.py
```

**Pygame** with a real chess interface will let you moove your pieces with your mouse.

<img src="https://github.com/Bictole/ChessAI/blob/master/readme_images/pygame.png" alt="Pygame">


## IA

The IA here is a **Q-Learning** Algorithm made with python. The proof of concept is in the file `main_AI.py`.


### Usage

A small reference chess game with the demonstration of the AI is available.
You just need to run :

```python
python displayIA.py
```