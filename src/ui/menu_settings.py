import pygame
from pygame.locals import *
from random import randrange
import sys
from sys import argv
from getopt import getopt, GetoptError
import time
import os

class Settings:
    def __init__(self):
        self.screen = screen
        self.maincolor = [0, 0, 0]
        self.white = [255, 255, 255]
        self.bsound = pygame.mixer.Sound("data/sounds/CLICK10A.WAV")
        self.background = pygame.image.load("data/menubg/menubg.png")
        self.backgroundadded = pygame.image.load("data/menubg/added.png")
        self.sav = pygame.image.load("data/menubg/sav.png")
        self.menu = ["  Fullscreen  ", "  Back to main  "]
        self.menubg = []
        self.menubg.append(pygame.image.load("data/menubg/al.png").convert())
        self.menubg.append(pygame.image.load("data/menubg/ci.png").convert())
        self.menubg.append(pygame.image.load("data/menubg/he.png").convert())
        self.menubg.append(pygame.image.load("data/menubg/na.png").convert())
        self.menubg.append(pygame.image.load("data/menubg/di.png").convert())
        self.menuall = ""
        self.selectedmenu = 0
        self.mid = []
        # get menu width
        self.menuid()
        # all menu in one:
        self.listmenuall()
        # mainloop
        sz = 0
        szam = 0
        szamlalo = 0
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    exit()
                if self.event.type == pygame.KEYDOWN:
                    self.bsound.play()
                    if self.event.key == pygame.K_LEFT:
                        if self.selectedmenu == 0:
                            self.selectedmenu = len(self.menu)-1
                        else:
                            self.selectedmenu = self.selectedmenu-1
                    elif self.event.key == pygame.K_RIGHT:
                        if self.selectedmenu == len(self.menu)-1:
                            self.selectedmenu = 0
                        else:
                            self.selectedmenu = self.selectedmenu+1
                    elif self.event.key == pygame.K_RETURN:
                        if self.selectedmenu == 0:
                            pygame.display.toggle_fullscreen()
                        else:
                            plc = Menu()
            # 1st layer: background color
            self.screen.fill(self.maincolor)
            self.bg = self.menubg[szam]
            self.bg.set_alpha(sz)
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.backgroundadded, (0, 0))
            # 2nd layer: menus
            self.crt_menu()
            # 3rd layer: transparent image
            self.screen.blit(self.background, (0, 0))
            
            font = pygame.font.Font("data/LiberationSans-Regular.ttf", 15)
            text_surface = font.render("Balazs Nagy - BFruit - "+VERSION , True, self.white)
            self.screen.blit(text_surface, (3, 460))
            
            szamlalo = szamlalo + 4
            
            if szamlalo < 245:
                sz = sz + 4
            if szamlalo > 244:
                sz = sz - 4
                
            if szamlalo > 490:
                sz = 0
                szamlalo = 0
                if szam == len(self.menubg)-1:
                    szam = 0
                else:
                    szam = szam + 1
            
            
            pygame.display.update()
            
    def menuid(self):
        for n in self.menu:
            font = pygame.font.Font("data/LiberationSans-Regular.ttf", 25)
            text_surface = font.render(n, True, self.white)
            self.mid.append(text_surface.get_width())
            
    def listmenuall(self):
        for n in self.menu:
            self.menuall = self.menuall+n
            
    def crt_menu(self):
        nmb = 0
        xpos = 0
        while nmb <= self.selectedmenu:
            xpos = xpos-self.mid[nmb]
            nmb = nmb+1
        xpos = xpos+self.mid[self.selectedmenu]/2
        # draw menus on screen
        font = pygame.font.Font("data/LiberationSans-Regular.ttf", 25)
        text_surface = font.render(self.menuall, True, self.white)
        self.screen.blit(text_surface, (320+xpos, 15))
