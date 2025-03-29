import pygame
import sys

class BallGame:
    def __init__(self):
        # Constants
        self.WIDTH, self.HEIGHT = 800, 600
        self.FPS = 60
        self.BALL_RADIUS = 30
        self.BALL_COLOR = (255, 0, 0)  # Red ball
        self.BG_COLOR = (0, 0, 0)  # Black background
        self.JUMP_AMOUNT = 50  # Amount to move upward when button is pressed
        
        # Initialize pygame (but don't create window - Sugar will do that)
        pygame.init()
        
        # Initialize ball position
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT - self.BALL_RADIUS  # Start at bottom of screen
        
        # Create clock for controlling framerate
        self.clock = pygame.time.Clock()
        
        # Setup game state
        self.running = True
        self.canvas = None  # Will be set by Sugar
        
        # Add a flag to track if the space key is being pressed
        self.space_pressed = False
    
    def set_canvas(self, canvas):
        """Store a reference to the pygame canvas"""
        self.canvas = canvas
        # The screen will be automatically set up by sugargame
    
    def draw_ball(self, x, y, screen):
        """Draw the ball at the specified position"""
        pygame.draw.circle(screen, self.BALL_COLOR, (x, y), self.BALL_RADIUS)
    
    def run(self):
        """Main game loop - will be called by sugargame"""
        # Get the pygame screen - in some sugargame versions, this is done automatically
        screen = pygame.display.get_surface()
        
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            # Check for key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.space_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.space_pressed = False
        
        # Check key states (this is an alternative method that might work better in Sugar)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or self.space_pressed:
            # Move ball upward
            self.ball_y = max(self.BALL_RADIUS, self.ball_y - self.JUMP_AMOUNT)
            self.space_pressed = False  # Reset after moving to prevent continuous movement
        
        # Clear screen
        screen.fill(self.BG_COLOR)
        
        # Draw ball
        self.draw_ball(self.ball_x, self.ball_y, screen)
        
        # Update display
        pygame.display.flip()
        
        # Control game speed
        self.clock.tick(self.FPS)
        
        return True  # Continue running
    
    def cleanup(self):
        """Clean up pygame resources properly"""
        # Release all pygame resources properly
        try:
            pygame.display.quit()
            pygame.quit()
        except:
            pass  # Ignore errors during cleanup
