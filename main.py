"Importar librerías"
import cv2
import os
from djitellopy import Tello
from ultralytics import YOLO

count = 0

"Conectar drone"
tello = Tello()
tello.connect()

"Crear carpeta para almacenar imagenes"
output_dir = 'captured_photos'
os.makedirs(output_dir, exist_ok=True)

"Cargar el modelo YOLO"
model = YOLO("weights/best.pt")

"Iniciar el stream del video"
tello.streamon()

"Agregar limite"
threshold = 0.75

while True:
    "Obtener el frame"
    frame = tello.get_frame_read().frame

    "Cambiar imagen a blanco y negro"
    img = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    "Leer el resultado del modelo"
    results = model.predict(img)[0]

    "Extraer información del modelo"
    for result in results.boxes.data.tolist():
        x1,y1,x2,y2,score,class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1),int(y1)),(int(x2),int(y2)),(0,255,0),4)
            "Guardar la imagen del frame"
            photo_path = os.path.join(output_dir, f'photo_{count+1}.jpg')
            cv2.imwrite(photo_path,frame)
            count += 1
            "Esperar 1 segundo antes de tomar la siguiente foto"
            cv2.waitKey(5000)

    cv2.imshow("DJI drone", frame)

    "Salir del programa"
    k = cv2.waitKey(30)
    if k == 27:
        tello.streamoff()
        break

cv2.destroyWindow()