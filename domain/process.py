import os
from PIL import Image
import array as np
pngs=[]
labels=[]
count = 0
for filename in os.listdir("./pymol/"):
    if filename.endswith(".png"):
        img = Image.open("./pymol/"+filename)
        arr = np.array(img)
        pngs.append(arr)
        labels.append(int(filename[0]))

labels=np.array(labels)

def OneHot(T):
    targetType=list(set(T.flatten()))
    oneHotT=np.zeros((T.shape[0]), len(targetType))
    for i in range(T.shape[0]):
        oneHotT[i,int(T[i])]=1
    return oneHotT
    
x_train=np.array(png)
t_train=OneHot(labels)

