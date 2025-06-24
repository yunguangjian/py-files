# -*- coding: utf-8 -*-
from pyautocad import Autocad, APoint

# 连接及库导入
acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello! Autocad from Python.")
# print(acad.doc.Name)
# Name = str(acad.doc.Name).split('.')[0]

# 获取所有面积线图层下的多段线
All_PolyLine = []

# 获取线
for line in acad.iter_objects('Line'):
    All_PolyLine.append(['线',line.Layer,line.Color,line.StartPoint,line.EndPoint])

# 获取多段线
for polyLine in acad.iter_objects('PolyLine'):
    All_PolyLine.append(['多段线',polyLine.Layer,polyLine.Area,polyLine.Color])

# 获取样条曲线
for spline in acad.iter_objects('Spline'):
    All_PolyLine.append(['样条曲线',spline.Layer,spline.Area,spline.Color])

# 获取圆
for circle in acad.iter_objects('Circle'):
    All_PolyLine.append(['圆',circle.Layer,circle.Area,circle.Color,circle.Center,circle.Radius])

# 获取圆弧
for arc in acad.iter_objects('Arc'):
    All_PolyLine.append(['圆弧',arc.Layer,arc.Area,arc.Color,arc.Center,arc.Radius])

# 获取椭圆
for ellipse in acad.iter_objects('Ellipse'):
    All_PolyLine.append(['椭圆',ellipse.Layer,ellipse.Area, ellipse.Color])

for item in All_PolyLine:
    print(item)