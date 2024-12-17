import pygame
from pygame.locals import *
from random import randrange
import sys
from sys import argv
from getopt import getopt, GetoptError
import time
import os

class Game:
    def __init__(self):
        self.mut = 0
        self.wins = [0, 0, 0, 0, 0]
        self.keys = 1
        self.credit = 20
        self.bet = 1
        self.lastwin = 0
        self.show = []
        
        self.screen = screen
        
        self.bsound = pygame.mixer.Sound("data/sounds/CLICK10A.WAV")
        self.rasound = pygame.mixer.Sound("data/sounds/film_projector.wav")
        self.rbsound = pygame.mixer.Sound("data/sounds/film_projector.wav")
        self.rcsound = pygame.mixer.Sound("data/sounds/film_projector.wav")
        self.bgsound = pygame.mixer.Sound("data/sounds/background001.wav")
        self.beepsound = pygame.mixer.Sound("data/sounds/beep.wav")
        self.background = pygame.image.load("data/img/bg.png")
        self.rlayer = pygame.image.load("data/img/rlayer.png")
        self.windowlayer = pygame.image.load("data/img/windowlayer.png")
        self.imgone = pygame.image.load("data/img/1.png")
        self.imgtwo = pygame.image.load("data/img/2.png")
        self.imgthree = pygame.image.load("data/img/3.png")
        self.imgfour = pygame.image.load("data/img/4.png")
        self.imgfive = pygame.image.load("data/img/5.png")
        self.imgsix = pygame.image.load("data/img/6.png")
        self.imgseven = pygame.image.load("data/img/7.png")
        self.imgeight = pygame.image.load("data/img/8.png")
        
        img = []
        img.append(self.imgone)
        img.append(self.imgtwo)
        img.append(self.imgthree)
        img.append(self.imgfour)
        img.append(self.imgfive)
        img.append(self.imgsix)
        img.append(self.imgseven)
        img.append(self.imgeight)
        
        self.bgsound.play(loops=-1)
        
        # mainloop
        while True:
            self.screen.fill([0, 0, 0])
            self.screen.blit(self.background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bgsound.stop()
                    exit()
                    
                if event.type == pygame.KEYDOWN:
                    self.bsound.play()
                    if event.key == pygame.K_LEFT and self.keys == 1:
                        if self.credit > 0:
                            if self.credit - self.bet < 0:
                                self.bet = self.credit
                            self.credit = self.credit - self.bet
                            self.randi()
                            self.check()
                            self.roll(img)
                            self.screen.blit(self.background, (0, 0))
                            self.drawl()
                            self.winner()
                        elif self.credit == 0 and self.bet == 0:
                            self.bgsound.stop()
                            plc = Menu()
                            
                    if self.credit > 0:
                        if event.key == pygame.K_UP and self.keys == 1:
                            if self.credit - self.bet - 1 >= 0:
                                self.bet = self.bet + 1
                            else:
                                self.bet = 1
                            if self.bet == 11:
                                self.bet = 1
                            
                    else:
                        self.bet = 0
                            
                            
                    if event.key == pygame.K_F1:
                        if self.keys == 1:
                            self.keys = 0
                            self.menu = "h"
                        elif self.keys == 0:
                            self.keys = 1
                            self.menu = "n"
                            
                    if event.key == pygame.K_RETURN:
                        self.keys = 0
                        self.menu = "e"
                      
                    if event.key == pygame.K_ESCAPE and self.keys == 1:
                        self.bgsound.stop()
                        plc = Menu()
                            
            self.draw_side()
            
            if self.mut == 1:
                self.drawl()
                self.check()
                self.wins = [0, 0, 0, 0, 0]
            
            if self.credit == 0 and self.bet == 0:
                font = pygame.font.Font("data/LiberationSans-Regular.ttf", 55)
                text_surface = font.render("Game Over", True, [255, 0, 0])
                self.screen.blit(text_surface, (70, 190))
            
            self.screen.blit(self.rlayer, (37, 48))
            self.screen.blit(self.windowlayer, (0, 0))
            
            if self.keys == 0 and self.menu == "h":
                self.helpmenu()
            if self.keys == 0 and self.menu == "e":
                self.endthegame(scr)
            
            pygame.display.update()
    
    def roll(self, img):
        szam = 0
        
        
        # toll time
        rolla = randrange(5, 14)
        rollb = randrange(rolla+1, rolla+5)
        rollc = randrange(rollb+1, rollb+5)
        
        # a column
        rollaf = []
        rollaf.append(img[int(self.show[0])-1])
        rollaf.append(img[int(self.show[1])-1])
        rollaf.append(img[int(self.show[2])-1])
        while szam <= rolla-3:
            rollaf.append(img[randrange(0, 8)])
            szam = szam + 1
        self.rasound.play()
        rollaf.append(img[int(self.showold[0])-1])
        rollaf.append(img[int(self.showold[1])-1])
        rollaf.append(img[int(self.showold[2])-1])
        
            
        szam = 0
        
        # b column
        rollbf = []
        rollbf.append(img[int(self.show[3])-1])
        rollbf.append(img[int(self.show[4])-1])
        rollbf.append(img[int(self.show[5])-1])
        while szam <= rollb-3:
            rollbf.append(img[randrange(0, 8)])
            szam = szam +1
        self.rbsound.play()
        rollbf.append(img[int(self.showold[3])-1])
        rollbf.append(img[int(self.showold[4])-1])
        rollbf.append(img[int(self.showold[5])-1])
            
        szam = 0
        
        # c column
        rollcf = []
        rollcf.append(img[int(self.show[6])-1])
        rollcf.append(img[int(self.show[7])-1])
        rollcf.append(img[int(self.show[8])-1])
        while szam <= rollc-3:
            rollcf.append(img[randrange(0, 8)])
            szam = szam +1
        self.rcsound.play()
        rollcf.append(img[int(self.showold[6])-1])
        rollcf.append(img[int(self.showold[7])-1])
        rollcf.append(img[int(self.showold[8])-1])
        
        szama = len(rollaf)-1
        szamb = len(rollbf)-1
        szamc = len(rollcf)-1
        
        while szamc > 2:
            self.screen.fill([0, 0, 0])
            self.screen.blit(self.background, (0, 0))
            
            if szama > 2:
                self.screen.blit(rollaf[len(rollaf)-3], (36, 46))
                self.screen.blit(rollaf[len(rollaf)-2], (36, 174))
                self.screen.blit(rollaf[len(rollaf)-1], (36, 302))
                szama = szama - 1
                del(rollaf[len(rollaf)-1])
            else:
                self.screen.blit(rollaf[len(rollaf)-3], (36, 46))
                self.screen.blit(rollaf[len(rollaf)-2], (36, 174))
                self.screen.blit(rollaf[len(rollaf)-1], (36, 302))
                self.rasound.stop()
                
            if szamb > 2:
                self.screen.blit(rollbf[len(rollbf)-3], (165, 46))
                self.screen.blit(rollbf[len(rollbf)-2], (165, 174))
                self.screen.blit(rollbf[len(rollbf)-1], (165, 302))
                szamb = szamb - 1
                del(rollbf[len(rollbf)-1])
            else:
                self.screen.blit(rollbf[len(rollbf)-3], (165, 46))
                self.screen.blit(rollbf[len(rollbf)-2], (165, 174))
                self.screen.blit(rollbf[len(rollbf)-1], (165, 302))
                self.rbsound.stop()
                
            if szamc > 2:
                self.screen.blit(rollcf[len(rollcf)-3], (295, 46))
                self.screen.blit(rollcf[len(rollcf)-2], (295, 174))
                self.screen.blit(rollcf[len(rollcf)-1], (295, 302))
                szamc = szamc - 1
                del(rollcf[len(rollcf)-1])
            else:
                self.screen.blit(rollcf[len(rollcf)-3], (295, 46))
                self.screen.blit(rollcf[len(rollcf)-2], (295, 174))
                self.screen.blit(rollcf[len(rollcf)-1], (295, 302))
            
            self.draw_side()
            self.screen.blit(self.rlayer, (37, 48))
            self.screen.blit(self.windowlayer, (0, 0))
            pygame.display.update()
            rollc = rollc - 1
        self.rcsound.stop()
    
    def draw_side(self):
        #animation
        digifont = pygame.font.Font("data/DIGITAL2.ttf",24)
        text_surface = digifont.render("88888888888", True, [60, 0, 0])
        self.screen.blit(text_surface, (470, 50))
        
        text_surface = digifont.render("F1 FOR HELP", True, [255, 0, 0])
        self.screen.blit(text_surface, (470, 50))
        
        font = pygame.font.Font("data/LiberationSans-Regular.ttf", 15)
        text_surface = font.render("Bet:", True, [230, 255, 255])
        self.screen.blit(text_surface, (500, 185))
        # multip
        digifont = pygame.font.Font("data/DIGITAL2.ttf",24)
        text_surface = digifont.render("88", True, [60, 0, 0])
        self.screen.blit(text_surface, (500, 210))
        text_surface = digifont.render(str(self.bet), True, [255, 0, 0])
        self.screen.blit(text_surface, (500, 210))
        
        font = pygame.font.Font("data/LiberationSans-Regular.ttf", 15)
        text_surface = font.render("Winner Paid:", True, [230, 255, 255])
        self.screen.blit(text_surface, (500, 255))
        # last win
        digifont = pygame.font.Font("data/DIGITAL2.ttf",24)
        text_surface = digifont.render("888", True, [60, 0, 0])
        self.screen.blit(text_surface, (500, 280))
        text_surface = digifont.render(str(self.lastwin), True, [255, 0, 0])
        self.screen.blit(text_surface, (500, 280))
        
        font = pygame.font.Font("data/LiberationSans-Regular.ttf", 15)
        text_surface = font.render("Credit:", True, [230, 255, 255])
        self.screen.blit(text_surface, (500, 325))
        # startsum
        digifont = pygame.font.Font("data/DIGITAL2.ttf",24)
        text_surface = digifont.render("888888", True, [60, 0, 0])
        self.screen.blit(text_surface, (500, 350))
        text_surface = digifont.render(str(self.credit), True, [255, 0, 0])
        self.screen.blit(text_surface, (500, 350))
    
    def drawl(self):        
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[0])+".png"), (36, 46))
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[1])+".png"), (36, 174))
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[2])+".png"), (36, 302))
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[3])+".png"), (165, 46))
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[4])+".png"), (165, 174))
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[5])+".png"), (165, 302))
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[6])+".png"), (295, 46))
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[7])+".png"), (295, 174))
        self.screen.blit(pygame.image.load("data/img/"+str(self.show[8])+".png"), (295, 302))

    # random images
    def randi(self):
        self.showold = []
        if len(self.show) > 1:
            self.showold = self.show
        else:
            self.showold = ["8", "8", "8", "8", "8", "8", "8", "8", "8"]
        self.mut = 1
        ran = {}
        ran[0] = randrange(1, 335)
        ran[1] = randrange(1, 335)
        ran[2] = randrange(1, 335)
        ran[3] = randrange(1, 335)
        ran[4] = randrange(1, 335)
        ran[5] = randrange(1, 335)
        ran[6] = randrange(1, 335)
        ran[7] = randrange(1, 335)
        ran[8] = randrange(1, 335)
        self.show = []
        for n in ran:
            if 1 <= ran[n] <= 5:
                self.show.append("8")
            if 6 <= ran[n] <= 15:
                self.show.append("7")
            if 16 <= ran[n] <= 30:
                self.show.append("6")
            if 31 <= ran[n] <= 50:
                self.show.append("5")
            if 51 <= ran[n] <= 120:
                self.show.append("4")
            if 121 <= ran[n] <= 180:
                self.show.append("3")
            if 181 <= ran[n] <= 253:
                self.show.append("2")
            if 254 <= ran[n] <= 334:
                self.show.append("1")
                
    def check(self):
        if self.show[0] == self.show[3] == self.show[6]:
            pygame.draw.line(self.screen, [246, 226, 0], (36, 111), (423, 111), 8)
            self.wins[0] = self.show[0]
        if self.show[1] == self.show[4] == self.show[7]:
            pygame.draw.line(self.screen, [246, 226, 0], (36, 239), (423, 239), 8)
            self.wins[1] = self.show[1]
        if self.show[2] == self.show[5] == self.show[8]:
            pygame.draw.line(self.screen, [246, 226, 0], (36, 367), (423, 367), 8)
            self.wins[2] = self.show[2]
        if self.show[0] == self.show[4] == self.show[8]:
            pygame.draw.line(self.screen, [246, 226, 0], (37, 47), (422, 433), 8)
            self.wins[3] = self.show[0]
        if self.show[2] == self.show[4] == self.show[6]:
            pygame.draw.line(self.screen, [246, 226, 0], (37, 432), (422, 47), 8)
            self.wins[4] = self.show[2]
            
    def winner(self):
        self.lastwin = 0
        for n in self.wins:
            winsu = self.bet*int(n)
            winsum = winsu + self.bet
            if winsum > self.bet:
                self.credit = self.credit + winsum
                self.lastwin = self.lastwin + winsum
                self.beepsound.play()
            
    def helpmenu(self):
        pygame.draw.line(self.screen, [176, 176, 176], (50, 250), (590, 250), 400)
        font = pygame.font.Font("data/LiberationSans-Regular.ttf", 15)
        text_surface = font.render("How to play:", True, [255, 255, 255])
        self.screen.blit(text_surface, (60, 60))
        text_surface = font.render("New spin: left arrow", True, [255, 255, 255])
        self.screen.blit(text_surface, (60, 80))
        text_surface = font.render("Raise bet: arrow up", True, [255, 255, 255])
        self.screen.blit(text_surface, (60, 100))
        text_surface = font.render("To end game to high score press Enter", True, [255, 255, 255])
        self.screen.blit(text_surface, (60, 120))
        text_surface = font.render("To close this as game over help press F1", True, [255, 255, 255])
        self.screen.blit(text_surface, (60, 160))
        
    def endthegame(self, scr):
        scrb = int(scr)
        pygame.draw.line(self.screen, [176, 176, 176], (50, 250), (590, 250), 400)
        if self.credit > scrb:
            font = pygame.font.Font("data/LiberationSans-Regular.ttf", 15)
            text_surface = font.render("You have a new high score!!!", True, [255, 255, 255])
            self.screen.blit(text_surface, (60, 60))
            text_surface = font.render("Old high score: "+scr, True, [255, 255, 255])
            self.screen.blit(text_surface, (60, 80))
            text_surface = font.render("New high score: "+str(self.credit), True, [255, 255, 255])
            self.screen.blit(text_surface, (60, 100))
            self.writehs(myhsfile)
        else:
            font = pygame.font.Font("data/LiberationSans-Regular.ttf", 15)
            text_surface = font.render("You ended the game, but you don't have a new high score...", True, [255, 255, 255])
            self.screen.blit(text_surface, (60, 60))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.bgsound.stop()
                plc = Menu()
    
    def writehs(self, myhsfile):
        writef = open(myhsfile, "w")
        writef.write(str(self.credit))
        writef.close()
