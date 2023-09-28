import open3d as o3d
import os.path
file_path = os.path.join(os.path.dirname(__file__), "../resource/models/french_bulldog.obj")
#(os.path.dirname(__file__)で現在実行中の.pyファイルがあるディレクトリを参照する
if(os.path.exists(file_path)):
    print("Testing IO for mesh ...")
    #四角形メッシュは未対応のためdog.objは読み込みに失敗する
    Mesh_load = o3d.io.read_triangle_mesh(file_path)
    Mesh_load.compute_vertex_normals()

    # Visualization in window
    o3d.visualization.draw_geometries([Mesh_load],mesh_show_back_face=True)
else:
    print("no such file")
    print("current:", os.path.dirname(__file__))