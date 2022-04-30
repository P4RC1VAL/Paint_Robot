
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

class Robot():
    def __init__(self):
		self.spray = SprayGun()
		self.contsys = ControlSystem()
		self.cam = Camera()
		
		
class Camera():
    def __init__(self):
		pass
        
    def detecting(self):
        self.detect = MudDetect()
        
    def getLocation(self):
		self.location = 0
        

class ControlSystem():
    def __init__(self):
        pass
        
    def EngineOnOff(self, state):
		self.statusOn = on
		self.statusOff = off
		
    def CommandString(self, string):
        self.string = string
        
    def move(self, angle, lenght, speed):
        cam = Camera()
        position = Camera.getLocation(self)
        self.angle = angle
        self.speed = speed
        self.lenght = lenght
        
    def stop(self, angle, location):
        self.angle = angle
        self.location = position

class MudDetect():
    def __init__(self):
        pass

class Manipulator():
	def __init__(self, orientation):
		self.orientV = vertical
		self.orientG = gorizontal

            
class SprayGun():
    def __init__(self):
        pass
    class SprayGunOnOff(SprayGun):
        def __init__(self):
            pass
        def on():
            pass
        def off():
            pass
            
def Terminal(system):
	robot = Robot()
	if (system == 1):
		print ("[SYS] The mud has been detected, moving...")
		robot.contsys.move(90,15,100)
	elif (system == 2):
		print ("[SYS] On position, chosing orientation...")
		print ("[SYS] Now orientation is " + str(Manipulator.self.orientV))
		else:
			print ("[SYS] Now orientation is " + str(Manipulator.self.orientG))
	elif (system == 3):
		print ("[SYS] Start cleaning")
		SprayGunOnOff.on()
	elif (system == 4):
		print ("[SYS] Stop cleaning")
		SprayGunOnOff.off()
	elif (system == 5):
		print ("[SYS] The cleaning is over, standby)")
		robot.contsys.EngineOnOff(off)
	else:
		exit("[ERR] You have some errors in program, please repair that and try again")
		

class EventSystem:
        def __init__(self, func=None):
            if func:
                self.Event = func
        def Event(self):
            pass
				

def SystemScreen():
    while(True):
        system = input()
        Terminal(system)
       
def NetCommand():
	while(True):
		msg = input()
		client(msg)


def main():
    print('[SYS] Choose:/')
    while True:
        rob = Robot()
        command = input()
        if command == 'manual':
            print('[SYS] Enter the command: ')
            event = rob.EventSystem(SystemScreen)
            event.Event()
        elif command == 'network':
            print('[SYS] Net connection starting... ')
            event = rob.EventSystem(NetCommand)
            event.Event()
            print('[SYS] Net connection was closed')
        elif command == 'exit':
            exit('[SYS] Success')
        else:
            print('[SYS] Please, enter correct command')
    

if __name__ == '__main__':
    main()
