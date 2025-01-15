import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Popcat Game")

# Load images
closed_image_path = "assets/closed_mouth_image.png"  # Ensure the correct image name
open_image_path = "assets/open_mouth_image.png"      # Ensure the correct image name
closed_image = pygame.image.load(closed_image_path)
open_image = pygame.image.load(open_image_path)

# Scale images if necessary
closed_image = pygame.transform.scale(closed_image, (200, 200))
open_image = pygame.transform.scale(open_image, (200, 200))

# Game variables
pop_count = 0
is_open = False
font = pygame.font.Font(None, 36)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_open = True
            pop_count += 1
        if event.type == pygame.MOUSEBUTTONUP:
            is_open = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the Popcat
    if is_open:
        screen.blit(open_image, (width // 2 - 100, height // 2 - 100))
    else:
        screen.blit(closed_image, (width // 2 - 100, height // 2 - 100))

    # Display pop count
    count_text = font.render(f'Count: {pop_count}', True, (0, 0, 0))
    screen.blit(count_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)
