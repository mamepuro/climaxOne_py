import open3d as o3d
import os.path
#import matplotlib.pyplot as plt
#import matplotlib.patches as pat

file_path = os.path.join(os.path.dirname(
    __file__), "../resource/models/french_bulldog.obj")
txt_file_path = os.path.join(os.path.dirname(
    __file__), "../resource/models/doggo.obj")
txt_middle_file_path = os.path.join(os.path.dirname(
    __file__), "../resource/models/doggo_face.txt")


# patches.Rectangleクラスのインスタンスを作成

# 左下の座標(0.3, 0.3), 横幅0.5, 高さ0.25
# 回転角0°, 塗り潰し色blue, 透明度0.5
# rec1 = pat.Rectangle(xy=(0.3, 0.3), width=0.5, height=0.25,
#                     angle=0, color="blue", alpha=0.5)

# 左下の座標(0.3, 0.3), 横幅0.5, 高さ0.25
# 回転角45°, 塗り潰し色red, 透明度0.5
# rec2 = pat.Rectangle(xy=(0.3, 0.3), width=0.5, height=0.25,
#                     angle=45, color="red", alpha=0.5)

# Axesに長方形を追加
# ax.add_patch(rec1)
# ax.add_patch(rec2)
# ax.set_xlim([-0.1, 0.1])
# ax.set_ylim([-0.1, 0.1])
# plt.savefig(os.path.join(os.path.dirname(__file__), "../resource/images/dog1.png"))
#fig.show()
# (os.path.dirname(__file__)で現在実行中の.pyファイルがあるディレクトリを参照する
if (os.path.exists(file_path)):
    print("Testing IO for mesh ...")
    # 四角形メッシュは未対応のためdog.objは読み込みに失敗する
    Mesh_load = o3d.io.read_triangle_mesh(file_path)
    Mesh_load.compute_vertex_normals()

    # Visualization in window
    o3d.visualization.draw_geometries([Mesh_load], mesh_show_back_face=True)
else:
    print("no such file")
    print("current:", os.path.dirname(__file__))
input()
