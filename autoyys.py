# coding:utf-8
#
import os
import os
import sys
import subprocess
import operator
import time
import math
import random
from PIL import Image
from functools import reduce
# 配置常量

# 最小差距值，DIFFER小于此值，表明是同一步的截图
MIN_DIFFER = 2000
# 最大差距值,DIFFER大于此值，可以认定两张图片是完全不同的
MAX_DIFFER = 10000
# “挑战”按钮所在位置宽的系数，可能会不准，得到方式：w/max_w （w是挑战按钮左边的像素，max_w是手机屏幕的最大宽）
CHALLENGEX = 0.73
# “挑战”按钮所在位置高的系数，可能会不准，得到方式：h/max_h （h是挑战按钮上边的像素，max_h是手机屏幕的最大高）
CHALLENGEY = 0.66
# “准备”按钮的宽的系数，得到方式同“挑战”，系数下同，不再标出
READYX = 0.89
# “准备”按钮的高的系数
READYY = 0.75
# “拒绝”按钮左边的系数
MIN_DENYX = 0.63
# “拒绝”按钮右边的系数
MAX_DENYX = 0.77
# “拒绝”按钮上边的系数
MIN_DENYY = 0.66
# “拒绝”按钮下边的系数
MAX_DENYY = 0.77
# 刷一遍魂十的最短时间，默认30s
MIN_TIME = 30
# 转景时间，根据我的手机暂定0.5s
SLEEP_TIME = 0.5
# 是否需要准备，默认不需要，开启阵容锁定即可
READY = 0
# 刷多少次，默认无限循环
COUNT = -1
# 截图方式
screenshot_way = 2
# 程序运行时的截图
IMAGE_NAME = "./image/current.png"
# 御魂开始之前的界面
START_IMAGE = Image.open("./image/yh.start.yys.png")
# 需要点准备的界面
READY_IMAGE = Image.open("./image/yh.ready.yys.png")
# 结束的界面
END_IMAGE = Image.open("./image/yh.end.yys.png")
# 失败的界面
FAIL_IMAGE = Image.open("./image/yh.fail.yys.png")
# 有好友发送协作任务时候的界面
ASSIST_IMAGE = Image.open("./image/xz.yys.png")
# 将“拒绝”按钮截出来，因为好友可以随时发送请求，所以只将最明显的特征截取出来
assistx = ASSIST_IMAGE.size[0]
assisty = ASSIST_IMAGE.size[1]
min_dx = MIN_DENYX * assistx
min_dy = MIN_DENYY * assisty
max_dx = MAX_DENYX * assistx
max_dy = MAX_DENYY * assisty
ASSIST_IMAGE = ASSIST_IMAGE.crop((min_dx, min_dy, max_dx, max_dy))

# 读取参数
if len(sys.argv) == 3:
    arg_min = sys.argv[1]
    if arg_min:
        try:
            MIN_TIME = int(arg_min)
        except:
            print("请输入正确时间")
            sys.exit()

    arg_count = sys.argv[2]
    if arg_count:
        try:
            COUNT = int(arg_count)
        except:
            print("请输入正确的次数")
            sys.exit()


def pull_screenshot():
    '''
    屏幕截图
    新的方法请根据效率及适用性由高到低排序
    return imageobject
    '''
    global screenshot_way
    if screenshot_way == 2 or screenshot_way == 1:
        process = subprocess.Popen('adb shell screencap -p', shell=True, stdout=subprocess.PIPE)
        screenshot = process.stdout.read()
        if screenshot_way == 2:
            binary_screenshot = screenshot.replace(b'\r\n', b'\n')
        else:
            binary_screenshot = screenshot.replace(b'\r\r\n', b'\n')
        f = open(IMAGE_NAME, 'wb')
        f.write(binary_screenshot)
        f.close()
    elif screenshot_way == 0:
        os.system('adb shell screencap -p /sdcard/current.png')
        os.system('adb pull /sdcard/current.png ' + IMAGE_NAME)
        os.system('adb shell rm /sdcard/current.png')

    return Image.open(IMAGE_NAME)

def int_compare(image1, image2):
    """返回两张图片的差异值"""
    histogram1 = image1.histogram()
    histogram2 = image2.histogram()

    differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a-b)**2, histogram1, histogram2)))/len(histogram1))
    return differ


