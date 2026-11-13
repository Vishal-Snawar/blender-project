"""
User interface for Milestone 1:
- AIRigProperties:     Stores panel input values on each Blender Scene.
- AIRIG_OT_generate:   Operator called when the user clicks the Generate button.
- AIRIG_PT_main_panel: Sidebar panel (N-panel) in the 3D Viewport under the 'AI Rig' tab.
"""

import bpy


class AIRigProperties(bpy.types.PropertyGroup):
    """Scene-level properties bound to the AI Rig sidebar panel."""

    prompt: bpy.props.StringProperty(
        name="Prompt",
        description="Describe the character or creature you want to generate",
        default="tall slim elf with long legs",
    )

    template: bpy.props.EnumProperty(
        name="Template",
        description="Choose a body template or let the AI detect it from the prompt",
        items=[
            ('AUTO', "Auto (from prompt)", "Detect humanoid or quadruped from the prompt"),
            ('HUMANOID', "Humanoid", "Two-legged humanoid base mesh and rig"),
            ('QUADRUPED', "Quadruped", "Four-legged creature base mesh and rig"),
        ],
        default='AUTO',
    )

    generate_rig: bpy.props.BoolProperty(
        name="Generate Rig",
        description="Create a matching armature and bind the mesh with automatic weights",
        default=True,
    )

    apply_modifiers: bpy.props.BoolProperty(
        name="Apply Modifiers",
        description="Apply Skin and Subdivision modifiers to produce an editable mesh",
        default=True,
    )

    status_message: bpy.props.StringProperty(
        name="Status",
        description="Latest status message from the add-on",
        default="Ready (Milestone 1 skeleton)",
    )


class AIRIG_OT_generate(bpy.types.Operator):
    """Test operator for Milestone 1: prints a message to Blender's System Console."""

    bl_idname = "airig.generate"
    bl_label = "Generate"
    bl_description = "Milestone 1 test: prints the current panel settings to the System Console"
    bl_options = {'REGISTER'}

    def execute(self, context):
        props = context.scene.ai_rig_props

        # Print to Blender's System Console (never print API keys!)
        print(
            "[AI Rig] Milestone 1 button clicked! "
            f"Prompt='{props.prompt}', Template='{props.template}', "
            f"GenerateRig={props.generate_rig}, ApplyModifiers={props.apply_modifiers}"
        )

        # Update the panel's status line and notify in Blender's bottom status bar
        props.status_message = "Done: printed test message to System Console."
        self.report({'INFO'}, "AI Rig (Milestone 1): Check System Console for output.")
        return {'FINISHED'}


class AIRIG_PT_main_panel(bpy.types.Panel):
    """3D Viewport Sidebar (N-panel) tab named 'AI Rig'."""

    bl_label = "AI Base-Mesh & Rig"
    bl_idname = "AIRIG_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "AI Rig"

    def draw(self, context):
        layout = self.layout
        props = context.scene.ai_rig_props

        # Input controls
        layout.prop(props, "prompt")
        layout.prop(props, "template")

        row = layout.row()
        row.prop(props, "generate_rig")
        row.prop(props, "apply_modifiers")

        layout.separator()

        # Action button
        layout.operator("airig.generate", icon='PLAY')

        layout.separator()

        # Status line
        box = layout.box()
        box.label(text=f"Status: {props.status_message}")


classes = (
    AIRigProperties,
    AIRIG_OT_generate,
    AIRIG_PT_main_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.ai_rig_props = bpy.props.PointerProperty(type=AIRigProperties)


def unregister():
    if hasattr(bpy.types.Scene, "ai_rig_props"):
        del bpy.types.Scene.ai_rig_props
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
