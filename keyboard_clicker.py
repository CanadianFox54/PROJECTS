import pygame
from pynput import keyboard

pygame.init()

SCREEN_WIDTH, SCREEN_HIGHT = 400, 300
WHITE, BLACK = (255, 255, 255), (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("Keyboard Clicker")

font = pygame.font.Font(None, 50)

count = 0
keys_pressed = set()

def on_press(key):
    global count
    if key not in keys_pressed:
        count += 1
        keys_pressed.add(key)

def on_release(key):
    global count
    if key in keys_pressed:
        keys_pressed.remove(key)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(WHITE)

    counter_surface = font.render(f"Keys Pressed: {count}", True, BLACK)
    counter_rect = counter_surface.get_rect(center=(SCREEN_WIDTH // 2,SCREEN_HIGHT // 2))
    screen.blit(counter_surface, counter_rect)

    pygame.display.flip()

pygame.quit()
listener.stop()