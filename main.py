"Importar librerías"
import cv2
import threading
import time
from djitellopy import Tello
from ultralytics import YOLO

"Cargar el modelo YOLO"
model = YOLO("weights/roof/best.pt")

"Agregar limite"
threshold = 0.90

"Conectar drone"
tello = Tello()
tello.connect()

"Iniciar el stream del video"
tello.streamon()


def detectar():
    count = 0

    while True:
        frame = tello.get_frame_read().frame
        results = model.predict(frame)[0]

        for result in results.boxes.data.to():
            x1,y1,x2,y2,score,classId = result

            if score > threshold:
                print("Porcentaje", score)
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(classId)], (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3,(0, 255, 0), 2)
                cv2.imwrite("captured_photos/"f'photo_{count + 1}.jpg', frame)
                count += 1
                cv2.waitKey(5000)

        cv2.imshow("DJI drone", frame)

        "Salir del programa"
        k = cv2.waitKey(30)
        if k == 27:
            tello.streamoff()
            break


hiloVideo = threading.Thread(target=detectar)
hiloVideo.start()
hiloVideo.join()
cv2.destroyWindow()