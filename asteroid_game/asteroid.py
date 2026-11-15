import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        color = (255,255,255)
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            new_vector1 = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast1.velocity = new_vector1 * 1.2
            new_ast2.velocity = new_vector2 * 1.2