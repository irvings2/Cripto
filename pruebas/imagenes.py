import cv2

image = cv2.imread('img.bmp')

x = 240
y = 178

b = image.item(y, x, 0)
g = image.item(y, x, 1)
r = image.item(y, x, 2)

print(image.shape)

print('pixel:', b, g, r)