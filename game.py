import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BALL_RADIUS = 30
BALL_COLOR = (255, 0, 0)  # Red ball
BG_COLOR = (0, 0, 0)  # Black background
JUMP_AMOUNT = 50  # Amount to move upward when button is pressed

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Ball Game")
clock = pygame.time.Clock()

# Initialize ball position
ball_x = WIDTH // 2
ball_y = HEIGHT - BALL_RADIUS  # Start at bottom of screen

def draw_ball(x, y):
    """Draw the ball at the specified position"""
    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)

# Main game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Move ball upward
                ball_y = max(BALL_RADIUS, ball_y - JUMP_AMOUNT)  # Ensure ball doesn't go off screen
    
    # Clear screen
    screen.fill(BG_COLOR)
    
    # Draw ball
    draw_ball(ball_x, ball_y)
    
    # Update display
    pygame.display.flip()
    
    # Control game speed
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()