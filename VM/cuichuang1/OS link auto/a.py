import pyautogui as pg
import time
time.sleep(2)
pg.moveTo(300, 416, duration=0.2)
pg.click()
pg.typewrite(message=r"E:\workspaceprod\cuichuang1\element_link_tool\dist\element_link_tool\upload_os_3.xlsx",
             interval=0.2)
pg.press('enter')
pg.press('enter')
time.sleep(20)
pg.moveTo(994, 287, duration=0.2)
pg.click()
pg.press('enter')
time.sleep(30)

# promte
#     more
pg.moveTo(760, 264, duration=0.2)
pg.click()
pg.moveTo(758, 319, duration=0.2)
pg.click()
pg.press('enter')
time.sleep(10)
pg.moveTo(323, 294, duration=0.2)
pg.click()

pg.moveTo(437, 265, duration=0.2)
pg.click()
pg.moveTo(450, 308, duration=0.2)
pg.click()

pg.moveTo(350, 268, duration=0.2)
pg.click()