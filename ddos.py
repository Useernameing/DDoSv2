import requests
import time

def main():
    print("Bu kod sadece eğitim amaçlıdır. Kötüye kullanmayınız.")

    # Kullanıcıdan URL al
    url = input("https://www.sitegirinizz/: ")

    # Sayı giriniz
    num_requests = 1000

    # İstekler arasında küçük bir gecikme ekleyin
    request_delay = 0.1

    # Content-Security-Policy başlığı
    csp_header = {
        "Content-Security-Policy": "default-src 'self'; script-src 'self'; >
    }

    # İstek döngüsü
    for i in range(num_requests):
        try:
            # Özel başlıklı GET isteği gönder
            response = requests.get(url, headers=csp_header)

            # Yanıt durum kodunu yazdır
            print(f"İstek {i+1} - Yanıt Durum Kodu: {response.status_code}")

        except requests.exceptions.RequestException as e:
            # Spesifik hataları yakala
            if isinstance(e, (requests.exceptions.ConnectionError, requests>
                print(f"İstek {i+1} - Hata: {e} (Bağlantı veya Zaman Aşımı)>
            else:
                print(f"İstek {i+1} - Hata: {e}")

        # İstekler arasında gecik
        time.sleep(request_delay)

    print("Tüm istekler tamamlandı.")