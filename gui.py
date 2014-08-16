# -*- coding: utf-8 -*-
"""
Insane Manager - gui.py
Copyright (C) 2014  Thomas Vanesse

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

from gi.repository import Gtk

class MainWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("glade/main_window.glade")

        # Main window
        self.main_window = self.builder.get_object("main_window")

        # The show must go on
        self.builder.connect_signals(MainWindowEventsHandler(self))
        self.main_window.show_all()


class MainWindowEventsHandler:

    def __init__(self, main_window):
        self.main_window = main_window

    def on_main_window_delete_event(self, *args):
        Gtk.main_quit(*args)



if __name__ == "__main__" :
    main_window = MainWindow()
    Gtk.main()