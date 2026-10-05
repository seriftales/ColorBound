import toml
from loguru import logger
from pathlib import Path

# Config Modülü: Ayar dosyasını yükler ve doğrular 
class Config:
    def loadConfig(self, config_file: Path) -> dict:
        if not config_file.exists():

            raise FileNotFoundError(f"Kritik Hata: Ayar dosyası bulunamadı -> {config_file}")

        try:
            with open(config_file, "r") as f:
                config_data = toml.load(f)
                
            if 'colors' not in config_data:
                raise ValueError("Kritik Hata: Config dosyasında '[colors]' anahtarı eksik.")
                
            logger.info("Config başarıyla yüklendi")
            return config_data
            
        except Exception as e:
            logger.error(f"Config okuma başarısız: {e}")
            raise 