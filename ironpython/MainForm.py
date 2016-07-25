import System.Drawing
import System.Windows.Forms

from randomCode import randomCodeGeneratorImpl

class randomCodeGeneratorForm(System.Windows.Forms.Form):
	def __init__(self):
		self.Text = 'Random Code Generator'
		self.Name = 'Random Code Generator'
		
		
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox5 = System.Windows.Forms.CheckBox()
		self._checkBox6 = System.Windows.Forms.CheckBox()
		self._checkBox7 = System.Windows.Forms.CheckBox()
		self._checkBox8 = System.Windows.Forms.CheckBox()
		self._checkBox9 = System.Windows.Forms.CheckBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._button1 = System.Windows.Forms.Button()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(20, 20)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(145, 22)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "十进制数字 0-9"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(180, 20)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(145, 22)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "特殊字符 @#%等"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(340, 20)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(145, 22)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "小写十六进制 0-f"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# checkBox4
		# 
		self._checkBox4.Location = System.Drawing.Point(500, 20)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(145, 22)
		self._checkBox4.TabIndex = 3
		self._checkBox4.Text = "大写十六进制 0-F"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# checkBox5
		# 
		self._checkBox5.Location = System.Drawing.Point(20, 65)
		self._checkBox5.Name = "checkBox5"
		self._checkBox5.Size = System.Drawing.Size(145, 22)
		self._checkBox5.TabIndex = 4
		self._checkBox5.Text = "小写英文字母 a-z"
		self._checkBox5.UseVisualStyleBackColor = True
		# 
		# checkBox6
		# 
		self._checkBox6.Location = System.Drawing.Point(180, 65)
		self._checkBox6.Name = "checkBox6"
		self._checkBox6.Size = System.Drawing.Size(145, 22)
		self._checkBox6.TabIndex = 5
		self._checkBox6.Text = "大写英文字母 A-Z"
		self._checkBox6.UseVisualStyleBackColor = True
		# 
		# checkBox7
		# 
		self._checkBox7.Location = System.Drawing.Point(340, 65)
		self._checkBox7.Name = "checkBox7"
		self._checkBox7.Size = System.Drawing.Size(145, 22)
		self._checkBox7.TabIndex = 6
		self._checkBox7.Text = "二进制数字 0-1"
		self._checkBox7.UseVisualStyleBackColor = True
		# 
		# checkBox8
		# 
		self._checkBox8.Location = System.Drawing.Point(500, 65)
		self._checkBox8.Name = "checkBox8"
		self._checkBox8.Size = System.Drawing.Size(145, 22)
		self._checkBox8.TabIndex = 7
		self._checkBox8.Text = "八进制数字 0-7"
		self._checkBox8.UseVisualStyleBackColor = True
		# 
		# checkBox9
		# 
		self._checkBox9.Location = System.Drawing.Point(20, 110)
		self._checkBox9.Name = "checkBox9"
		self._checkBox9.Size = System.Drawing.Size(145, 22)
		self._checkBox9.TabIndex = 8
		self._checkBox9.Text = "自定义字符"
		self._checkBox9.UseVisualStyleBackColor = True
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._checkBox8)
		self._groupBox1.Controls.Add(self._checkBox9)
		self._groupBox1.Controls.Add(self._checkBox4)
		self._groupBox1.Controls.Add(self._checkBox7)
		self._groupBox1.Controls.Add(self._checkBox6)
		self._groupBox1.Controls.Add(self._checkBox5)
		self._groupBox1.Controls.Add(self._checkBox3)
		self._groupBox1.Controls.Add(self._checkBox2)
		self._groupBox1.Controls.Add(self._checkBox1)
		self._groupBox1.Location = System.Drawing.Point(12, 26)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(623, 143)
		self._groupBox1.TabIndex = 9
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "选择包含的字符"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(6, 20)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(610, 21)
		self._textBox1.TabIndex = 10
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._textBox1)
		self._groupBox2.Location = System.Drawing.Point(12, 191)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(622, 54)
		self._groupBox2.TabIndex = 11
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "随机码长度"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 410)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(83, 34)
		self._button1.TabIndex = 12
		self._button1.Text = "生成随机码"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._textBox2)
		self._groupBox3.Location = System.Drawing.Point(13, 265)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(622, 139)
		self._groupBox3.TabIndex = 12
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "随机码"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(6, 27)
		self._textBox2.Multiline = True
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(610, 95)
		self._textBox2.TabIndex = 0
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(120, 110)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(497, 21)
		self._textBox3.TabIndex = 11
		# 
		# randomCodeGeneratorForm
		# 
		self.ClientSize = System.Drawing.Size(647, 456)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "randomCodeGeneratorForm"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox2.PerformLayout()
		self._groupBox3.ResumeLayout(False)
		self._groupBox3.PerformLayout()
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		length = self._textBox1.Text
		
		randomCodeGenerator = randomCodeGeneratorImpl()
		success, msg = randomCodeGenerator.setLength(length)
		if not success:
			self._textBox2.Text = msg
			return
		if self._checkBox1.Checked:
			randomCodeGenerator.pushDecimalNums()
		if self._checkBox2.Checked:
			randomCodeGenerator.pushSpecialCharacters()
		if self._checkBox3.Checked:
			randomCodeGenerator.pushSmallLetterHexadecimalNums()
		if self._checkBox4.Checked:
			randomCodeGenerator.pushBigLetterHexadecimalNums()
		if self._checkBox5.Checked:
			randomCodeGenerator.pushSmallLetters()
		if self._checkBox6.Checked:
			randomCodeGenerator.pushBigLetters()
		if self._checkBox7.Checked:
			randomCodeGenerator.pushBinaryNums()
		if self._checkBox8.Checked:
			randomCodeGenerator.pushOctalNums()
		if self._checkBox9.Checked:
			customCharacters = self._textBox3.Text
			randomCodeGenerator.pushCustomCharacters(customCharacters)
			
		success, self._textBox2.Text = randomCodeGenerator.getRandomCode()

