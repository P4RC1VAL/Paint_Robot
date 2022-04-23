
import numpy
import cv2


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()


class SprayGun:
    def __init__(self):
        pass
    class SprayGunOnOff:
        def __init__(self):
            pass
        def on():
            pass
        def off():
            pass

class Camera:
    def __init__(self):
        pass
    def uses(self):
        self.determenant = MudDetect()
    def getCoordinate(self):
        pass

class ControlSystem:
    def __init__(self):
        pass
    def EngineOnOff(self, state):
        pass
    def CommandRec(self, string):
        self.string = string
    def go(self, angle, speed):
        cam = Camera()
        coordinate = Camera.getCoordinate(self)
        self.angle = angle
        self.speed = speed
    def stop(self, angle):
        self.angle = angle

class MudDetect:
    def __init__(self):
        pass


def checkStatus(status):
    robot = Robot()
    if(status == '1'):
        print('[STATUS] System activated')
        robot.control.EngineOnOff(True)
    elif(status == '2'):
        print('[STATUS] Mud annigilation')
        robot.cam.uses()
        print('[STATUS] Getting Mud coordinates')
        robot.cam.getCoordinate()
    elif(status == '3'):
        print('[STATUS] Go to problem place')
        robot.control.go(90, 100)
    elif(status == '4'):
        print('[STATUS] Stop')
        robot.control.stop(0)
    elif(status == '5'):
        print('[STATUS] Start cleaning')
        robot.puliviz.SprayGunOnOff.on()
    elif(status == '6'):
        print('[STATUS] Stop cleaning')
        robot.puliviz.SprayGunOnOff.off()
    elif(status == '7'):
        print('[STATUS] Change the world, my finall message, goodbye')
        robot.control.EngineOnOff(False)
    elif(status == 'exit'):
        exit('[SYS] Success')
    else:
        print('[SYS] ERROR, please try again ')

class Robot:
    def __init__(state=False):
        pass
    spray = SprayGun()
    contsys = ControlSystem()
    cam = Camera()
    
    class EventHandler:
        def __init__(self, func=None):
            if func:
                self.Event = func
        def Event(self):
            pass

def Terminal():
    while(True):
        status = input()
        checkStatus(status)

def EventNet():
    pass

def main():
    print('[SYS] Choose:/')
    while True:
        rob = Robot()
        command = input()
        if command == 'term':
            print('[SYS] Enter the command: ')
            event = rob.EventHandler(EventTerminal)
            event.Event()
        elif command == 'net':
            print('[SYS] Net starting... ')
            event = rob.EventHandler(EventNet)
            event.Event()
            print('[SYS] Net end')
        elif command == 'exit':
            exit('[SYS] Success')
        else:
            print('[SYS] Please, enter correct command')
    

if __name__ == '__main__':
    main()
