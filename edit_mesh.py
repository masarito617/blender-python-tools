import bpy

####################
# mesh操作
####################


# 新しくmeshを作成する
def create_mesh(name, vertices, indices):
    # objectの作成
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    # meshにpolygonを登録
    mesh.from_pydata(vertices, [], indices)
    mesh.update()


# meshを全て削除
def remove_all_meshes():
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)


if __name__ == "__main__":
    # 既存のmeshを削除
    remove_all_meshes()

    # 三角ポリゴンの作成
    _vertices = [(0, 0, 10), (10, 0, -10), (-10, 0, -10)]
    _indices = [(0, 1, 2)]
    create_mesh("NewMesh1", _vertices, _indices)

    # ピラミッドの作成
    _vertices = [(0, 0, 10), (10, 10, -10), (-10, 10, -10), (-10, -10, -10), (10, -10, -10)]
    _indices = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1), (4, 3, 2, 1)]
    create_mesh("NewMesh2", _vertices, _indices)
