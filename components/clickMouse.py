import suanpan
from suanpan import g
from suanpan.app import app
from suanpan.app.arguments import Json, String, Int
from suanpan.log import logger

import time
import numpy
import win32api, win32con
import pyautogui

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def getScreenShot(radius):
    img = pyautogui.screenshot()
    img = numpy.array(img)
    return img[g.y-radius:g.y+radius, g.x-radius:g.x+radius ,:]

def check(x, y):
    return not (x==y).all()

@app.input(String(key="inputData1"))
@app.input(Json(key="inputData2"))
@app.param(Int(key="param1"))
@app.param(Int(key="param2"))
@app.param(Int(key="param3"))
@app.output(String(key="outputData1"))
def clickMouse(context):
    args = context.args
    if args.inputData1:
        if g.x and g.y:
            g.pic = getScreenShot(args.param2)
            count = 0
            while True:
                logger.info("click mouse")
                click(g.x, g.y)
                time.sleep(args.param1 / 1000)
                pic = getScreenShot(args.param2)
                if check(g.pic, pic) or count >= args.param3:
                    break
                else:
                    count += 1
            if count < args.param3:
                return f"点击坐标{g.x}, {g.y}成功"
    else:
        g.x, g.y = args.inputData2["x"], args.inputData2["y"]


if __name__ == "__main__":
    suanpan.run(app)
