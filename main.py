"Importar librerías"
import cv2
import threading
import time
from djitellopy import Tello
from ultralytics import YOLO

"Cargar el modelo YOLO"
model = YOLO("weights/roof/best.pt")

"Agregar limite"
threshold = 0.92

"Conectar drone"
tello = Tello()
tello.connect()

"Iniciar el stream del video"
tello.streamon()


def detectar():
    count = 0

    while True:
        frame = tello.get_frame_read().frame
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model.predict(img)[0]

        for result in results.boxes.data.to():
            x1,y1,x2,y2,score,classId = result

            if score > threshold:
                print("Porcentaje", score)
                cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(img, results.names[int(classId)], (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3,(0, 255, 0), 2)
                cv2.imwrite("captured_photos/"f'photo_{count + 1}.jpg', img)
                count += 1
                cv2.waitKey(5000)

        cv2.imshow("DJI drone", img)

        "Salir del programa"
        k = cv2.waitKey(30)
        if k == 27:
            tello.streamoff()
            break


hiloVideo = threading.Thread(target=detectar)
hiloVideo.start()
hiloVideo.join()
cv2.destroyWindow()