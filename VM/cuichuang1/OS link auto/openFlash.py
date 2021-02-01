import time
import pyautogui as pg

def openFlash():
    pass
# 保护措施
    pg.FAILSAFE=False
    pg.PAUSE = 1
    # 获取当前屏幕像素
    width, height = pg.size()
    time.sleep(2)
    x,y = pg.position()
    print(x,y)
    # 1
    pg.moveTo(135,46)
    pg.click()
    # # # 2
    pg.moveTo(365,219)
    pg.click()
    # # 3
    pg.moveTo(378,272)
    pg.click()

if __name__=='__main__':
    openFlash()