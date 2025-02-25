import pyautogui as pt
import cv2
from pynput.keyboard import Key, Controller
import win32gui,win32con
from time import sleep

hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
sleep(2)

pt.FAILSAFE = True

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print((x,y))
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (0, 0, 255), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates and color
        # on the Shell
        bgr = img[y, x]
        b, g, r = bgr[0], bgr[1], bgr[2]
        print('pt.moveTo({}, {}) {}'.format(x, y, bgr))
 
        # displaying the coordinates and color
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)

# make screenshot of screen
pt.screenshot("imgs/screenshot.png")

# reading the image
img = cv2.imread('imgs/screenshot.png', 1)

# displaying the image
cv2.imshow('image', img)

# setting mouse handler for the image
# and calling the click_event() function
cv2.setMouseCallback('image', click_event)

# Wait for a key to be pressed to exit
while True:
    if cv2.waitKey(0):
        break

# Close the window
cv2.destroyAllWindows()