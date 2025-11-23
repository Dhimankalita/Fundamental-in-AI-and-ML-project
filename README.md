● Car Racing Game

● Overview:This code implements a simple 2D car racing game using Pygame. The game window is set up with a fixed size and a title. It defines colors, lanes, and road measurements to render the racing track and lane markers.
Player and enemy vehicles are represented as sprite classes, with images scaled and positioned appropriately. The player can move the car within defined lane boundaries using arrow keys.
Enemy vehicles spawn randomly in lanes, moving downward continuously with their speed increasing as the player’s score increases. Collision detection ends the game when the player hits an enemy car, showing a crash image and offering a replay or quit option.
The main game loop handles event processing, game state updates, rendering, and frame rate control to ensure smooth gameplay. Overall, the code demonstrates core game programming concepts such as sprite management, event-driven input handling, collision detection, and dynamic difficulty scaling within a modular design pattern supported by Pygame.​

● Features:The main features of this Pygame car racing game code include:
Custom game window setup with fixed dimensions and title display.
Defined road dimensions, lane positions, and color constants for drawing the gaming environment.
Player and enemy vehicles are implemented as Pygame sprites with image scaling and positioning encapsulated in classes for modularity.
Grouping of player and enemy sprites enables efficient rendering and collision detection.
Keyboard input handling for player car movement with explicit boundary checks ensures the player stays within lanes and screen limits.
Dynamic spawning of enemy vehicles in random lanes while preventing overcrowding and overlap.
Enemy vehicles move downwards at a current speed that increases progressively as the player’s score increases, adding difficulty.
Continuous score tracking displayed on screen, increasing when enemy vehicles move off-screen.
Collision detection that switches the game state to "game over" and shows a crash image along with a prompt to replay or exit.
Game loop managing input events, game state updates, rendering, and frame rate control to maintain smooth gameplay at 120 FPS.

● Technologies/tools used:The technologies and tools used in this code are:
Python: The programming language used for the entire project.
Pygame Library: A Python library for video game development that provides functionality for creating game windows, handling sprite objects, processing user input (keyboard), drawing graphics, managing game loops, collision detection, and timing control.
Pygame Sprites: Utilized to represent player and enemy vehicles as objects with properties like image, position, and collision bounds.
Pygame's Event Handling: To capture keyboard events and window events like closing the game.
Pygame's Drawing Functions: For rendering the game background, roads, lane markings, and other graphical elements.
Image File Assets: External PNG image files for player car, enemy vehicles, and crash images, loaded into Pygame.
Game Loop Control: Using pygame.time.Clock() to maintain a consistent frame rate of 120 FPS.

● Steps to install & run the project:Steps to install and run the Pygame car racing game project:
Install Python:
Ensure Python 3.x is installed on your system from https://www.python.org/downloads/.
Verify installation via python --version or python3 --version in the terminal.
Install Pygame Library:
Open your command prompt or terminal.
Run the command:
bash
pip install pygame
This installs the Pygame library needed to run the game code.
Prepare Game Assets:
Ensure the image files referenced in the code (car.png, pickup_truck.png, semi_trailer.png, taxi.png, van.png, crash.png) are downloaded or available in the same directory as the Python script.
Save the Code:
Copy the provided game code into a file with a .py extension, e.g., car_racing_game.py.
Run the Game:
In the command prompt or terminal, navigate to the folder containing the script and assets.
Run the game using:
bash
python car_racing_game.py
or if multiple Python versions exist on your system:
bash
python3 car_racing_game.py
Play the Game:
Use arrow keys to move the player car.
Avoid enemy vehicles to score points.
On collision, the game pauses and prompts to play again or quit.

● Instructions for testing:Instructions for testing this Pygame car racing game code:
Initialization Test:
Run the game to verify the Pygame window opens correctly with the specified title "My Fast Car Game" and size 500x500 pixels.
User Input and Boundaries:
Use arrow keys (left, right, up, down) to move the player car.
Confirm that the player car moves only within the defined lane boundaries and does not go outside the screen.
Enemy Vehicle Spawning:
Observe enemy vehicles spawning randomly in one of the defined lanes, with no more than 3 enemies at a time.
Enemy Movement and Speed Scaling:
Ensure enemy vehicles move continuously downward and disappear when off-screen.
Verify the game speed increases every 5 points scored by the player.
Scoring System:
Confirm the score increments each time an enemy vehicle passes beyond the bottom of the screen.
Check that the score is displayed correctly in the top-right corner.
Collision Detection:
Drive the player car into an enemy vehicle and verify the collision is detected, triggering the game over screen with crash image and replay prompt.
Game Over and Restart:
On game over, press 'Y' to restart the game and confirm all variables reset and gameplay restarts.
Press 'N' to quit the game and ensure the window closes properly.
Performance Check:
Play the game over extended periods and check for smooth frame rates and responsiveness without crashes or lag.

● Screenshots (optional but recommended):
Code:<img width="1172" height="938" alt="image" src="https://github.com/user-attachments/assets/eacc7382-9379-430c-8aca-721fff561bb9" />
<img width="1287" height="911" alt="image" src="https://github.com/user-attachments/assets/fb8f2126-1116-4767-9451-97e13003be43" />
<img width="1587" height="942" alt="image" src="https://github.com/user-attachments/assets/5440dc61-6602-4448-abc3-f9dfdbb1e0b1" />
<img width="1572" height="937" alt="image" src="https://github.com/user-attachments/assets/4c4ffa3d-ec57-400b-8551-eaad744a489f" />
<img width="1753" height="902" alt="image" src="https://github.com/user-attachments/assets/134698eb-134e-49d0-8aad-c927a3d657a2" />
<img width="1443" height="915" alt="image" src="https://github.com/user-attachments/assets/b11fa6ea-2273-40cf-a565-b472ce9fe150" />
<img width="1317" height="951" alt="image" src="https://github.com/user-attachments/assets/007ed683-06d6-499b-a665-54366e995447" />
<img width="1435" height="933" alt="image" src="https://github.com/user-attachments/assets/76e348ea-bdd9-45a2-977a-510ea686d8b8" />
<img width="1268" height="607" alt="image" src="https://github.com/user-attachments/assets/94446a0f-40a2-4667-b562-c1f58105223c" />

Output:<img width="620" height="661" alt="image" src="https://github.com/user-attachments/assets/e931b2c7-800e-432e-9692-5311b4a96431" />









