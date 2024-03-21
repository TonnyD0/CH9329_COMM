import serial
import time

class DataComm:
    """
    此类初始化三个字典，
    control_button_hex_dict包含键盘上控制键，
    normal_button_hex_dict包含键盘上的普通按钮，
    normal_char_hex_dict包含大写字母及符号，
    如果需要更多的按钮，请自行根据协议文档补充。
    """

    def __init__(self, serial_com):
        
        serial.ser = serial.Serial(serial_com, 115200) # 开启串口

        self.normal_char_hex_dict = {"A": ["L_SHIFT","a"],
                                     "B": ["L_SHIFT","b"],
                                     "C": ["L_SHIFT","c"],
                                     "D": ["L_SHIFT","d"],
                                     "E": ["L_SHIFT","e"],
                                     "F": ["L_SHIFT","f"],
                                     "G": ["L_SHIFT","g"],
                                     "H": ["L_SHIFT","h"],
                                     "I": ["L_SHIFT","i"],
                                     "J": ["L_SHIFT","j"],
                                     "K": ["L_SHIFT","k"],
                                     "L": ["L_SHIFT","l"],
                                     "M": ["L_SHIFT","m"],
                                     "N": ["L_SHIFT","n"],
                                     "O": ["L_SHIFT","o"],
                                     "P": ["L_SHIFT","p"],
                                     "Q": ["L_SHIFT","q"],
                                     "R": ["L_SHIFT","r"],
                                     "S": ["L_SHIFT","s"],
                                     "T": ["L_SHIFT","t"],
                                     "U": ["L_SHIFT","u"],
                                     "V": ["L_SHIFT","v"],
                                     "W": ["L_SHIFT","w"],
                                     "X": ["L_SHIFT","x"],
                                     "Y": ["L_SHIFT","y"],
                                     "Z": ["L_SHIFT","z"],
                                     "~": ["L_SHIFT","`"],
                                     "!": ["L_SHIFT","1"],
                                     "@": ["L_SHIFT","2"],
                                     "#": ["L_SHIFT","3"],
                                     "$": ["L_SHIFT","4"],
                                     "%": ["L_SHIFT","5"],
                                     "^": ["L_SHIFT","6"],
                                     "&": ["L_SHIFT","7"],
                                     "*": ["L_SHIFT","8"],
                                     "(": ["L_SHIFT","9"],
                                     ")": ["L_SHIFT","0"],
                                     "_": ["L_SHIFT","-"],
                                     "+": ["L_SHIFT","="],
                                     "{": ["L_SHIFT","["],
                                     "}": ["L_SHIFT","]"],
                                     "|": ["L_SHIFT","\\"],
                                     ":": ["L_SHIFT",";"],
                                     "\"": ["L_SHIFT","'"],
                                     "<": ["L_SHIFT",","],
                                     ">": ["L_SHIFT","."],
                                     "?": ["L_SHIFT","/"],
                                     " ": ["","Space"]
                                     }

        self.control_button_hex_dict = {"NULL": b'\x00',
                                        "R_WIN": b"\x80",
                                        "R_ALT": b"\x40",
                                        "R_SHIFT": b"\x20",
                                        "R_CTRL": b"\x10",
                                        "L_WIN": b"\x08",
                                        "L_ALT": b"\x04",
                                        "L_SHIFT": b"\x02",
                                        "L_CTRL": b"\x01"
                                        }

        self.normal_button_hex_dict = {"null": b'\x00',
                                        "a": b"\x04",
                                        "b": b"\x05",
                                        "c": b"\x06",
                                        "d": b"\x07",
                                        "e": b"\x08",
                                        "f": b"\x09",
                                        "g": b"\x0A",
                                        "h": b"\x0B",
                                        "i": b"\x0C",
                                        "j": b"\x0D",
                                        "k": b"\x0E",
                                        "l": b"\x0F",
                                        "m": b"\x10",
                                        "n": b"\x11",
                                        "o": b"\x12",
                                        "p": b"\x13",
                                        "q": b"\x14",
                                        "r": b"\x15",
                                        "s": b"\x16",
                                        "t": b"\x17",
                                        "u": b"\x18",
                                        "v": b"\x19",
                                        "w": b"\x1A",
                                        "x": b"\x1B",
                                        "y": b"\x1C",
                                        "z": b"\x1D",
                                        "1": b"\x1E",
                                        "2": b"\x1F",
                                        "3": b"\x20",
                                        "4": b"\x21",
                                        "5": b"\x22",
                                        "6": b"\x23",
                                        "7": b"\x24",
                                        "8": b"\x25",
                                        "9": b"\x26",
                                        "0": b"\x27",
                                        "Enter": b"\x28",
                                        "Esc": b"\x29",
                                        "Backspace": b"\x2A",
                                        "Tab": b"\x2B",
                                        "Space": b"\x2C",
                                        "-": b"\x2D",
                                        "=": b"\x2E",
                                        "[": b"\x2F",
                                        "]": b"\x30",
                                        "\\": b"\x31",
                                        "": b"\x32",
                                        ";": b"\x33",
                                        "'": b"\x34",
                                        "`": b"\x35",
                                        ",": b"\x36",
                                        ".": b"\x37",
                                        "/": b"\x38",
                                        "Caps": b"\x39",
                                        "F1": b"\x3A",
                                        "F2": b"\x3B",
                                        "F3": b"\x3C",
                                        "F4": b"\x3D",
                                        "F5": b"\x3E",
                                        "F6": b"\x3F",
                                        "F7": b"\x40",
                                        "F8": b"\x41",
                                        "F9": b"\x42",
                                        "F10": b"\x43",
                                        "F11": b"\x44",
                                        "F12": b"\x45",
                                        "PrintScr": b"\x46",
                                        "ScrollLock": b"\x47",
                                        "PauseBreak": b"\x48",
                                        "Insert": b"\x49",
                                        "Home": b"\x4A",
                                        "PageUp": b"\x4B",
                                        "Delete": b"\x4C",
                                        "End": b"\x4D",
                                        "PageDown": b"\x4E",
                                        "Right": b"\x4F",
                                        "Left": b"\x50",
                                        "Down": b"\x51",
                                        "Up": b"\x52",
                                        "NumLock": b"\x53",
                                        "Pad_\\": b"\x54",
                                        "Pad_*": b"\x55",
                                        "Pad_-": b"\x56",
                                        "Pad_+": b"\x57",
                                        "Pad_Enter": b"\x58",
                                        "Pad_End": b"\x59",
                                        "Pad_Down": b"\x5A",
                                        "Pad_Next": b"\x5B",
                                        "Pad_Left": b"\x5C",
                                        "Pad_Clear": b"\x5D",
                                        "Pad_Right": b"\x5E",
                                        "Pad_Home": b"\x5F",
                                        "Pad_Up": b"\x60",
                                        "Pad_Prior": b"\x61",
                                        "Pad_Insert": b"\x62",
                                        "Del": b"\x63",
                                        "": b"\x64",
                                        "Pad_Apps": b"\x65",
                                        "": b"\x66",
                                        "": b"\x67"
                                       }
        
        self.NUMLOCK = 0b0001
        self.CAPSLOCK = 0b0010
        self.SCROLLLOCK = 0b0100


    """
    发送数据到串口。
    
    参数:
        data (str): 要发送的按键信息。
        ctrl (str): 要发送的控制键。
        com (serial): 要发送数据的串口。
    
    返回:
        bool: 如果数据成功发送，则为True，否则为False。
    """



    def type(self, strdata):
        # 将字符串转写为单个字符，调用send_data
        for i in range(0, len(strdata), 1):
            if(strdata[i] in self.normal_char_hex_dict):
                self.send_data(self.normal_char_hex_dict[strdata[i]][1], self.normal_char_hex_dict[strdata[i]][0])
            else:
                self.send_data(strdata[i])
            self.release()

 
    def send_data(self, data, ctrl='', com=serial):
        # 将字符转写为数据包
        HEAD = b'\x57\xAB'  # 帧头
        ADDR = b'\x00'  # 地址
        CMD = b'\x02'  # 命令
        LEN = b'\x08'  # 数据长度
        DATA = b''  # 数据

        # 控制键
        if ctrl == '':
            DATA += b'\x00'
        elif isinstance(ctrl, int):
            DATA += bytes([ctrl])
        else:
            DATA += self.control_button_hex_dict[ctrl]

        # DATA固定码
        DATA += b'\x00'

        # 读入data
        DATA += self.normal_button_hex_dict[data]
        if len(DATA) < 8:
            DATA += b'\x00' * (8 - len(DATA))
        else:
            DATA = DATA[:8]

        # 分离HEAD中的值，并计算和
        HEAD_hex_list = []
        for byte in HEAD:
            HEAD_hex_list.append(byte)
        HEAD_add_hex_list = sum(HEAD_hex_list)

        # 分离DATA中的值，并计算和
        DATA_hex_list = []
        for byte in DATA:
            DATA_hex_list.append(byte)
        DATA_add_hex_list = sum(DATA_hex_list)

        #
        try:
            SUM = sum([HEAD_add_hex_list, int.from_bytes(ADDR, byteorder='big'),
                       int.from_bytes(CMD, byteorder='big'), int.from_bytes(LEN, byteorder='big'),
                       DATA_add_hex_list]) % 256  # 校验和
        except OverflowError:
            print("int too big to convert")
            return False
        packet = HEAD + ADDR + CMD + LEN + DATA + bytes([SUM])  # 数据包