def compare(image1, image2):
    '''
    检测两张图片(Image)相似度，根据DIFFER的数值来比较
    return 0 不相似 1 相等 2 相似
    '''
    differ = int_compare(image1, image2)

    if differ < MIN_DIFFER:
        result = 1
    elif differ < MAX_DIFFER:
        result = 2
    else:
        result = 0
    return result


def click(x, y):
    """点击坐标"""
    os.system("adb shell input tap {x} {y}".format(x=x, y=y))


def get_xy(img, scalex, scaley):
    """根据图片以及比例，算出按钮的坐标"""
    return img.size[0] * scalex, img.size[1] * scaley


def check_xz(img):
    imgx = img.size[0]
    imgy = img.size[1]
    min_ix = MIN_DENYX * imgx
    min_iy = MIN_DENYY * imgy
    max_ix = MAX_DENYX * imgx
    max_iy = MAX_DENYY * imgy
    img = img.crop((min_ix, min_iy, max_ix, max_iy))
    value = int_compare(img, ASSIST_IMAGE)
    if value < 260:
        result = True
    else:
        result = False

    return result


def check_start():
    """检测开始，确定是否点击"""
    flag = 0
    for _ in range(30):
        time.sleep(0.5)
        simage = pull_screenshot()
        if check_xz(simage):
            ssizex = simage.size[0]
            ssizey = simage.size[1]
            denyx = random.uniform(MIN_DENYX * ssizex, MAX_DENYX * ssizex)
            denyy = random.uniform(MIN_DENYY * ssizey, MAX_DENYY * ssizey)
            print("检测到协助，点击拒绝按钮")
            click(denyx, denyy)
        if flag == 0:
            sresult = compare(simage, START_IMAGE)
            if sresult:
                inputx, inputy = get_xy(simage, CHALLENGEX, CHALLENGEY)
                print("检测到开始，点击挑战按钮")
                click(inputx, inputy)
                flag = 1
                time.sleep(SLEEP_TIME)
        if READY:
            rresult = compare(simage, READY_IMAGE)
            if rresult:
                inputx, inputy = get_xy(simage, READYX, READYY)
                print("检测到准备，点击准备按钮")
                click(inputx, inputy)
                flag = 2
        if READY and flag == 2:
            break
        elif READY == 0 and flag == 1:
            break


def check_end():
    """检测结束，确定是否点击"""
    flag = 0
    counter = 0
    min_w = 0.82
    max_w = 0.98
    min_h = 0.10
    max_h = 0.74
    for _ in range(90):
        time.sleep(0.5)

        eimage = pull_screenshot()
        esizex = eimage.size[0]
        esizey = eimage.size[1]
        clickx = random.uniform(min_w * esizex, max_w * esizex)
        clicky = random.uniform(min_h * esizey, max_h * esizey)

        if check_xz(eimage):
            denyx = random.uniform(MIN_DENYX * esizex, MAX_DENYX * esizex)
            denyy = random.uniform(MIN_DENYY * esizey, MAX_DENYY * esizey)
            print("检测到协助，点击拒绝按钮")
            click(denyx, denyy)
        if compare(eimage, FAIL_IMAGE):
            print("检测到失败，点击随机的空白区域")
            click(clickx, clicky)
        if compare(eimage, END_IMAGE):
            print("检测到结束，点击随机的空白区域")
            click(clickx, clicky)
            flag = flag + 1
            time.sleep(SLEEP_TIME)
        else:
            if flag > 0:
                break

        if flag > 0:
            counter = counter + 1
            if counter > 10:
                break


def check_screenshot():
    '''
    检查获取截图的方式
    '''
    global screenshot_way
    if os.path.isfile(IMAGE_NAME):
        os.remove(IMAGE_NAME)
    if (screenshot_way < 0):
        print('暂不支持当前设备')
        sys.exit()
    try:
        pull_screenshot().load()
        print('采用方式{}获取截图'.format(screenshot_way))
    except:
        screenshot_way -= 1
        check_screenshot()


def main():
    '''
    主函数
    '''
    global COUNT
    check_screenshot()
    circuit_count = 1
    while COUNT != 0:
        print("---------第%s次开始----------------------" % circuit_count)
        check_start()
        time.sleep(MIN_TIME)
        check_end()
        if COUNT > 0:
            COUNT = COUNT - 1
        print("---------第%s次结束----------------------" % circuit_count)
        circuit_count = circuit_count + 1
        time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
