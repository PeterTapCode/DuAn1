import pyautogui 
from pyput.keyboard import *

# ======= Cài đặt ========
delay = 0.1 
tiep_tuc  = key.f1()
dung_auto = key.f2()
thoat_auto = key.esc()

# ========================

dung = True
Chay_tt = True

def on_press(key):
    global Chay_tt, dung
    
    if key == tiep_tuc:
        dung = False
        print("[Resumed]")
    elif key == dung_auto:
        dung = True
        print("[Paused]")
    elif key == thoat_auto:
        Chay_tt = False
        print("[Exit]")
        

def hienthi_dieukhien():
    print("Auto clicker by Phong")
    print("----Setting :----")
    print("\t delay = " + str(dotre) + 'giay' + '\n')
    print("// - Controls:")
    print("\t F1 = Tiep Tuc")
    print("\t F2 = Dung Lai")
    print("\t F3 = Thoat Ra")
    print("================================================")
    print("Nhan F1 De Bat Dau...")