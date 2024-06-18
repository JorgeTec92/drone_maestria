"Importar librerías"
import cv2
from djitellopy import Tello
from ultralytics import YOLO

"Conectar drone"
tello = Tello()
tello.connect()

"Obtener el porcentaje de bateria"
print(tello.get_battery())

"Cargar el modelo YOLO"
model = YOLO("weights/best.pt")

"Iniciar el stream del video"
tello.streamoff()
tello.streamon()

while True:
    "Obtener el frame"
    frame_read = tello.get_frame_read()
    frame = frame_read.frame

    "Cambiar imagen a blanco y negro"
    img = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    "Leer el resultado del modelo"
    results = model.predict(img)
    anotacion = results[0].plot()

    "Mostrar imagen"
    cv2.imshow("frame", anotacion)

    "Salir del programa"
    k = cv2.waitKey(30)
    if k == 27:
        tello.streamoff()
        break

cv2.destroyWindow()