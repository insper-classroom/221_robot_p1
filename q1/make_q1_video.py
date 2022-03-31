import math
import cv2
from cv2 import IMREAD_UNCHANGED
import numpy as np
from random import triangular

f = 200

print(f"H hero {60/f*600}")
print(f"H meteor {60/f*371}")

def overlay(img_bg, img_fg, alpha):
    print("Alpha: ", alpha.shape)
    print("BG: ", img_bg.shape)
    ret, mask = cv2.threshold(alpha, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(img_bg,img_bg,mask = mask_inv)
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img_fg,img_fg,mask = mask)
    # Put logo in ROI and modify the main image
    return cv2.add(img1_bg,img2_fg)
    
class Character:
    def __init__(self, img, x, y, z, H, v=0):
        self.z = float(z)
        self.x = float(x)
        self.y = float(y)
        self.img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
        self.v = float(v) #pixels por segundo
        self.H = float(H)

    def update(self, dt):
        self.x -= int(self.v * dt) # dt is in secs
        #print(self.x)

    def draw(self, bgr):
        h = self.H/self.z * f
        w = self.img.shape[1]/self.img.shape[0]*self.H/self.z * f
        print((w,h))
        print((self.x,self.y, self.z))
        img_to_show = cv2.resize(self.img, (int(w),int(h)))
        bgr[int(self.y):(int(self.y)+int(h)), int(self.x):(int(self.x)+int(w))] = \
            overlay(
                bgr[int(self.y):(int(self.y)+int(h)), int(self.x):(int(self.x)+int(w))],
                img_to_show[:,:,:-1],
                img_to_show[:,:,-1]
            ) 
        

if __name__ == "__main__":

    # constants
    img_w = 800
    img_h = 600
    timespan = 30.
    fps = 30.
    frames = int(timespan * fps)

    # Hero
    hero = Character('green_lama.png', 100, 200, 250, 180)
    
    # Meteor
    meteor = Character('meteoro.png', 400, 400, 250, 111.3, v=60)
    

    # independent movement variables
    t_alien = 0

    last_shot = -1
    fourcc = cv2.VideoWriter_fourcc("H","2","6","4")
    writer = cv2.VideoWriter("attempt3.mp4",fourcc,30,(img_w,img_h),True)
    for t in range(frames):
        try:
            bgr = np.zeros((img_h,img_w,3), dtype=np.uint8)

            # drawing 
            hero.draw(bgr)
            meteor.draw(bgr)

            # Update
            hero.update(1./fps)
            meteor.update(1./fps)

            # Show image
            cv2.imshow("Game", bgr)
            writer.write(bgr)
            if cv2.waitKey(1000//int(fps)) == ord('q'):
                break
        except Exception as e:
            cv2.destroyAllWindows()
            writer.release()
            raise e

    cv2.destroyAllWindows()
    writer.release()






