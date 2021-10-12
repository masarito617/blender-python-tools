import bpy
import bmesh

####################
# オブジェクト情報出力
####################

# Object Info
print("*** Object Info ***")
print("Object Num " + str(len(bpy.data.objects)))
for o, obj in enumerate(bpy.data.objects):
    print("Object {0}, Name {1}, Type {2}".format(o, obj.name, obj.type))

# Mesh Info
print("\n*** Mesh Info ***")
for m, mesh in enumerate(bpy.data.meshes):
    print("Mesh {0}, Vertex Num {1}, Polygon Num {2}".format(m, len(mesh.vertices), len(mesh.polygons)))
    # 頂点座標
    for v, vertex in enumerate(mesh.vertices):
        print ("Vertex {0}, Vertex({1}, {2}, {3})".format(v, vertex.co.x, vertex.co.y, vertex.co.z))
    # インデックス座標(polygon.vertices)
    for p, polygon in enumerate(mesh.polygons):
        indices = ""
        for i, index in enumerate(polygon.vertices):
            indices += str(index) + ", "
        print("Polygon {0}, Index({1})".format(p, indices))
# Mesh Edge Info
for o, obj in enumerate(bpy.data.objects):
    if obj.type != "MESH":
        continue
    # オブジェクトをアクティブにしてEditModeに変更
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="EDIT")
    mesh = bmesh.from_edit_mesh(obj.data)
    print("Mesh {0}, Edge Num {1}".format(o, len(mesh.edges)))
# Modeを元に戻す
bpy.ops.object.mode_set(mode="OBJECT")

# Material Info
print("\n*** Material Info ***")
for m, material in enumerate(bpy.data.materials):
    print("Material {0}, Name {1}".format(m, material.name))
for o, obj in enumerate(bpy.data.objects):
    if obj.type != "MESH":
        continue
    for ms in obj.material_slots:
        name = "None"
        texture = "None"
        # material
        if not ms.material is None:
            name = ms.material.name
            # texture
            if ms.material.node_tree is not None:
                for node in ms.material.node_tree.nodes:
                    if node.type == "TEX_IMAGE":
                        texture = node.image.filepath
        print("Mesh {0}, MaterialSlot Name {1}, Texture Path {2}".format(o, name, texture))

# UV Info
print("\n*** UV Info ***")
for m, mesh in enumerate(bpy.data.meshes):
    for layer in mesh.uv_layers:
        for d, data in enumerate(mesh.uv_layers[layer.name].data):
            uv = ",".join([str(uv) for uv in data.uv])
            print("UV {0}, ({1})".format(d, uv))

# Bone Info
print("\n*** Bone Info ***")
for obj in bpy.data.objects:
    if obj.pose is None:
        continue
    # オブジェクトをアクティブにしてPoseModeに変更
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode="POSE")
    # 回転モードに合わせて取得
    for bone in obj.pose.bones:
        if "QUATERNION" in bone.rotation_mode:
            rot = bone.rotation_quaternion
        elif "AXIS_ANGLE" in bone.rotation_mode:
            rot = bone.rotation_axis_angle
        else:
            rot = bone.rotation_euler
        print("Bone Name {0}, {1}, {2}".format(bone.name, bone.location, rot))
# Modeを元に戻す
bpy.ops.object.mode_set(mode="OBJECT")

# Animation Info
print("\n*** Animation Info ***")
for obj in bpy.data.objects:
    # MESH、ARMATUREオブジェクトのみ対象
    if obj.type != "MESH" and obj.type != "ARMATURE":
        continue
    if obj.animation_data is None:
        continue
    print("Object Name {0}".format(obj.name))
    for fcurve in obj.animation_data.action.fcurves:
        for keypoint in fcurve.keyframe_points:
            frame = int(keypoint.co[0])
            vertex = keypoint.co[1]
            print("Animation Key {0}, {1}, {2}, {3}".format(fcurve.data_path, fcurve.array_index, frame, vertex))
