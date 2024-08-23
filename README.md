# Ball Simulation with Pygame

This project is a simple ball simulation created using the Pygame library in Python. The simulation features balls that are created on mouse clicks, and they move around the screen with physics-based behaviors like gravity and collision detection. The simulation runs until the user closes the window.

## Features

- **Ball Creation**: Balls are created at the mouse's current position when the user clicks on the screen.
- **Gravity**: The balls are affected by gravity, which can either pull them towards the bottom of the screen or towards the center line, depending on the mode.
- **Collision Detection**: The balls collide with the edges of the screen and bounce off, losing a bit of energy each time they collide.
- **Ball Expiry**: Each ball has a lifespan of 15 seconds, after which it disappears from the screen.
- **Frame Rate Display**: The script displays the current frames per second (FPS) in the terminal to help monitor performance.
- **Visual Elements**: A circle border is drawn in the center of the screen, and a line divides the screen horizontally in the middle.

## Installation

To run this script, you'll need Python installed on your machine along with the Pygame library. If you don't have Pygame installed, you can install it using pip:

```bash
pip install pygame
