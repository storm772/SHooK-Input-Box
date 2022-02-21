import pygame
import sys

pygame.init()
# Change to True if you want advanced debugging.
# Messages like: 'input box (de)/activated', 'input box empty' will appear.
advancedDebug = False

# Set Clock
clock = pygame.time.Clock()

# Set screen
screen = pygame.display.set_mode([320, 95])
pygame.display.set_caption("[SHooK] Input Box")

# Font
font = pygame.font.SysFont(None, 48)

# Render Text Hook System
def renderText(text, *pos):
    if not (pos): pos = (100,100)
    textE = font.render(text, True, (0))
    screen.blit(textE, (pos))

# Fill before render text.
screen.fill((255,255,255))
renderText(f'Input a string:', (10, 12))

# Input Box stuff
base_font = pygame.font.Font(None, 32)
color = pygame.Color('chartreuse4')

# Input Box variables
active = False 
user_text = ''

# Your commands here
def commands():
    if user_text == 'quit': quit(), pygame.quit()
    if len(user_text) > 32: print('the string that you\'ve input is greater than the max characters allowed.')
    print(user_text)

while True:
    for event in pygame.event.get():
        # Silent Quit
        if event.type == pygame.QUIT: pygame.quit(), sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
          
            # Check if clicked at input box or its border
            if pygame.Rect(10, 50, 300, 32).collidepoint(event.pos) or pygame.Rect(7, 47, 306, 38).collidepoint(event.pos): 
                if active == True:
                    if advancedDebug == True:
                        print(f'[SHooK] Attempted to activate input-box but it\'s already activated.')
                    else:
                        pass
                else:
                    if advancedDebug == True:
                        print(f'[SHooK] Activated Input-Box!')
                    else:
                        pass
                    active = True
                    
            # If didnt clicked, dont allow user to input
            else: 
                if active == False:
                    pass 
                else:
                    if advancedDebug == True:
                        print('[SHooK] De-activated Input-Box!')
                    else:
                        pass
                    active = False
                    
        # Main system
        if event.type == pygame.KEYDOWN:           
            if active == True:
              
                # RETURN = Enter key
                if event.key == pygame.K_RETURN: 
                  
                    # If nothing was done, dont execute anything
                    if not user_text:
                        if advancedDebug == True:
                            print(f'[SHooK] User sent a empty input!')
                        else:
                            pass
                          
                    # Else, execute commands, set input to nothing, make input box not active
                    else:
                        commands()
                        user_text = ''
                        active = False
                        if advancedDebug == True:
                            print(f'[SHooK] Sent a command! Text: {user_text}')
                        else:
                            pass
                          
                # Backspace System
                # TODO: Allow hold backspace.
                if event.key == pygame.K_BACKSPACE: 
                    user_text = user_text[:-1]
                else: user_text += event.unicode
            else: 
                pass
              
    # Active/Disabled Colors
    if (active == False):
        color = pygame.Color('chartreuse4')
    if (active == True):
        color = pygame.Color(53, 107, 0)
        
    # Draw Border then input box itself
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(7, 47, 306, 38))  # input rect border
    pygame.draw.rect(screen, color, pygame.Rect(10, 50, 300, 32)) # input rect
    
    # Render what was typed
    screen.blit(base_font.render(user_text, True, (255, 255, 255)), (pygame.Rect(10, 50, 300, 32).x+5, pygame.Rect(10, 50, 300, 32).y+5))
    
    # Keep updating the screen
    pygame.display.update()
    
    # Set FPS to 60
    clock.tick(60)
