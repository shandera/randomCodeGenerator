# -*- coding: UTF-8 -*-
import random


class basisRandomCodeGeneratorImpl():
    def __init__(self):
        """\brief 
            chars 字符取值范围集
            length 最终生成字符串长度
        """
        self.chars = set()
        self.length = 0
        self.randomCode = ""
        self.status = True
        self.msg = ""
    
    def setAns(self, status, msg):
        self.status = status
        self.msg = msg
    
    def getAns(self):
        return self.status, self.msg
        
    def setLength(self, length):
        """\brief 设置长度
        """
        if isinstance(length, str) and length.isdigit():
            if len(length) > 4:
                self.setAns(False, "随机码长度不得超过10000")
            else:
                self.length = int(length)
        else:
            self.setAns(False, "随机码长度不合规范")
            
        return self.getAns()
            
            
class randomCodeGeneratorImpl(basisRandomCodeGeneratorImpl):
    # 组合字符集    
    def pushDecimalNums(self):
        """\brief 插入十进制数字
        """
        self.chars.update(range(10))
    
    def pushSmallLetters(self):
        """\brief 插入小写字母
        """
        self.chars.update('abcdefghijklmnopqrstuvwxyz')
        
    def pushBigLetters(self):
        """\brief 插入大写字母
        """
        self.chars.update('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    def pushBinaryNums(self):
        """\brief 插入二进制数字
        """
        self.chars.update(range(1))
        
    def pushOctalNums(self):
        """\brief 插入八进制数字
        """
        self.chars.update(range(8))
        
    def pushSmallLetterHexadecimalNums(self):
        """\brief 插入小写十六进制数字
        """
        self.chars.update(range(10))
        self.chars.update('abcdef')
    
    def pushBigLetterHexadecimalNums(self):
        """\brief 插入大写十六进制数字
        """
        self.chars.update(range(10))
        self.chars.update('ABCDEF')
    
    def pushSpecialCharacters(self):
        """\brief 插入特殊字符
        """
        self.chars.update('!@#$%^&*()><?')
    
    def pushCustomCharacters(self, customCharacters):
        """\brief 插入自定义字符
        """
        self.chars.update(customCharacters)
        
    def getRandomCode(self):
        """\brief 返回随机字符串
        """
        self.genRandomCode()
        return self.getAns()
        
    def genRandomCode(self):
        """\brief 随机字符串生成器
        """
        charLength = len(self.chars)
        if not charLength or not self.length:
            self.setAns(False, "随机码长度和取值范围不得为空")
            return
        # 先生成个随机数字列表
        randomCodeList = [random.randint(0, charLength - 1) for i in xrange(self.length)]
        # 生成随机字符串
        charList = list(self.chars)
        self.randomCode = ''.join(map(lambda temp: str(charList[temp]), randomCodeList))
        self.setAns(True, self.randomCode)
        
    
