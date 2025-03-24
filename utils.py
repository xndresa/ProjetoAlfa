import cv2

def carregar_detector():
    return cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detectar_objetos(frame, detector):
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = detector.detectMultiScale(cinza, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in rostos:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame
