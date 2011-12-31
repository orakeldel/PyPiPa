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

class WidgetNewGame (object):
  """
  All widget classes (Menu, Games, Controls,...) have to derivate this class.
  """
  
  def define_screen (self, screen):
    self.screen = screen
    self.screen.fill((255,0,0,255));
    
    
  
  def get_surface (self):
    """
    Draws the widget on the screen
    @type screen: pygame.Surface
    @param screen: Surface to paint uppon
    """

    self.screen.fill((255,0,0,255));
    pygame.display.flip()
    return self.screen

  def manage_interaction (self, key):
    """
    Manages interaction with the widgets (f.e. cursor key up pressed,...)
    """
    if key == K_RETURN:
      return False