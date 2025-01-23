import pygame

MESSAGE_INPUT = input("what is your message: ")

pygame.init()



SCREEN_WIDTH, SCREEN_HIGHT = 4000, 3000 #change screen width and size
BLACK, WHITE = (255, 255, 255), (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption("mm")

font = pygame.font.Font(None, 100) #change font size

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    counter_surface = font.render(f"{MESSAGE_INPUT}", True, BLACK)
    counter_rect = counter_surface.get_rect(center=(SCREEN_WIDTH // 2,SCREEN_HIGHT // 2))
    screen.blit(counter_surface, counter_rect)

    pygame.display.flip()

pygame.quit()