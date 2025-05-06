"Importar librerías"
import cv2
import threading
import time
import math
import numpy as np
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
            cv2.destroyWindow()
            break


def girar(yaw, x, drone_x, y, drone_y):
    alpha = math.atan2(y-drone_y, x-drone_x)# Get degrees to of the angle but in radians
    alpha_degrees = math.degrees(alpha)     # Convert radians to degrees

    angle_to_remove = alpha_degrees - yaw   # Subtract degrees and orientation
    angle_to_move = (angle_to_remove + 180)%360 - 180 #Normalizar el ángulo para que esté entre -180 y 180 grados
    return angle_to_move

def distancia_euclidea(x, drone_x, y, drone_y):
    distancia = np.sqrt((y - drone_y)**2 + (x - drone_x)**2)# Calculate euclidean distance
    return distancia


hiloVideo = threading.Thread(target=detectar)
hiloVideo.start()

" Recorrer de inicio al punto 1 "

"Punto 1"
drone_pos1 = [116.5,0]
drone_x1, drone_y1 = drone_pos1
objective1 = [116.5,166]
x1, y1 = objective1

'Grados a mover'
yaw1 = tello.get_yaw() # Get drone orientation
print(f"Orientacion del drone: {yaw1}")

angle_to_move1 = girar(yaw1, x1, drone_x1, y1, drone_y1)

tello.takeoff() # Take off drone
tello.rotate_counter_clockwise(int(angle_to_move1)) # Rotate drone to left

'Recorrer la distancia punto 1'
euclidean_distance1 = distancia_euclidea(x1, drone_x1, y1, drone_y1) # Calculate euclidean distance to point 1
#print(euclidean_distance1)
tello.move_forward(int(euclidean_distance1)) # Move drone forward
time.sleep(0.3)

" Recorrer del punto 1 al punto 2 "

"Punto 2"
drone_pos2 = [116.5,166]
drone_x2, drone_y2 = drone_pos2
objective2 = [200,166]
x2, y2 = objective2

'Grados a mover'
yaw2 = tello.get_yaw() # Get drone orientation
print(f"Orientacion del drone: {yaw2}")

angle_to_move2 = girar(yaw2, x2, drone_x2, y2, drone_y2)
tello.rotate_clockwise(int(angle_to_move2)) # Rotate drone to right

'Recorrer distancia punto 2'
euclidean_distance2 = distancia_euclidea(x2, drone_x2, y2, drone_y2) # Calculate euclidean distance to point 2
#print(euclidean_distance2)
tello.move_forward(int(euclidean_distance2)) # Move drone forward
time.sleep(0.3)

" Recorrer del punto 2 al punto 3 "

"Punto 3"
drone_pos3 = [200,166]
drone_x3, drone_y3 = drone_pos3
objective3 = [200,266]
x3, y3 = objective3

'Grados a mover'
yaw3 = tello.get_yaw() # Get drone orientation
print(f"Orientacion del drone: {yaw3}")


angle_to_move3 = girar(yaw3, x3, drone_x3, y3, drone_y3)
tello.rotate_counter_clockwise(int(angle_to_move3)) # Rotate drone to left

'Recorrer distancia punto 3'
euclidean_distance3 = distancia_euclidea(x3, drone_x3, y3, drone_y3) # Calculate euclidean distance to point 3
#print(euclidean_distance3)
tello.move_forward(int(euclidean_distance3)) # Move drone forward
time.sleep(0.3)

" Recorrer del punto 3 al punto 4 "

"Punto 4"
drone_pos4 = [200,266]
drone_x4, drone_y4 = drone_pos4
objective4 = [100,67]
x4, y4 = objective4

'Grados a mover'
yaw4 = tello.get_yaw() # Get drone orientation
yaw4 = -1*yaw4
print(f"Orientacion del drone: {yaw4}")

angle_to_move4 = girar(yaw4, x4, drone_x4, y4, drone_y4)
tello.rotate_counter_clockwise(int(angle_to_move4)) # Rotate drone to left

euclidean_distance4 = distancia_euclidea(x4, drone_x4, y4, drone_y4) # Calculate euclidean distance to point 4
#print(euclidean_distance4)
tello.move_forward(int(euclidean_distance4))
time.sleep(0.3)

tello.land() # land drone
hiloVideo.join() # Eliminate thread
