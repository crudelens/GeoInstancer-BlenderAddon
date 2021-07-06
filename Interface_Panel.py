#imports
import bpy
from bpy.props import FloatProperty, PointerProperty, StringProperty
from bpy.types import Operator, Panel, PropertyGroup

#Interfacecode
class Interface_PT_Panel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Geo Instancer"
    bl_idname = "Settings_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Instancing"

    def draw(self, context):
        #layout
        layout = self.layout
        scene=context.scene.your_properties

        col = layout.column()
        #Selecting Main Geo
        col.label(text="Select Main Geometry", icon='CUBE')
        col.prop(scene, "SelectedMainGeo",icon_only = True)
        col.label(text="Select Instanced Geometry", icon='SNAP_VERTEX')
        col = layout.column()
        row = layout.row()
        #Selecting Geo to be Instanced
        row.prop(scene, "Cubeselect", icon='CUBE',icon_only = True)
        row.prop(scene, "UVSpherselect", icon='MESH_UVSPHERE',icon_only = True)
        row.prop(scene, "ICOselect", icon='MESH_ICOSPHERE',icon_only = True)
        col = layout.column()
        row = layout.row()
        row.prop(scene, "Planeselect", icon='MESH_PLANE', icon_only = True)
        row.prop(scene, "Cylinderselect", icon='MESH_CYLINDER',icon_only = True)
        row.prop(scene, "Coneselect", icon='CONE',icon_only = True)
        col = layout.column()
        row = layout.row()
        row.prop(scene, "Torusselect", icon='MESH_TORUS',icon_only = True)
        row.prop(scene, "Monkeyselect", icon='MESH_MONKEY',icon_only = True)
        row.prop(scene, "Mballselect", icon='OUTLINER_OB_META',icon_only = True)
        col = layout.column()
        col.prop(scene, "SelectCustomGeo")
        #Bool for the Custom Geometry
        if scene.SelectCustomGeo:
            col.prop(scene, "SelectedInstancedGeo",icon_only = True)
        col = layout.column()
        box = layout.box()
        #Rotation parameters of Geometry
        box.label(text="Rotation", icon='CON_ROTLIKE')
        box.prop(scene, "orientaxis")
        box.prop(scene, "rotation",slider=True)
        col = layout.column()
        box = layout.box()
        #Scale parameters of Scale
        box.label(text="Scale", icon='CON_SIZELIKE')
        box.prop(scene, "scale")
        box.prop(scene, "scalerand", slider=True)
        #Other Parameters
        col = layout.column()
        col.prop(scene, "Emitter")
        col.prop(scene, "seed")
        #Operators
        col.operator("maingeoselect.create", icon = "PLAY")
        col.operator("maingeoselect.reset", icon = "TRASH")
