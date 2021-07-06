#Imports
import bpy

from .maingeoselector import Main_OT_Geometry
#Updating Live of Parameters
global updation
updation = Main_OT_Geometry.updatingsettings

from bpy.props import (EnumProperty, FloatProperty, IntProperty,
                       PointerProperty, BoolProperty)
from bpy.types import Operator, Panel, PropertyGroup

#Property Group
class addon_Properties(PropertyGroup):
    SelectedMainGeo : PointerProperty(
        type=bpy.types.Object
        )
    SelectedInstancedGeo : PointerProperty(
        type=bpy.types.Object
        )
#DropDown Menu
    orientaxis : EnumProperty(
        name="Orientation Axis",
        description="Rotation Type",
        items=[ ("OB_Z","Object Z",""),
        ("OB_Y","Object Y",""),
        ("OB_X","Object X",""),
        ("GLOB_Z","Global Z",""),
        ("GLOB_Y","Global Y",""),
        ("GLOB_X","Global X",""),
        ("VEL","Velocity / Hair",""),
        ("NOR_TAN","Normal-Tangent",""),
        ("NOR","Normal",""),
        ("NONE","None","")
        ],
        update=updation
    )
    rotation : FloatProperty(
        name = "Rotation Randomness",
        description = "Input Randomness of the Rotation",
        default = 0,
        min=0.0,
        max=1,
        step=1,
        precision=1,
        unit='NONE',
        update=updation,
        get=None,
        set=None
    )
    scale : FloatProperty(
        name = "Scale",
        description = "Input Scale of the Object",
        default = 0.05,
        soft_min = 0.02,
        soft_max = 1, 
        unit='NONE',
        update=updation,
        get=None,
        set=None
    )

    scalerand : FloatProperty(
        name = "Scale Randomness",
        description = "Input Randomness of the Scale",
        default = 0,
        min=0.0,
        max=1,
        step=1,
        precision=1,
        unit='NONE',
        update=updation,
        get=None,
        set=None
    )
    
    seed : IntProperty(
        name = "Seed",
        description = "Seed",
        min = 0,
        default = 1,
        update=updation
    )

    Emitter : BoolProperty(
        name="Show Emitter",
        description="Hide or Show Emitter",
        default = False,
        update=updation
    )

    SelectCustomGeo : BoolProperty(
        name="Select Custom Geometry",
        description="Enable Custom Geo",
        default = False,
        update=updation
    )
    Cubeselect : BoolProperty(
        name="Cube",
        description="Select Geo",
        default = False
    )
    UVSpherselect : BoolProperty(
        name="UV Sphere",
        description="Select Geo",
        default = False
    )
    ICOselect : BoolProperty(
        name="ICO Sphere",
        description="Select Geo",
        default = False
    )
    Cylinderselect : BoolProperty(
        name="Cylinder",
        description="Select Geo",
        default = False
    )
    Coneselect : BoolProperty(
        name="Cone",
        description="Select Geo",
        default = False
    )
    Torusselect : BoolProperty(
        name="Torus",
        description="Select Geo",
        default = False
    )
    Monkeyselect : BoolProperty(
        name="Monkey",
        description="Select Geo",
        default = False
    )
    Mballselect : BoolProperty(
        name="Metaball",
        description="Select Geo",
        default = False
    )
    Planeselect : BoolProperty(
        name="Plane",
        description="Select Geo",
        default = False
    )
    
    