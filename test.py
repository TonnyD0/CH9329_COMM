import serial
import ch9329Comm

serial.com3 = serial.Serial('COM3', 115200) # 开启串口

keyboard = ch9329Comm.keyboard.DataComm(serial.com3) # 键盘

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


mouse = ch9329Comm.mouse.DataComm(serial.com3, 2560, 1440, 1.25) # 鼠标

# （绝对）鼠标移动到屏幕的左上100*100的位置
mouse.send_data_absolute(100,100)

# （相对）鼠标右移100px 下移100px
mouse.move_to_basic(100, 100)

# # 校验
# mouse.move_to(-230,-480)

serial.com3.close()  # 关闭串口
