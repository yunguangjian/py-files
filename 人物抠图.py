# -*- coding: utf-8 -*-
import os
import paddlehub as hub

import paddlehub as hub
from pathlib import Path

img_dir = r"C:\Users\Administrator\Desktop\123"
save_dir = r"C:\Users\Administrator\Desktop\456"

inputs = [str(i) for i in Path(img_dir).glob('*.jpg')]

human_seg = hub.Module(name="deeplabv3p_xception65_humanseg")
results = human_seg.segmentation(paths=inputs, visualization=True, output_dir=save_dir)

print(results)