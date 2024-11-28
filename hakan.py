import configparser

# config.ini dosyasını yükle
config = configparser.ConfigParser()
config.read('hakan.ini')

# Boolean değerleri oku
is_active = config.getboolean('Settings', 'is_active')
allow_notifications = config.getboolean('Settings', 'allow_notifications')

print(f"is_active: {is_active}")  # True
print(f"allow_notifications: {allow_notifications}")  # False
