# ColorBound

ColorBound, OpenCV kullanarak gerçek zamanlı görüntü işleme ve renk tespiti yapan bir Computer Vision projesidir. Sistem, kameradan aldığı görüntü akışını HSV renk uzayına çevirir, TOML yapılandırma dosyasında belirlenen dinamik aralıklara göre  maskeleme yapar ve tespit edilen nesneleri Bounding Box içerisine alarak etiketler.

##  Özellikler
* **Gerçek Zamanlı Tespit:** Web kamerasından alınan görüntüler üzerinde anlık renk filtreleme.
* **Dinamik Yapılandırma:** Renklerin alt ve üst HSV sınır değerleri koda gömülmek yerine `config.toml` dosyasından okunur.
* **Gürültü Filtreleme:** Yanlış pozitifleri  engellemek için morfolojik işlemler ve minimum piksel alanı eşiği.
* **Merkezi Loglama:** Hata ayıklama ve sistem takibi için `loguru` tabanlı dinamik loglama mekanizması.

##  Kurulum (Ubuntu / Linux)

Sistem bağımlılıklarının çakışmaması için projenin izole bir Python sanal ortamında (venv) çalıştırılması önerilir.

1. **Depoyu Klonlayın:**
   ```bash
   git clone [https://github.com/seriftales/ColorBound.git](https://github.com/seriftales/ColorBound.git)
   cd ColorBound
   
   ```

2. **Sanal ortam oluşturun ve aktif edin:** 

    ```bash 
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Gerekli paketleri yükleyin:**
    ```bash 
    pip install -r requirements.txt
    ```

##  Çalıştırma 

Görüntü işleme motorunu ve kamera akışını başlatmak için ana orkestratör dosyasını çalıştırın:

```bash 
python3 app.py
```

##  Dizin Yapısı

```text 
ColorBound/
├── app/
│   ├── __init__.py          # Paketleyici
│   ├── camera_process.py    # Görüntü işleme, HSV maskeleme ve Bounding Box algoritmaları
│   ├── config.py            # TOML yapılandırma okuyucusu 
│   ├── logger.py            # Loguru rotasyonlu loglama yapılandırması
│   └── streamer.py          # Kamera bağlantısı ve Stream
├── config/
│   └── config.toml          # Renklerin dinamik HSV alt/üst sınır değerleri
├── logs/
│   └── app.log              # Uygulama çalışma zamanı kayıtları 
├── .gitignore               
├── requirements.txt         # Projenin çalışması için gereken Python kütüphaneleri
└── app.py                   # Uygulamanın giriş noktası 

```
