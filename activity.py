import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import StopButton, ActivityToolbarButton
import sugargame.canvas
import sugargame.event
from ball_up_game import BallUpGame

class BallUpActivity(activity.Activity):
    def __init__(self, handle):
        super(BallUpActivity, self).__init__(handle)

        # Set up the toolbar
        toolbar_box = ToolbarBox()
        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        # Create the Pygame canvas
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self)
        self.set_canvas(self._pygamecanvas)

        # Create an instance of the game
        self.game = BallUpGame()

        # Start the Pygame main loop
        self._pygamecanvas.run_pygame(self.game.run)

    def read_file(self, file_path):
        pass  # Implement loading functionality if needed

    def write_file(self, file_path):
        pass  # Implement saving functionality if needed