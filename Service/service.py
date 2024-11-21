import os

class MyService:
    def __init__(self):
        self.is_running = False

    def start_service(self):
        self.is_running = True
        print("Servis başlatılıyor...")
        self.log("Servis başarıyla başlatılıd.")

    def stop_service(self):
        self.is_running = False
        print("Servis durdurluyor...")
        self.log("Servis başarıyla durduldu.")

    def log(self, message):
        with open("service_log.txt", "a", encoding='utf-8') as log_file:
            log_file.write(f"{message}\n")

if __name__ == '__main__':
    service = MyService()
    service.start_service()
    service.stop_service()



"""
MyService sınıfı, basit bir servisi temsil eder.
start_service() fonksiyonu servisi başlatır.
stop_service() fonksiyonu servisi durdurur.
log() fonksiyonu her iki durumda da bir log kaydeder.
"""