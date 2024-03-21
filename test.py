import serial
import ch9329Comm
from ch9329Comm import keyboard
from ch9329Comm import mouse

keyboard = ch9329Comm.keyboard.DataComm('COM3')  # 开启串口，默认115200

# # 检查键盘状态
print('CH9329 version:', keyboard.version())
print('USB connected:', keyboard.usb_conn())
print('Num Lock:', keyboard.num_lock())
print('Caps Lock:', keyboard.caps_lock())
print('Scroll Lock:', keyboard.scroll_lock())

# # 键盘输出helloworld
keyboard.type('Hello World!') # 输入Hello World!
keyboard.send_data('Enter') # 回车换行
keyboard.release()  # 释放按键  

keyboard.close()

serial.ser = serial.Serial('COM4', 115200)  # 开启串口

# （绝对）鼠标移动到屏幕的左上100*100的位置

# dc = mouse.DataComm()
# dc.send_data_absolute(500,500)

# （相对）鼠标右移100px 下移100px
# dc2 = mouse.DataComm()
# dc2.move_to(-100, -100)

# # 校验
# dc2 = mouse.DataComm()
# dc2.move_to(-230,-480)

serial.ser.close()  # 关闭串口
