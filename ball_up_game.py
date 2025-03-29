import pygame

class BallUpGame:
    def __init__(self):
        # Screen dimensions
        self.WIDTH, self.HEIGHT = 400, 300
        # Ball settings
        self.ball_radius = 15
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT // 2
        # Button settings
        self.button_rect = pygame.Rect(10, self.HEIGHT - 50, 80, 40)
        self.button_color = (0, 0, 255)  # Blue
        self.font = pygame.font.SysFont(None, 24)
        self.button_text = self.font.render("UP", True, (255, 255, 255))  # White
        self.running = True

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.ball_y -= 10  # Move the ball up by 10 pixels

    def run(self, surface):
        # Handle events
        for event in pygame.event.get():
            self.process_event(event)
        # Update game state
        # (Add any game logic updates here if needed)
        # Render game state
        surface.fill((255, 255, 255))  # Fill the screen with white
        pygame.draw.circle(surface, (0, 0, 0), (self.ball_x, self.ball_y), self.ball_radius)  # Black ball
        pygame.draw.rect(surface, self.button_color, self.button_rect)
        surface.blit(self.button_text, (self.button_rect.x + 20, self.button_rect.y + 10))
        pygame.display.flip()
