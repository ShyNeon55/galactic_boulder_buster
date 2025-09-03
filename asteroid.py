from circleshape import *
from constants import * 
import random


class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        a = Asteroid(self.position.x, self.position.y, new_radius)
        b = Asteroid(self.position.x, self.position.y, new_radius)
        #^This creates two asteroids
        
        av, bv = self._split_velocities(scale = 1.2)
        #^This splits the velocity from the original amongst the two new ones

        a.velocity, b.velocity = av, bv
        #^This assigns the new velocities to the new asteroids
        
    
    
    #This creates a new method to simplify splitiing the velocities between the two asteroids
    #Potentially need to change this if adding more asteroids in the future
    def _split_velocities(self, scale = 1.0):
        angle = random.uniform(20, 50)
        v = self.velocity
        #This gaurds against asteroids with no velocity
        if self.velocity.length_squared() < 1e-6:
            self.velocity = pygame.Vector2(1, 0).rotate(random.uniform(0, 360))
        return v.rotate(angle) * scale, v.rotate(-angle) * scale

        