from circleshape import CircleShape
import constants, pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.containers = None

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position[0], self.position[1]), self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)
