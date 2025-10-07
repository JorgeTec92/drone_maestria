import cv2

nuevo_tamano = (640, 320)

for i in range(1,2089):
    imagen = cv2.imread("D:/Maestria/Imagenes para dataset/data/images/validation/"f'DJI_{i}.jpg')
    imagen_reducida = cv2.resize(imagen, nuevo_tamano, interpolation = cv2.INTER_LINEAR)
    cv2.imwrite("D:/Maestria/Imagenes para dataset/data3/images/validation/"f'DJI_{i}.jpg', imagen_reducida)
    print("imagen redudica",i)