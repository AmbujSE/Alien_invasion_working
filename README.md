# Alien Invasion

A small Pygame-based shooter prototype. Control a ship at the bottom of the screen, move left/right and fire bullets. This repository contains the current minimal implementation (no aliens yet).

## Features
- Ship movement and rendering
- Bullet creation, movement, and cleanup
- Configurable values in a single settings class

## Controls
- Left arrow — move left
- Right arrow — move right
- Space — fire a bullet
- Q — quit the game

## Run
1. Install dependencies:
```sh
pip install pygame
python3 [alien_invasion.py](http://_vscodecontentref_/0)
Important files
alien_invasion.py — main game loop; composes Ship, Bullet, and Settings.
ship.py — defines the Ship class and rendering logic.
bullet.py — defines the Bullet class and bullet behavior.
settings.py — defines the Settings class with game constants.
images/ship.bmp — ship sprite used by the game.
Notes / TODO
Aliens and collision handling are not yet implemented.
settings.py contains the main tunable parameters (speeds, sizes, colors).
There is a small fullscreen sizing line in alien_invasion.py that assigns screen_width twice; consider verifying screen dimension