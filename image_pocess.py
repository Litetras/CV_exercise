import sensor, image, time, json, pyb, os, tf, uos, gc
from pid import PID
from pyb import UART, Pin, Timer

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_gain(False)  # 自动增益关闭（False）。在使用颜色追踪时，要关闭自动增益。
sensor.set_auto_whitebal(False)  # 自动白平衡关闭。在使用颜色追踪时，要关闭自动白平衡。
sensor.set_auto_exposure(8300)  # 设置一个固定曝光时间，单位微秒。曝光时间短则适合光线比较好的情况
#print(sensor.get_exposure_us())#返回当前曝光值
sensor.skip_frames(time=1000)
clock = time.clock()

while (True):
    clock.tick()  # 开始追踪运行时间。
    for i in range(20):
        img = sensor.snapshot()
        img.binary([THRESHOLD])
        img.erode(1)  # 腐蚀噪音
    for i in range(20):
        img = sensor.snapshot()
        img.binary([THRESHOLD])
        img.dilate(2)  # 膨胀噪音
