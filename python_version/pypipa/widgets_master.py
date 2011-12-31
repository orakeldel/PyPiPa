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
widgets = __import__("widgets.widget_menu", globals(), locals(), ['WidgetMenu'], -1)

class WidgetsMaster (object):
  """
  The WidgetsMaster handles 1-4 widgets on the screen. Widgets may be games or 
  control elements. The widgets are orderd the following:
  1:|-----|  2:|-----|  3:|-----|  4:|-----|
    |#####|    |##|##|    |##|##|    |##|##|
    |#####|    |##|##|    |-----|    |-----|
    |#####|    |##|##|    |#####|    |##|##|
    |-----|    |-----|    |-----|    |-----|
  In case of 2 players, there will be one widgetmaster each:
  1:|-------| 2:|-------| 3:|--------| 4:|-------|
    |#######|   |###|###|   |##|##|##|   |#|#|#|#|
    |-------|   |-------|   |--------|   |-------|
  """
  def __init__ (self, screen, widgets_count = 1, widgets = None, is_multiplayer = False):
    """
    Constructor of WidgetsMaster
    @type screen: pygame.Surface
    @param screen: Surface to paint uppon
    @type widgets_count: int
    @param widgets_count: numbers of widgets to draw (default: 1)
    @type widgets: array
    @param widgets: array of widgets to use (size has to >= widgets_count), None to define later using set_widgets() (defualt: None)
    @type is_multiplayer: bool
    @param is_multiplayer: shall screen tile like multiplayer mode (defualt: false)
    """
    self.screen = screen
    
    self.widgets_count = widgets_count;
    if self.widgets_count > 4:
      print ("ERROR: Widgets_count greater than 4: Resetting to 4.")
      self.widgets_count = 4;
    
    self.widgets = widgets
    
    self.is_multiplayer = is_multiplayer;
    self.create_screen_parts()
      
    i = 0
    for widget in self.widgets:
      widget.define_screen(self.screenparts[i])
      i+=1

  def change_widgets_count (self, new_widgets_count):
    """
    Changes the number of widgets
    @type new_widgets_count: int
    @param new_widgets_count: numbers of widgets to draw
    """
    if new_widgets_count > 4:
      print ("ERROR: new_widgets_count greater than 4: Resetting to 4.")
    else:
      self.widgets_count = new_widgets_count
    
  def set_widgets (self, widget, widget_index = 0):
    """
    Sets the widgets to draw
    @type widget: widget
    @param widget: widget to be changed to
    @type widget_index: int
    @param widget_index: index of the widget to change (default: 0)
    """
    if widget_index < len(self.widgets):
      self.widgets[widget_index] = widget
    
  def draw (self):
    """
    Draws the widget on the screen
    """    
    i = 0
    for widget in self.widgets:
      if i < 2:
        self.screen.blit(widget.get_surface(), (i*self.screen.get_width()/2,0))
      else:
        self.screen.blit(widget.get_surface(), ((i % 2)*self.screen.get_width()/2, self.screen.get_height()/2))
      i+=1
    
  def manage_interaction (self):
    """
    Manages interaction with the widgets (f.e. cursor key up pressed,...)
    """
    reactions = []
    for e in pygame.event.get():
      if e.type == QUIT:
        pygame.quit()
        return False
      if e.type == KEYDOWN:
        for widget in self.widgets:
          reactions.append(widget.manage_interaction(e.key))
    
        if isinstance(self.widgets[0], widgets.WidgetMenu):
          return reactions[0];
        #TODO: Possibility of message return from modules
        reaction = True
        for react in reactions:
          if react == False:        
            reaction = "widgets.WidgetMenu"
        return reaction
    return True
  
  def create_screen_parts (self):
    """
    makes all needed screenparts
    """
    self.screenparts = [];
    if self.widgets_count == 1: 
      self.screenparts.append(pygame.Surface((self.screen.get_width(),self.screen.get_height())))
    elif self.widgets_count == 2:
      for i in range (0,2):
        self.screenparts.append(pygame.Surface(((self.screen.get_width()/2),self.screen.get_height())))
    elif self.widgets_count == 3: 
      for i in range (0,2):
        self.screenparts.append(pygame.Surface(((self.screen.get_width()/2),(self.screen.get_height()/2))))
      self.screenparts.append(pygame.Surface((self.screen.get_width(),(self.screen.get_height()/2))))
    elif self.widgets_count == 4: 
      for i in range (0,4):
        self.screenparts.append(pygame.Surface(((self.screen.get_width()/2),(self.screen.get_height()/2))))
    else:
      print ("ERROR: widgets_count is neither 1,2,3 nor 4.")
      
    
    #TODO: 2 players
    pass
