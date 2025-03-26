import cv2
import matplotlib.pyplot as plt

image = cv2.imread('example.png')

roi = image[0:100, 0:100]
height,width, _ = image.shape
roi = image[int(height/2):height,: ]
roi = image[:,int(width/2):width ]
print("podaj 4 wartosci startx, endx , starty, endy")
#startx=input()
#endx=input()
#starty=input()
#endy=input()
#roi = image[startx:endx, starty:endy]
image2 = cv2.imread('face.jpeg')
roi = image2[20:600, 300:730]

roi = image[0:100,0:100]
image[height-100:height, width-100:width] = roi
#plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

part_height = height // 3
part_width = width // 3

parts = []

for i in range(3):
    for j in range(3):
        part = image[i * part_height:(i + 1) * part_height, j * part_width:(j + 1) * part_width]
        parts.append(part)

fig, axs = plt.subplots(3, 3, figsize=(10, 10))
axs = axs.ravel()

for i in range(9):
        plt.imshow(cv2.cvtColor(parts[i], cv2.COLOR_BGR2RGB))  # Konwersja BGR -> RGB
        plt.axis('off')  # Ukrycie osi
        plt.title(f'Part {i+1}')  # Dodanie tytułu
        #plt.show()
image = cv2.imread('example.png')
roi = image[0:100, 0:100]

plt.close()
# for i in range(0,101,10):
#     roi=image[0+i:100+i,0+i:100+i]
#     plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
#     plt.axis('off')
#     plt.title(f"ROI at position {i}")
#     plt.draw()
#     key = cv2.waitKey(0)
#     plt.show()

image = cv2.imread('example.png')
roi = image[0:100, 0:100]
cv2.imwrite('output_roi.png', roi)
plt.imshow(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
plt.show()
