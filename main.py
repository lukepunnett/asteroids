import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, SHOT_RADIUS, PLAYER_SHOOT_SPEED, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE, ASTEROID_KINDS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import random
import sys

def main():
    print("Starting Asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    control = True
    clock = pygame.time.Clock()

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Initialize player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    # Initialize asteroid field
    # We let the AsteroidField add itself to all necessary groups.
    # We will NOT remove it, as that seems to break its update logic.
    AsteroidField.containers = (updatable, drawable, asteroids)
    asteroid_field = AsteroidField()

    # Main game loop
    while control:
        dt = clock.tick(60) / 1000  # Calculate delta time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                control = False

        # --- UPDATE LOGIC ---

        # Update player and check for shooting
        shot = player.update(dt)
        if shot:
            shots.add(shot)
            updatable.add(shot)
            drawable.add(shot)

        # Update all shots and asteroids.
        # The 'updatable' group contains the player, shots, asteroids, AND the field manager.
        # Calling update() on this single group handles everything.
        updatable.update(dt)

        # --- COLLISION DETECTION ---
        # UPDATED: The fix is to add a check inside the loops to specifically
        # ignore the asteroid_field object during collision checks.

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            # This check prevents the 'no attribute position' error
            if asteroid is asteroid_field:
                continue
            if player.colliding(asteroid):
                print("Game Over!")
                pygame.quit()
                sys.exit(0)

        # Check for collisions between shots and asteroids
        for shot in shots:
            # We must copy the list of asteroids to iterate over, as we might modify it
            for asteroid in list(asteroids):
                # This check prevents the 'no attribute position' error
                if asteroid is asteroid_field:
                    continue
                
                if shot.colliding(asteroid):
                    print("Asteroid hit!")
                    shot.kill()
                    asteroid.kill()
                    # This shot is gone, so we break to the next shot
                    break

        # --- DRAWING ---

        screen.fill("black")
        drawable.draw(screen) # Using the group's draw method is more efficient
        pygame.display.flip()

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main() 
