from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from circleshape import CircleShape
import pygame
from shot import Shot
class Player(CircleShape):
    def __init__(self,x,y): 
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0# in the player class
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if (self.shoot_timer > 0):
            self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-PLAYER_TURN_SPEED * dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED * dt)   # Rotate right
        if keys[pygame.K_w]:
            self.move(PLAYER_SPEED * dt)
        if keys[pygame.K_s]:
            self.move(-PLAYER_SPEED * dt)
        if keys[pygame.K_SPACE]:  # Check for spacebar press
            if(self.shoot_timer <= 0):
                self.shoot_timer += PLAYER_SHOOT_COOLDOWN
                return self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        # Create a new shot at the player's position
        shot = Shot(self.position.x, self.position.y, self.rotation)  # Pass the rotation angle
        
        return shot  # Return the shot object

