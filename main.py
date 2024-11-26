import logging
import configparser

# ConfigParser ile config.ini dosyasından okuttuk
config = configparser.ConfigParser()
config.read("config.ini")

# Loglama durumunu config dosyasından çekme
logging_enabled = config["Settings"].getboolean("logging_enabled")
log_file = config["Settings"].get("log_file", "default.log")
log_level = config["Settings"].get("log_level", "INFO")

log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}
selected_log_level = log_levels.get(log_level.upper(), logging.INFO)

# Loglama ayarları
if logging_enabled:
    logging.basicConfig(
        filename=log_file,
        level=selected_log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
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
        print("Hata: Bölme işlemi sıfıra bölünemez. DewsLife")

some_function()
some_error_function()

print("Program bitti.")
