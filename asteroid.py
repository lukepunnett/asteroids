
import pygame
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(random.uniform(-50, 50), random.uniform(-50, 50))  # Random velocity

    def update(self, dt):
        # Update the position based on velocity and delta time
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "grey", (int(self.position.x), int(self.position.y)), self.radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_num = random.uniform(20,50) 
              # Generate a random angle for splitting
            random_angle = random.uniform(15, 45)  # Random angle between 15 and 45 degrees
            self.velocity1 = self.velocity.rotate(random_angle)  # Rotate by random_angle
            self.velocity2 = self.velocity.rotate(-random_angle)  # Rotate by -random_angle
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.x, self.y, self.new_radius)
            asteroid_b = Asteroid(self.x, self.y, self.new_radius)
            asteroid_a.velocity = velocity1*1.2
            asteroid_b.velocity = velocity2*1.2

