import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, SHOT_RADIUS)
        # Set the velocity based on the player's angle
        self.velocity = pygame.Vector2(0, 1).rotate(angle) * PLAYER_SHOOT_SPEED  # Set initial velocity

    def update(self, dt):
        # Update the position based on velocity and delta time
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw the shot as a circle
        pygame.draw.circle(screen, "yellow", (int(self.position.x), int(self.position.y)), self.radius)

