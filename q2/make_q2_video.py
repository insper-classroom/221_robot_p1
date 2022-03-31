import math
import cv2
from cv2 import IMREAD_UNCHANGED
import numpy as np
import random

COLOR = (255, 255, 0)

class Quadrado:
    def __init__(self, x, y, z, t):
        self.z = float(z)
        self.x = float(x)
        self.y = float(y)
        self.t = float(t)
        self.vx = 0.0 #pixels por segundo
        self.vy = 0.0 #pixels por segundo
        self.vz = 0.0 #pixels por segundo
        self.w = 0.0 #rad/s 

    def update(self, dt):
        self.x += self.vx * dt # dt is in secs
        self.y += self.vy * dt # dt is in secs
        self.z += self.vz * dt # dt is in secs
        self.t += self.w * dt # 
        #print(self.x)

    def draw(self, bgr):
        siz_ = 1000/self.z

        x = np.empty(4)
        y = np.empty(4)

        x[0] = self.x + siz_/2**.5 * math.cos(math.pi/4 + self.t)  
        y[0] = self.y + siz_/2**.5 * math.sin(math.pi/4 + self.t)  
        x[1] = self.x + siz_/2**.5 * math.cos(3*math.pi/4 + self.t)  
        y[1] = self.y + siz_/2**.5 * math.sin(3*math.pi/4 + self.t)  
        x[2] = self.x + siz_/2**.5 * math.cos(-3*math.pi/4 + self.t)  
        y[2] = self.y + siz_/2**.5 * math.sin(-3*math.pi/4 + self.t)  
        x[3] = self.x + siz_/2**.5 * math.cos(-math.pi/4 + self.t)  
        y[3] = self.y + siz_/2**.5 * math.sin(-math.pi/4 + self.t) 

        cv2.polylines(bgr, [np.column_stack((x,y)).astype(np.int32).reshape((-1,1,2))], True, COLOR, 3)
        

if __name__ == "__main__":

    # constants
    img_w = 800
    img_h = 600
    timespan = 20.
    fps = 30.
    frames = int(timespan * fps)

    quad = Quadrado(img_w//2,img_h//2,6,.3)

    # independent movement variables
    t = 0

    last_shot = -1
    fourcc = cv2.VideoWriter_fourcc("H","2","6","4")
    writer = cv2.VideoWriter("quadrado.mp4",fourcc,30,(img_w,img_h),True)
    for t in range(frames):
        try:
            bgr = np.zeros((img_h,img_w,3), dtype=np.uint8)

            # drawing 
            quad.draw(bgr)
            
            # set new speeds
            quad.vx += random.randint(-5, 5)/10
            quad.vy += random.randint(-5, 5)/10
            quad.vz += random.randint(-10, 10)/200
            quad.w += random.randint(-5, 6)/15

            # Update
            quad.update(1./fps)
            
            # Show image
            cv2.imshow("Quadrado", bgr)
            writer.write(bgr)
            if cv2.waitKey(1000//int(fps)) == ord('q'):
                break
        except Exception as e:
            cv2.destroyAllWindows()
            writer.release()
            raise e
        
    cv2.destroyAllWindows()
    writer.release()






