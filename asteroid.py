from circleshape import CircleShape
import pygame, constants, random

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)
        self.containers = None

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position[0], self.position[1]), self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        child_one_angle = self.velocity.rotate(angle)
        child_two_angle = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        child_one = Asteroid(self.position.x, self.position.y, new_radius)
        child_one.velocity = child_one_angle * 1.2

        child_two = Asteroid(self.position.x, self.position.y, new_radius)
        child_two.velocity = child_two_angle * 1.2
