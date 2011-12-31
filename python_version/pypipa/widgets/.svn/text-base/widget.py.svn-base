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

class Widget (object):
  """
  All widget classes (Menu, Games, Controls,...) have to derivate this class.
  """
    
  def get_surface (self, screen):
    """
    Draws the widget on the screen
    @type screen: pygame.Surface
    @param screen: Surface to paint uppon
    """
    raise NotImplementedError( "ERROR: Module " + self.__class__.__name__ + " hasn't implemented the draw() function." )
    
  def manage_interaction (self):
    """
    Manages interaction with the widgets (f.e. cursor key up pressed,...)
    """
    raise NotImplementedError( "ERROR: Module " + self.__class__.__name__ + " hasn't implemented the manage_interaction() function." )