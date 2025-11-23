import pygame
from pygame.locals import *
import random

pygame.init()

# --- Initial Setup with Varied Naming ---
W = 500  # Abbreviated width
H = 500  # Abbreviated height
screenSize = (W, H) # camelCase for screen size
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption('My Fast Car Game') # Different window title


# --- Color Definitions with Inconsistent Capitalization ---
GRY = (100, 100, 100) # Abbreviated
grn = (76, 208, 56)   # lower case
Red = (200, 0, 0)     # Capitalized
White = (255, 255, 255)
yell = (255, 232, 0) # lower case abbreviation


# --- Road Constants with Varied Naming & Spacing ---
roadWidth = 300
markW = 10
MARKER_HEIGHT = 50 # ALL CAPS constant


left_lane = 150 # snake_case
centerLane = 250 # camelCase
rightLane = 350
Lanes = [left_lane, centerLane, rightLane] # Capitalized list name


# --- Game Objects Rects (slightly verbose creation) ---
RoadRect = (100, 0, roadWidth, H)
leftEdge = (95, 0, markW, H)
rEdge = (395, 0, markW, H) # Abbreviated name


marker_y_offset = 0 # Different variable name for lane marker movement

# Player Initial Position
player_x_start = 250
player_y_start = 400


clk = pygame.time.Clock() # Abbreviated clock
FPS = 120 # ALL CAPS constant

# Game State
gameOver = False # camelCase
speed_current = 2 # verbose name
current_score = 0 # verbose name

# --- Class Definitions with Varied Naming and Spacing ---
class VehicleSprite(pygame.sprite.Sprite): # Modified class name
    
    def __init__(self, Img, x_pos, y_pos): # Varied parameter names
        pygame.sprite.Sprite.__init__(self)
        
        # Scale calculation with inconsistent spacing
        scaleFactor = 45 / Img.get_rect().width 
        
        # Calculation on separate lines
        newW = Img.get_rect().width * scaleFactor
        newH = Img.get_rect().height * scaleFactor
        
        self.image = pygame.transform.scale(Img, (newW, newH))
        
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
        
class PlayerCar(VehicleSprite): # Modified class name
    
    def __init__(self, x_start, y_start): # Varied parameter names
        player_img = pygame.image.load('car.png')
        # Use super().__init__ with slightly different parameter order for effect
        super().__init__(player_img, x_start, y_start) 
        

# --- Group and Image Loading ---
player_car_group = pygame.sprite.Group() # More verbose group name
enemy_vehicles = pygame.sprite.Group() # Different name for vehicle group

player_obj = PlayerCar(player_x_start, player_y_start) # Different object name
player_car_group.add(player_obj)


imgFiles = ['pickup_truck.png', 'semi_trailer.png', 'taxi.png', 'van.png']
vehicle_images_list = [] # Varied list name
for fileName in imgFiles: # Varied loop variable
    loadedImage = pygame.image.load(fileName)
    vehicle_images_list.append(loadedImage)
    

crash_pic = pygame.image.load('crash.png') # Varied variable name
crash_rect = crash_pic.get_rect()


