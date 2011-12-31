#! /usr/bin/python
"""
PyPiPa - Python Pirate Party.
Copyright (C) 2010  launchpad.net/pypipa <pypipa@orakeldel.net>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
"""

import pygame
from pygame.locals import *

class WidgetMenu (object):
  """
  All widget classes (Menu, Games, Controls,...) have to derivate this class.
  """
  menu_x = []
  menu_y = []

  font_size = []
  
  def define_screen (self, screen):
    self.screen = screen
    
    self.states = ("NewGame", "Multiplayer", "Highscores", "Settings", "About", "Exit")
    self.state_titles = ("New Game", "Multiplayer", "Highscores", "Settings", "About", "Exit")
    self.state_text = []
    self.state_position = []
    self.current = 0
    self.last_current = self.current

    self.current_selected = 0
    self.last_current = self.current_selected

    self.screen_width = self.screen.get_width()
    self.screen_height = self.screen.get_height()

    self.menu_x = self.screen_width/2.5
    self.menu_y = self.screen_height/4 

    self.new_saber_size = self.screen_height/15
    self.saber = pygame.image.load("data/saber.png")
    self.saberrect = self.saber.get_rect()
    self.smallsaber = pygame.transform.scale(self.saber, (int(self.saberrect.right*(self.screen_height/900.0)), int(self.saberrect.bottom*(self.screen_height/900.0))))

    self.font_size = self.screen_height/15
    self.font = pygame.font.Font("data/primitive.ttf", self.font_size)
    
    for i in range(0,6):
        self.state_text.append(self.font.render(self.state_titles[i], True, (200, 200, 200)))

        cur_x = self.menu_x
        cur_y = self.menu_y
        menu_pos = [cur_x, cur_y]
        self.state_position.append(menu_pos)

        self.screen.blit(self.state_text[i], menu_pos)
        self.menu_y = cur_y + (self.font_size*1.5)

    self.saber_x = (self.state_position[0][0]-self.smallsaber.get_width()-(self.screen_height/30))
    self.saber_y = self.state_position[0][1]
    #self.screen.blit(self.smallsaber,(self.state_position[0][0]-self.smallsaber.get_width()-(screen_height/30), self.state_position[0][1]))
    self.draw_stuff()
    
  
  def draw_stuff(self):
    self.screen.fill((0,0,0,255))
    for i in range(0,6):
      self.state_text.append(self.font.render(self.state_titles[i], True, (200, 200, 200)))

      self.screen.blit(self.state_text[i], (self.state_position[i][0], self.state_position[i][1]))
      pygame.display.flip()
    self.screen.blit(self.smallsaber, (self.saber_x, self.saber_y))
    
    pygame.display.flip()
  
  def get_surface (self):
    """
    Draws the widget on the screen
    @type screen: pygame.Surface
    @param screen: Surface to paint uppon
    """

    pygame.display.flip()
    return self.screen

  def manage_interaction (self, key):
    """
    Manages interaction with the widgets (f.e. cursor key up pressed,...)
    """
    """
    for e in pygame.event.get():
      if e.type == QUIT:
        pygame.quit()
        return False
      if e.type == KEYDOWN:
	if e.key == K_UP:
          self.selectPrev()
        if e.key == K_DOWN:
          self.selectNext()"""
    if key == K_UP:
      self.selectPrev()
    if key == K_DOWN:
      self.selectNext()
        
    self.draw_stuff()
    if key == K_RETURN:
      return self.get_state()
      
    return True
	  
  def selectPrev (self):
    self.last_current = self.current
    self.current = max ( (0, self.current-1) )
    self.saber_x=(self.state_position[self.current][0]-self.smallsaber.get_width()-(self.screen_height/30))
    self.saber_y=self.state_position[self.current][1]
    #print self.state_position[(self.current)][1]
    #self.screen.blit(self.smallsaber,(self.state_position[self.current][0]-self.smallsaber.get_width()-(self.screen_height/30), self.state_position[self.current][1]))
    #self.state_text[ self.last_current ] = self.font.render( self.state_titles[ self.last_current ], True, (200, 200, 200) )
    #self.state_text[ self.current ] = self.font.render( self.state_titles[ self.current ], True, (150, 100, 100) )
	  
  def selectNext (self):
    self.last_current = self.current
    self.current = min ( (self.current+1, len( self.states ) - 1) )
    self.saber_x=(self.state_position[self.current][0]-self.smallsaber.get_width()-(self.screen_height/30))
    self.saber_y=self.state_position[self.current][1]
    #print self.state_position[(self.current)][1]
    #self.screen.blit(self.smallsaber,(self.state_position[self.current][0]-self.smallsaber.get_width()-(self.screen_height/30), self.state_position[self.current][1]))
    #self.state_text[ self.last_current ] = self.font.render( self.state_titles[ self.last_current ], True, (200, 200, 200) )
    #self.state_text[ self.current ] = self.font.render( self.state_titles[ self.current ], True, (150, 100, 100) )
    
  def get_state (self):
    if self.current == 5:
      return False
    elif self.current == 0:
      return "widget.WidgetNewGame"
    else:
      return True