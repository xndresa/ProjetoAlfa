# Parâmetros de detecção
SCALE_FACTOR = 1.3  # Escala para detecção
MIN_NEIGHBORS = 5   # Número mínimo de vizinhos para formar uma detecção
MIN_SIZE = (30, 30)  # Tamanho mínimo dos objetos detectados

# Caminho para o classificador
HAAR_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'