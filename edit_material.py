import bpy
import random

####################
# material操作
####################


# 指定色でmaterialを作成する
def create_material(name, color):
    # materialの作成
    material = bpy.data.materials.new(name)
    # use_nodesをtrueに設定
    material.use_nodes = True
    # material情報を編集
    bsdf = material.node_tree.nodes["Principled BSDF"]
    bsdf.inputs[0].default_value = color  # color
    bsdf.inputs[4].default_value = 1      # metal
    bsdf.inputs[7].default_value = 0      # specular
    material.diffuse_color = color        # diffuseColor
    return material


# objectにmaterialを設定する
def set_material(in_material):
    for obj in bpy.data.objects:
        for slot in obj.material_slots:
            slot.material = in_material


if __name__ == "__main__":
    # ランダム色を定義
    _r = random.random()
    _g = random.random()
    _b = random.random()
    _color = (_r, _g, _b, 1)

    # materialを作成して設定する
    _material = create_material("RandomMaterial", _color)
    set_material(_material)
