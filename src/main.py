import open3d as o3d
import os.path
import matplotlib.pyplot as plt
import matplotlib.patches as pat

file_path = os.path.join(os.path.dirname(
    __file__), "../resource/models/french_bulldog.obj")
txt_file_path = os.path.join(os.path.dirname(
    __file__), "../resource/models/dog.obj")
ZCoordinate_list = []
vertices = []
m_count = 0
rec_count = 0
# 最初の頂点かどうか
isFirstPoint = True
# 最初の頂点が何行目に配置されているか
firstPointLineNumber = 0
fig = plt.figure(figsize=(5, 5))

# FigureにAxes(サブプロット)を追加
ax = fig.add_subplot(111)
with open(txt_file_path) as f:
    # 一行ずつ最後まで読み込む
    for line in f:
        # 行数を+1カウント
        m_count += 1
        contents = line.split()
        if (contents[0] == 'v'):
            # blenderではボクセルはy軸方向に縦に並べている
            # y軸で切る
            if (isFirstPoint):
                firstPointLineNumber = m_count
                isFirstPoint = False
            if (contents[2] not in ZCoordinate_list):
                ZCoordinate_list.append(contents[2])
            # 頂点データを格納
            vertices.append([contents[1], contents[2], contents[3]])
        ZCoordinate_list.sort()
        if (contents[0] == 'f'):
            # 面を構成する1頂点を取り出す
            indexNum = int(contents[1].split('//')[0])
            if (vertices[indexNum-1][1] == ZCoordinate_list[0]):
                point0 = vertices[int(contents[1].split('//')[0]) - 1]
                point1 = vertices[int(contents[2].split('//')[0]) - 1]
                point2 = vertices[int(contents[3].split('//')[0]) - 1]
                point3 = vertices[int(contents[4].split('//')[0]) - 1]
                points = [point0[0], point0[2]], [point1[0], point1[2]], [
                    point2[0], point2[2]], [point3[0], point3[2]]
                rec = pat.Polygon(xy=points, color="blue", alpha=0.5)
                ax.add_patch(rec)
                rec_count += 1

    print("DEBUG LOG: ボクセルモデルは縦に頂点が", len(ZCoordinate_list), "個並んでます")
    print("DEBUG LOG: 一番下の超点数は", rec_count, "個並んでます")
# z座標を昇順で格納し直す


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
fig.show()
# (os.path.dirname(__file__)で現在実行中の.pyファイルがあるディレクトリを参照する
if (os.path.exists(file_path)):
    print("Testing IO for mesh ...")
    # 四角形メッシュは未対応のためdog.objは読み込みに失敗する
    Mesh_load = o3d.io.read_triangle_mesh(file_path)
    Mesh_load.compute_vertex_normals()

    # Visualization in window
    # o3d.visualization.draw_geometries([Mesh_load], mesh_show_back_face=True)
else:
    print("no such file")
    print("current:", os.path.dirname(__file__))
input()
