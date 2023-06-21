import os
import cv2


path = "C:/Users/luiza/Downloads/PRO_1-1_C105_AtividadeDoAluno1-main.zip/PRO_1-1_C105_AtividadeDoAluno1-main/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)


fdv = cv2.imread(images [0])

height, width, c = fdv.shape
size = (width, height)
video = cv2.videoWriter("pds.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 2, size)

for i in range(count -1, 0, -1) : 
    fdv = cv2.imread(images [i])
    video.write(fdv)

video.release()