#         print("sending", str(bytes.hex(packet)))
        com.ser.write(packet)  # 将命令代码写入串口
        
        time.sleep(0.06)
        
        count=com.ser.inWaiting()
        if count>0:
            com_input = com.ser.read(count)
            if com_input!=b'':
#                 print("receive", str(bytes.hex(com_input)))
                if bytes.hex(com_input)[10:12]=='00':
                    return True # 如果成功，则返回True，否则引发异常
                else:
                    return False

        return False

    """
    释放按钮。
    
    参数:
        serial (object): 用于发送数据的串行对象。
    
    返回:
        None
    """

    def release(self):
        self.send_data('')

    def version(self):
        return "%0.1f"%(int(self.get_info())//10000/10-2)

    def usb_conn(self):
        if int.from_bytes(bytes.fromhex(self.get_info()),byteorder='big')//0xFFFF%0xFF:
            return True
        else:
            return False
            
    def num_lock(self):        
        if int.from_bytes(bytes.fromhex(self.get_info()),byteorder='big')%0xFF & self.NUMLOCK:
            return 'on'
        else:
            return 'off'

    def caps_lock(self):        
        if int.from_bytes(bytes.fromhex(self.get_info()),byteorder='big')%0xFF & self.CAPSLOCK:
            return 'on'
        else:
            return 'off'

    def scroll_lock(self):  
        if int.from_bytes(bytes.fromhex(self.get_info()),byteorder='big')%0xFF & self.SCROLLLOCK:
            return 'on'
        else:
            return 'off'

    def get_info(self, com=serial):
        HEAD = b'\x57\xAB'  # 帧头
        ADDR = b'\x00'  # 地址
        CMD = b'\x01'  # 命令
        LEN = b'\x00'  # 数据长度
        # 分离HEAD中的值，并计算和
        HEAD_hex_list = []
        for byte in HEAD:
            HEAD_hex_list.append(byte)
        HEAD_add_hex_list = sum(HEAD_hex_list)
        #
        try:
            SUM = sum([HEAD_add_hex_list,
                       int.from_bytes(ADDR, byteorder='big'),
                       int.from_bytes(CMD, byteorder='big'),
                       int.from_bytes(LEN, byteorder='big')]) % 256  # 校验和
        except OverflowError:
            print("int too big to convert")
            return False
        packet = HEAD + ADDR + CMD + LEN + bytes([SUM])  # 数据包
        # print("sending", str(bytes.hex(packet)))
        com.ser.write(packet)  # 将命令代码写入串口

        time.sleep(0.01)
        
        count=com.ser.inWaiting()
        if count>0:
            com_input = com.ser.read(count)
            if com_input!=b'': # 如果成功，则返回结果，否则引发异常
                return bytes.hex(com_input)[10:16]
            else:
                return False
        else:
            return False

    def close(self,com=serial):
        com.ser.close()
        
