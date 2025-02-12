import pygame as pg
from pygame.locals import *
from pygame.image import load

class BG: 
    def __init__(self, mapImage: str, screen: pg.Surface, speed: int = 0, spawnpoint: pg.math.Vector2 = pg.math.Vector2(0,0)):
        self.mapImage = mapImage
        self.screen = screen
        self.speed = speed
        self.spawnpoint = (spawnpoint[0] - self.screen.get_width() / 2, spawnpoint[1] - self.screen.get_height() / 2)
        self.__post_init__()
    
    
    def __post_init__(self):
        self.bg = load(self.mapImage).convert()
        self.width = self.bg.get_width()
        self.height = self.bg.get_height()
        
    
    def blitBG(self, offset: pg.math.Vector2 = pg.math.Vector2(0,0)):
        self.screen.blit(self.bg, self.bg.get_rect().topleft - (offset + self.spawnpoint))
        self.topleftpos = self.bg.get_rect().topleft - (offset + self.spawnpoint)
    
    
    def blitStatic(self):
        self.screen.blit(self.bg, ((self.screen.get_width() // 2) - (self.bg.get_width() // 2), (self.screen.get_height() // 2) - (self.bg.get_height() // 2)))
