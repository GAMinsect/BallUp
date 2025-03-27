import pygame

class BallUpGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Screen dimensions
        self.WIDTH, self.HEIGHT = 400, 300
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Ball Up Game")

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)

        # Ball settings
        self.ball_radius = 15
        self.ball_x = self.WIDTH // 2
        self.ball_y = self.HEIGHT // 2

        # Button settings
        self.button_rect = pygame.Rect(10, self.HEIGHT - 50, 80, 40)
        self.button_color = self.BLUE
        self.font = pygame.font.SysFont(None, 24)
        self.button_text = self.font.render("UP", True, self.WHITE)

        self.running = True

    def process_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.ball_y -= 10  # Move the ball up by 10 pixels

    def update(self):
        pass  # Add game logic updates here if needed

    def render(self):
        self.screen.fill(self.WHITE)
        pygame.draw.circle(self.screen, self.BLACK, (self.ball_x, self.ball_y), self.ball_radius)
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        self.screen.blit(self.button_text, (self.button_rect.x + 20, self.button_rect.y + 10))
        pygame.display.flip()
