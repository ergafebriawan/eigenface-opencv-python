import os
from time import sleep

btn_exit = False

while (btn_exit == False):
    os.system('clear')
    print("pilih menu berikut: \n1. start program \n2. take sample \n3. training data \n4. test ultrasonic \n5. test doorlock")
    print("tekan q pada keyboard untuk menutup program")
    menu = input()

    if menu == 'q' or menu == 'Q':
        btn_exit = True
        sleep(1)
        break
    elif menu == '1':
        print('starting program......')
        sleep(0.5)
        os.system('python main.py')
    elif menu == '2':
        print('take sample picture......')
        sleep(0.5)
        os.system('python capture/take_capture.py')
    elif menu == '3':
        print('training data.......')
        sleep(0.5)
        os.system('python eigenface/training.py')
    elif menu == '4':
        print('testing ultrasonic........')
        sleep(0.5)
        os.system('python test_hardware/test_ultra.py')
    elif menu == '5':
        print('testing doorlock.........')
        sleep(0.5)
        os.system('python test_hardware/test_relay.py')
    else:
        print('invalid input keyboard')
        sleep(0.8)