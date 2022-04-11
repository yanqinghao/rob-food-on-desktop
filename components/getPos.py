import suanpan
from suanpan.app import app
from suanpan.app.arguments import String, Json
from suanpan.log import logger

import win32gui
import keyboard

@app.input(String(key="inputData1"))
@app.output(Json(key="outputData1"))
def getPos(context):
    args = context.args
    logger.info("Start to detect keyboard R...")
    keyboard.wait('r')
    logger.info("Detect keyboard R Pressed...")
    flags, hcursor, (x,y) = win32gui.GetCursorInfo()

    return {"x": x, "y": y}


if __name__ == "__main__":
    suanpan.run(app)
