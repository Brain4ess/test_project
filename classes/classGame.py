import pygame as pg
from pygame.locals import *
from UI.classGameScreen import GameScreen
from classes.classBackground import BG
from classes.classCharacter import Character
from classes.classCamera import Camera

class Game:
    def __init__(self, screen: GameScreen, fps: int):
        self.imageBG = 'assets/images/placeholders/maps/BigMapPlaceholderCenterDot.png'
        self.fps = fps
        self.screen = screen
        self.bg = BG(self.imageBG, self.screen, spawnpoint=(500, 500))
        self.run = True
        self.camera = Camera(self.screen, self.bg.width, self.bg.height, self.bg)
        self.player = Character(self.bg, self.screen, 5)
        self.clock = pg.time.Clock()
    
    
    def eventGame(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.run = False
    
    
    def runGame(self):
        while self.run:
            self.eventGame()
            
            self.bg.blitBG(self.camera.getoffset())
            
            self.player.update(self.camera.getoffset())
            self.camera.update(self.player)
            
            pg.display.update()
            self.clock.tick(self.fps)
