from config import Config

# Config sınıfını başlat
config = Config()

# Ayarları oku
is_active = config.get_boolean('Settings', 'is_active')
log_level = config.get('Settings', 'log_level')
app_name = config.get('Settings', 'app_name')

# Ayarlara göre işlem yap
if is_active:
    print(f"{app_name} çalışıyor!")
    print(f"Log seviyesi: {log_level}")
else:
    print(f"{app_name} şu anda devre dışı.")
