import cv2
from loguru import logger

# Streamer Modülü: Kameradan gelen görüntüleri alır ve stream eder
class Streamer:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            logger.error("Donanım Hatası: Kamera bağlantısı sağlanamadı")
            raise RuntimeError("Kamera açılmadığı için sistem başlatılamıyor.")

        logger.info("Kamera başarıyla başlatıldı")

    def get_frame(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                logger.warning("Kameradan frame gelmiyor, stream sonlandırılıyor.")
                break
                
            frame = cv2.flip(frame, 1)
            yield frame

    def release(self):
        if self.cap.isOpened():
            self.cap.release()
            logger.info("Kamera bağlantısı kesildi")