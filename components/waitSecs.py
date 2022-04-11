import suanpan
from suanpan.app import app
from suanpan.app.arguments import String, Int
from suanpan.log import logger

import time

@app.input(String(key="inputData1"))
@app.param(Int(key="param1"))
@app.output(String(key="outputData1"))
def waitSecs(context):
    args = context.args
    time.sleep(args.param1 / 1000)
    return args.inputData1


if __name__ == "__main__":
    suanpan.run(app)
