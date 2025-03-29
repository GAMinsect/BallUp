from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import StopButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.style import GRID_CELL_SIZE

from gettext import gettext as _
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from sugargame import canvas
from game import BallGame

import pygame

class BallGameActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        
        # Create the game instance
        self.game = BallGame()
        
        # Build the activity toolbar
        self.build_toolbar()
        
        # Build the Pygame canvas and keep a reference to it
        self._pygamecanvas = canvas.PygameCanvas(self,
            main=self.game.run,
            modules=[pygame.display, pygame.font])
        
        # Set the focus to the canvas to capture key events
        self._pygamecanvas.set_can_focus(True)
        self._pygamecanvas.grab_focus()
        
        # Set the game's screen reference
        self.game.set_screen(self._pygamecanvas.get_surface())
        
        # Add the canvas to the activity's GTK grid
        self.set_canvas(self._pygamecanvas)
        
        # Connect to the destroy signal for proper cleanup
        self.connect("destroy", self._cleanup_cb)
        
        # Show everything
        self.show_all()
    
    def build_toolbar(self):
        # Create a new toolbar box
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()
        
        # Create an activity button
        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()
        
        # Add a restart button
        restart_button = ToolButton('view-refresh')
        restart_button.set_tooltip(_('Restart'))
        restart_button.connect('clicked', self._restart_button_cb)
        toolbar_box.toolbar.insert(restart_button, -1)
        restart_button.show()
        
        # Add a help button
        help_button = ToolButton('help-icon')
        help_button.set_tooltip(_('How to play'))
        help_button.connect('clicked', self._help_button_cb)
        toolbar_box.toolbar.insert(help_button, -1)
        help_button.show()
        
        # Add the stop button to the toolbar
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()
        
        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()
    
    def _restart_button_cb(self, button):
        """Restart the game"""
        # Reset ball position
        self.game.ball_y = self.game.HEIGHT - self.game.BALL_RADIUS
    
    def _help_button_cb(self, button):
        """Display a help dialog"""
        help_dialog = Gtk.MessageDialog(
            transient_for=self.get_toplevel(),
            modal=True,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text=_('Ball Game Help')
        )
        help_dialog.format_secondary_text(
            _('Press the space bar to make the ball jump up!')
        )
        help_dialog.run()
        help_dialog.destroy()
    
    def _cleanup_cb(self, widget):
        """Clean up pygame resources before closing"""
        self.game.cleanup()  # Call the cleanup method in our game
        
    def read_file(self, file_path):
        """Load the activity state"""
        pass
        
    def write_file(self, file_path):
        """Save the activity state"""
        pass
