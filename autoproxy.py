#"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
import subprocess
import winreg
import requests as req


def login(url="http://stgw.iitmandi.ac.in/ug/authenticate.php", username="joe", password="mama"):

    myobj = {
        "username": username,
        "password": password
    }

    res = req.post(url, myobj)

    return res.status_code


registry_key = winreg.OpenKey(
    winreg.HKEY_CURRENT_USER, "Software\Microsoft\Windows\CurrentVersion\Internet Settings", 0, winreg.KEY_ALL_ACCESS)

x = winreg.QueryValueEx(registry_key, "ProxyEnable")
wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
data = wifi.decode('utf-8')
if 'IITMandi_5.0 GHz' in data:
    # print(x[0])
    login()
    if (x[0] == 0):
        winreg.SetValueEx(registry_key, "ProxyEnable", 0, winreg.REG_DWORD, 1)

else:
    if (x[0] == 1):
        winreg.SetValueEx(registry_key, "ProxyEnable", 0, winreg.REG_DWORD, 0)
