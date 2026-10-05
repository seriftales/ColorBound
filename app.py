import sys
import cv2

from pathlib import Path
from app.config import Config
from app.logger import setup_logger
from app.camera_process import CameraProcessor
from app.streamer import Streamer

#Ana Uygulama Modülü : Ana uygulama döngüsünü başlatır, konfigürasyonu yükler, kamera ve görüntü işleme modüllerini başlatır.
def main():
    BASE_DIR = Path(__file__).resolve().parent
    
    logger = setup_logger(BASE_DIR)
    logger.info("Uygulama başlatılıyor...")

    config_path = BASE_DIR / "config" / "config.toml"
    
    config_loader = Config()
    config = config_loader.loadConfig(config_path)

    processor = CameraProcessor(config)
    streamer = Streamer()

    logger.info("Görüntü işleme döngüsü başlıyor")
    try:
        for frame in streamer.get_frame():
            processed_frame, detected_colors = processor.process_frame(frame)
            cv2.imshow("Processed Frame", processed_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        logger.exception("Beklenmeyen bir hata oluştu!")
        sys.exit(1)
    finally:
        logger.info("Sistem kapatılıyor")
        streamer.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()