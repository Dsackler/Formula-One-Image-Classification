import cv2
import matplotlib.pyplot as plt

img = cv2.imread('test_images/_4 Lando Norris.jpg')
print(img.shape)
plt.imshow(img)
plt.show()

