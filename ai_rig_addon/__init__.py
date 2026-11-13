"""
Entry point for the AI Base-Mesh & Rig Generator add-on (Milestone 1).

Blender calls:
- register()   when the user enables the add-on in Preferences.
- unregister() when the user disables the add-on in Preferences.
"""

if "bpy" in locals():
    import importlib

    importlib.reload(preferences)
    importlib.reload(ui)

import bpy

from . import preferences
from . import ui


def register():
    """Register add-on preferences, scene properties, operators, and UI panels."""
    preferences.register()
    ui.register()


def unregister():
    """Unregister everything in reverse order so disabling leaves no leftover data."""
    ui.unregister()
    preferences.unregister()


if __name__ == "__main__":
    register()
