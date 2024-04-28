import pygame
from colorsys import hsv_to_rgb
    
def get_rgb_color_list(num_colors=5, saturation=1.0, value=1.0):
    rgb_colors = []
    hsv_colors = [[float(x / num_colors), saturation, value] for x in range(num_colors)]
    
    for hsv in hsv_colors:
       hsv = [int(x * 255) for x in hsv_to_rgb(*hsv)]
       rgb_colors.append(hsv)
    
    return rgb_colors

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))

colour_list = get_rgb_color_list(num_colors=60)
colour_list_index = 0

# Time variables
change_color_every_ms = 200  # Total time to change from one color to the next
last_change_time = pygame.time.get_ticks()
increment = 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current time
    current_time = pygame.time.get_ticks()

    if (current_time - last_change_time) > change_color_every_ms:
        last_change_time = current_time
        colour_list_index += increment
        if colour_list_index > len(colour_list) - 1:
            increment = increment * -1
            colour_list_index += increment
        if colour_list_index < 0:
            increment = increment * -1
            colour_list_index += increment

    rgb_colour = colour_list[colour_list_index]


    # Fill the screen with the interpolated color
    screen.fill(rgb_colour)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
