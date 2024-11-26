import winreg # Importing the Windows Registry module

def read_registry_value(path, name):
    try:
        # Open the registry key in read-only mode
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_READ)
        # Query the value of the specified name under the registry key
        value, regtype = winreg.QueryValueEx(registry_key, name)
        # Close the registry key after reading
        winreg.CloseKey(registry_key)
        return value
    except WindowsError as e:
        # Handle errors if the registry key or value does not exist
        print(f"Registry error for {path}\\{name}: {e}")
        return None

path = "Software\\MyApp"
name = "female_gender"
value = read_registry_value(path, name)

if value is not None:
    print(f"The value of {name} is {value}")
else:
    print("Could not read the registry value.")
