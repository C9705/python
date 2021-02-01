import pyautogui as pg
import time
# 保护措施，防止产生异常
pg.FAILSAFE = False
# # 操作等待
pg.PAUSE = 1
# # 获取当前屏幕像素
width, height = pg.size()
print(width, height)
# 获取鼠标当前位置坐标 position()
initialMouseX,initialMouseY  = pg.position()
print(initialMouseX,initialMouseY)
pg.moveTo(1014,284,duration=1)
pg.click()
# #
# # # Search
# time.sleep(5)
# pg.moveTo(265, 194, duration=1)
# pg.click()
# # # # # 文本框
# pg.moveTo(532, 422, duration=1)
# pg.click()
# # # # # 输入信息
# pg.typewrite(message='4 Digital Mic', interval=0.5)
# # # #
# # # # # Search2
# pg.moveTo(638, 564, duration=1)
# pg.click()
# #
# # # element 740 281
# pg.moveTo(740, 281, duration=1)
# pg.dragTo(x=292, y=249, duration=1, button='left')
# #
# # # export with checkout
# pg.moveTo(655, 187, duration=1)
# pg.click()
#
# time.sleep(2)
#
# browser.close()  # 关闭浏览器