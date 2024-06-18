"Importar librerías"
import cv2
from djitellopy import Tello

"Conectar drone"
tello = Tello()
tello.connect()

"Obtener el porcentaje de bateria"
print(tello.get_battery())

"Iniciar el stream del video"
tello.streamoff()
tello.streamon()

while True:
    "Obtener el frame"
    frame_read = tello.get_frame_read()
    frame = frame_read.frame

    "Cambiar imagen a blanco y negro"
    img = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    "Mostrar imagen"
    cv2.imshow("frame", img)

    "Salir del programa"
    k = cv2.waitKey(30)
    if k == 27:
        tello.streamoff()
        break

cv2.destroyWindow()