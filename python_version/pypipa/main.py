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
import os
import widgets_master as wm
widgets = __import__("widgets", globals(), locals(), ['WidgetMenu'], -1)


def set_icon (iconname):
  """
  Sets the icon of the window.
  @type iconname: string
  @param iconname: the filename of the iconfile (64x64 pixels) ff00ff = Transparent
  """
  icon = pygame.Surface ((64,64))
  icon.set_colorkey ((255,0,255))#and call that color transparant
  rawicon = pygame.image.load (iconname)#must be 32x32, black is transparant
  for i in range (0,64):
      for j in range (0,64):
          icon.set_at ((i,j), rawicon.get_at ((i,j)))
  pygame.display.set_icon (icon)


def main ():
  os.environ[ "SDL_VIDEO_CENTERED" ] = "1"
  pygame.init()
  pygame.display.set_caption ("PyPiPa - Python Pirate Party")
  set_icon ("data/logo_64x64.png")
  screen = pygame.display.set_mode ((800, 600)) # Make this variable
  widget_menu = widgets.WidgetMenu()
  #widget_menu2 = widgets.WidgetMenu()
  #widget_menu3 = widgets.WidgetMenu()
  #widgets_master = wm.WidgetsMaster(screen, 3, [widget_menu,widget_menu2,widget_menu3])
  widgets_master = wm.WidgetsMaster(screen, 1, [widget_menu])
  reaction = True
  while reaction:
    reaction = widgets_master.manage_interaction()
    widgets_master.draw()
    if isinstance(reaction, str):
      #widget_master = wm.
      #TODO start module reaction
      #widgets_master.set_widgets()    
      reaction = True
    pygame.time.delay(50) #Sleeps

if __name__ == "__main__":
  main()