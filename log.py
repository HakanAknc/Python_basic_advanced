import logging
import json

# Config dosyasını oku
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Loglama durumu
logging_enabled = config.get("logging_enabled", False)

if logging_enabled:
    logging.basicConfig(
        filename="app.log",  # Log dosyasının adı
        level=logging.INFO,  # Log (INFO, ERROR)
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def some_function():
    if logging_enabled:
        logging.info("Bu bir bilgi logudur.")
    print("Fonksiyon çalıştı!")

def some_error_function():
    try:
        1 / 0
    except ZeroDivisionError as e:
        if logging_enabled:
            logging.error("Bir hata oluştu: %s", e)
        print("Hata: Bölme işlemi sıfıra bölünemez. ******")

some_function()
some_error_function()

print("Program bitti.")
