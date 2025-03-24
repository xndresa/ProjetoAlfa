import cv2
from utils import carregar_detector, detectar_objetos

# Iniciar a captura de vídeo (0 para webcam padrão)
cap = cv2.VideoCapture(0)

detector_rosto = carregar_detector()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detectar rostos
    frame = detectar_objetos(frame, detector_rosto)
    
    # Exibir o vídeo com as detecções
    cv2.imshow('Detector de Rostos', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()