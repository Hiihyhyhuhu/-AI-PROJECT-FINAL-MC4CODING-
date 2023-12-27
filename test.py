from deepface import DeepFace
import numpy as np
import pandas as pd
import os

os.remove("images/representations_vgg_face.pkl")
result = np.array(DeepFace.find(img_path = "style/sample_img.png", db_path = 'images', enforce_detection = False))
print(result)

# result = [things for items in result for things in items]
# print(result)
# result = result.reshape((-1,10))
# result = np.flip(result)
# similar_img, score = result[:10,0], result[:10,9]