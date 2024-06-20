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

"Agregar limite"
threshold = 0.65

while True:
    "Obtener el frame"
    frame_read = tello.get_frame_read()
    frame = frame_read.frame

    "Cambiar imagen a blanco y negro"
    img = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    "Leer el resultado del modelo"
    results = model.predict(img)[0]

    for result in results.boxes.data.tolist():
        x1,y1,x2,y2,score,class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),4)
            cv2.imwrite("picture.png",frame)

    cv2.imshow("DJI drone", frame)

    "Salir del programa"
    k = cv2.waitKey(30)
    if k == 27:
        tello.streamoff()
        break

cv2.destroyWindow()