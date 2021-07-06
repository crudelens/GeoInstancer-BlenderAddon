import bmesh
import bpy

global objectlist
objectlist=[]
class Main_OT_Geometry(bpy.types.Operator):
    bl_idname = "maingeoselect.create"
    bl_label = "Execute Instancing"

    def __init__(self):
        ps = None
        self.ps=ps

    def execute(self, context):

        scene = context.scene.your_properties
        Obj1= scene.SelectedMainGeo
        Obj2= scene.SelectedInstancedGeo
        ob = Obj1
        for o in bpy.data.collections:
            if o.name=="GeoInstancer":
                continue    
            else:
                Col2=bpy.data.collections.new("GeoInstancer")
                break
        if scene.SelectCustomGeo:
            bpy.data.collections["GeoInstancer"].objects.link(Obj2)
        if scene.Cubeselect:
            bpy.ops.mesh.primitive_cube_add()
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (5,5,0)
            objectlist.append(bpy.context.object.name)
        if scene.UVSpherselect:
            bpy.ops.mesh.primitive_uv_sphere_add()
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (6,5,0)
            objectlist.append(bpy.context.object.name)
        if scene.ICOselect:
            bpy.ops.mesh.primitive_ico_sphere_add()
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (7,5,0)
            objectlist.append(bpy.context.object.name)
        if scene.Planeselect:
            bpy.ops.mesh.primitive_plane_add()
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (8,5,0)
            objectlist.append(bpy.context.object.name)
        if scene.Cylinderselect:
            bpy.ops.mesh.primitive_cylinder_add()
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (9,5,0)
            objectlist.append(bpy.context.object.name)
        if scene.Coneselect:
            bpy.ops.mesh.primitive_cone_add()
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (10,5,0)
            objectlist.append(bpy.context.object.name)
        if scene.Torusselect:
            bpy.ops.mesh.primitive_torus_add()
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (11,5,0)
            objectlist.append(bpy.context.object.name)
        if scene.Monkeyselect:
            bpy.ops.mesh.primitive_monkey_add()
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (12,5,0)
            objectlist.append(bpy.context.object.name)
        if scene.Mballselect:
            bpy.ops.object.metaball_add(type='BALL')
            bpy.data.collections["GeoInstancer"].objects.link(bpy.context.object)
            bpy.data.objects[bpy.context.object.name].location = (13,5,0)
            objectlist.append(bpy.context.object.name)
        i = 0
        for modifier in ob.modifiers:
            if modifier.name=="instancing":
                i=1
                break
            else:
                continue
        if i==0:
            self.ps = ob.modifiers.new("instancing", 'PARTICLE_SYSTEM')
            self.ps.name='instancing'
            psys = ob.particle_systems[self.ps.name]
            psys.settings.type = 'HAIR'
            bpy.context.view_layer.objects.active = ob
            me = bpy.context.object.data
            # Get a BMesh representation
            bm = bmesh.new()   # create an empty BMesh
            bm.from_mesh(me)   # fill it in from a Mesh
            i = 0
            for v in bm.verts:
                i+=1
            psys.settings.count = i
            psys.settings.emit_from = 'VERT'
            psys.settings.use_emit_random = False
            psys.settings.render_type = 'COLLECTION'
            psys.settings.instance_collection= Col2
            psys.settings.use_advanced_hair = True
            psys.settings.use_rotations = True
            psys.settings.rotation_mode=scene.orientaxis
            psys.settings.rotation_factor_random = scene.rotation
            psys.settings.particle_size = scene.scale
            psys.settings.size_random = scene.scalerand
            psys.seed=scene.seed
            psys.settings.use_collection_pick_random = True
            print(scene.Emitter)
            ob.show_instancer_for_render = scene.Emitter
            ob.show_instancer_for_viewport = scene.Emitter
            if Obj2 is not None:
                Obj2.hide_render = True
        else:
            self.report({'WARNING'},"Reset instancing before creating a new instance on the object")
        return {'FINISHED'}
    
    def updatingsettings(self,context):
        scene = context.scene.your_properties
        Obj1= scene.SelectedMainGeo
        Obj2= scene.SelectedInstancedGeo
        ob = Obj1
        psys = ob.particle_systems['instancing']
        psys.settings.type = 'HAIR'
        bpy.context.view_layer.objects.active = ob
        psys.settings.rotation_mode= scene.orientaxis
        psys.settings.size_random = scene.scalerand
        psys.settings.rotation_factor_random = scene.rotation
        psys.settings.particle_size = scene.scale
        psys.seed=scene.seed
        ob.show_instancer_for_render = scene.Emitter
        ob.show_instancer_for_viewport = scene.Emitter


class Reset_OT_Geometry(bpy.types.Operator):
    bl_idname = "maingeoselect.reset"
    bl_label = "Reset Instancing"


    def execute(self, context):
        if bpy.context.object.mode == 'EDIT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')
        scene = context.scene.your_properties
        Obj1= scene.SelectedMainGeo
        for o in objectlist:
            bpy.data.objects[o].select_set(True, view_layer=context.scene.view_layers[0])
            bpy.ops.object.delete()
        bpy.context.view_layer.objects.active = Obj1
        Col2=bpy.data.collections.get("GeoInstancer")
        bpy.data.collections.remove(Col2)
        objectlist.clear()
        try:
            bpy.ops.object.particle_system_remove()
        except:
            None
        return {'FINISHED'}