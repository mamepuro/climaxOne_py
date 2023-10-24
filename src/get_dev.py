import open3d as o3d
import os.path
import numpy as np
import svgwrite
from svgwrite import cm, mm  
#import matplotlib.pyplot as plt
#import matplotlib.patches as pat

file_path = os.path.join(os.path.dirname(
    __file__), "../resource/models/french_bulldog.obj")
txt_file_path = os.path.join(os.path.dirname(
    __file__), "../resource/models/test.obj")
txt_middle_file_path = os.path.join(os.path.dirname(
    __file__), "../resource/models/test_i.txt")

ZCoordinate_list = []
vertices = []
m_count = 0
rec_count = 0
# 最初の頂点かどうか
isFirstPoint = True
# 最初の頂点が何行目に配置されているか
firstPointLineNumber = 0
with open(txt_file_path, encoding="utf-8") as f:
    # 一行ずつ最後まで読み込む
    with open(txt_middle_file_path, 'w', encoding="utf-8") as tf:
        for line in f:
            # 行数を+1カウント
            m_count += 1
            contents = line.split()
            if (contents[0] == 'v'):
                # 頂点データを格納
                vertices.append([contents[1], contents[2], contents[3]])
            if (contents[0] == 'f'):
                # 面を構成する1頂点を取り出す
                indexNum = int(contents[1].split('/')[0])
                if(len(contents) == 5):
                    tf.writelines(line)
            if(contents[0] == 'o'):
                tf.writelines(line)
        print("DEBUG LOG: ボクセルモデルは縦に頂点が", len(ZCoordinate_list), "個並んでます")
        print("DEBUG LOG: 一番下の超点数は", rec_count, "個並んでます")
    #四角形メッシュの個数
    rec_count = 0
    width_rec = 0
    height_rec = 0
    margin_w = 10
    margin_h = 10
    w = 0
    h = 0
    dwg = svgwrite.Drawing('test.svg', profile='tiny')
    with open(txt_middle_file_path) as tf:
        for line in tf:
            contents = line.split()
            if(contents[0] == 'o'):
                if(width_rec != 0):
                    if(width_rec >= height_rec):
                        w = height_rec * rec_count
                        h = width_rec
                    else:
                        w = width_rec * rec_count
                dwg.add(dwg.rect((margin_w, margin_h), (w,h)))
                dwg.add(dwg.text('Test', insert=(0, 0.2), fill='red'))
                rec_count = 0
                margin_h += margin_h
            else:
                faceNums = [0,0,0]
                for i in range(3):
                    faceNums[i] = int(contents[i+1].split('/')[0])
                print(faceNums)
                v0 = vertices[faceNums[0]-1]
                v2 = vertices[faceNums[1]-1]
                v1 = vertices[faceNums[2]-1]
                p0 = np.array([float(v0[0]), float(v0[1]), float(v0[2])])
                p1 = np.array([float(v1[0]), float(v1[1]), float(v1[2])])
                p2 = np.array([float(v2[0]), float(v2[1]), float(v2[2])])
                #print(np.subtract(p0, p1))
                width_rec = np.linalg.norm(p0 - p1)
                height_rec = np.linalg.norm(p1 - p2)
                #print(width_rec)
                #print(height_rec)
                rec_count += 1
        print("DEBUG LOG: 一番下の超点数は", rec_count, "個並んでます")
    dwg.save()  
    # plt.gca().clear()

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
