"""
Add-on Preferences (Edit > Preferences > Add-ons > AI Base-Mesh & Rig Generator).

Stores the user's LLM provider choice and API key inside Blender's local
preferences so secrets are never hard-coded into the Python files or committed to Git.
"""

import bpy

# In Blender 4.2+ / 5.0 Extensions, referencing the root package via relative import
# ensures bl_idname always matches the extension's registered package ID.
from . import __package__ as base_package


class AIRigPreferences(bpy.types.AddonPreferences):
    bl_idname = base_package

    provider: bpy.props.EnumProperty(
        name="LLM Provider",
        description="Select which AI service will interpret character prompts (Milestone 4)",
        items=[
            ('GEMINI', "Google Gemini", "Use the Google Gemini API (free tier)"),
            ('OPENAI_COMPAT', "OpenAI-Compatible / Ollama", "Use a local or compatible endpoint"),
        ],
        default='GEMINI',
    )

    api_key: bpy.props.StringProperty(
        name="API Key",
        description="Stored locally by Blender; never hard-coded or printed to the console",
        default="",
        subtype='PASSWORD',
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "provider")
        layout.prop(self, "api_key")
        layout.label(
            text="Milestone 1 skeleton: network calls will be added in Milestone 4.",
            icon='INFO',
        )


def register():
    bpy.utils.register_class(AIRigPreferences)


def unregister():
    bpy.utils.unregister_class(AIRigPreferences)