# --- Main Game Loop (Re-ordered and Modified Logic) ---
running = True
while running:
    
    clk.tick(FPS)
    
    # Event Handling Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if event.type == KEYDOWN and not gameOver:
            
            # Use explicit conditional checks for movement bounds
            if event.key == K_LEFT and player_obj.rect.center[0] > left_lane:
                player_obj.rect.x -= 100
            elif event.key == K_RIGHT and player_obj.rect.center[0] < rightLane:
                player_obj.rect.x += 100
            elif event.key == K_DOWN and player_obj.rect.bottom < H: # Use H instead of height
                player_obj.rect.y += 20
            elif event.key == K_UP and player_obj.rect.top > 0:
                player_obj.rect.y -= 20
    
    
    if not gameOver:
        
        # --- Drawing Phase with varied color names ---
        screen.fill(grn) # Use grn
        
        pygame.draw.rect(screen, GRY, RoadRect) # Use GRY
        
        # Draw side markers
        pygame.draw.rect(screen, yell, leftEdge) # Use yell
        pygame.draw.rect(screen, yell, rEdge)
        
        # Animate and draw lane markers
        marker_y_offset += speed_current * 2
        
        if marker_y_offset >= MARKER_HEIGHT * 2: # Use MARKER_HEIGHT
            marker_y_offset = 0
            
        # Draw markers with non-standard loop variable (i) and non-standard calculation
        step = MARKER_HEIGHT * 2
        i_start = MARKER_HEIGHT * -2
        for i in range(i_start, H, step):
            pygame.draw.rect(screen, White, (left_lane + 45, i + marker_y_offset, markW, MARKER_HEIGHT))
            pygame.draw.rect(screen, White, (centerLane + 45, i + marker_y_offset, markW, MARKER_HEIGHT))
            
        # Draw player
        player_car_group.draw(screen)
        
        # --- Vehicle Spawning Logic ---
        # Changed condition for spawning (less than 3 instead of 2)
        if len(enemy_vehicles) < 3: 
            
            spawnVehicle = True # Use boolean variable
            for car in enemy_vehicles:
                # Different constant multiplier for gap check
                if car.rect.top < car.rect.height * 2: 
                    spawnVehicle = False
                    
            if spawnVehicle:
                
                # Use random.choice on the Capitalized Lanes list
                carLane = random.choice(Lanes) 
                
                
                carImage = random.choice(vehicle_images_list)
                # Use VehicleSprite class name
                newVehicle = VehicleSprite(carImage, carLane, H / -2) 
                enemy_vehicles.add(newVehicle)
        
        # --- Vehicle Movement and Scoring ---
        for moving_car in enemy_vehicles: # Use a different loop variable
            moving_car.rect.y += speed_current
            
            # Check if vehicle is off screen
            if moving_car.rect.top >= H:
                moving_car.kill()
                current_score += 1 # Use verbose score name
                
                # Speed increase logic
                if current_score > 0 and current_score % 5 == 0:
                    speed_current += 1
        
        # Draw opponents
        enemy_vehicles.draw(screen)
        
        # --- Score Display (Font and Position adjustment) ---
        scoreFont = pygame.font.Font(pygame.font.get_default_font(), 30)
        scoreTxt = scoreFont.render('Score: ' + str(current_score), True, White)
        scoreRect = scoreTxt.get_rect()
        scoreRect.topright = (W - 10, 10) # Use W for width
        screen.blit(scoreTxt, scoreRect)
        
        
        # --- Final Collision Check (outside event loop) ---
        if pygame.sprite.spritecollide(player_obj, enemy_vehicles, True):
            gameOver = True
            crash_rect.center = [player_obj.rect.center[0], player_obj.rect.top]
            
    # --- Game Over Screen ---
    if gameOver:
        screen.blit(crash_pic, crash_rect)
        
        pygame.draw.rect(screen, Red, (0, 50, W, 100)) # Use W and Red
        
        goFont = pygame.font.Font(pygame.font.get_default_font(), 30)
        goTxt = goFont.render('PLAY AGAIN? (Y/N)', True, White)
        goRect = goTxt.get_rect()
        goRect.center = (W / 2, 100)
        screen.blit(goTxt, goRect)
        
    pygame.display.update()

    # --- Game Over Input Loop ---
    while gameOver:
        
        clk.tick(FPS)
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                gameOver = False
                running = False
                
            
            if event.type == KEYDOWN:
                if event.key == K_y:
                    
                    # Reset state with varied variable names
                    gameOver = False
                    speed_current = 2
                    current_score = 0
                    enemy_vehicles.empty()
                    player_obj.rect.center = [player_x_start, player_y_start]
                elif event.key == K_n:
                    
                    gameOver = False
                    running = False

pygame.quit()
        
        
