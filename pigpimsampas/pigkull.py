#pigkull.py

class Student: #class main จะRun ทุกครั้ง
	def __init__(self,name):
		self.name = name
		self.exp = 0
		self.lesson = 0
		#st.name 
		#self = st แทนที่ตัว Objectของมัน

		#call function
		#self.learning(10) # add มาแต่แรกเลยตามจำนวนที่ระบุ

	def Hello(self):
		print('สวัสดีจ้า {}'.format(self.name))
		print('---------------')

	def Coding(self):
		
		self.exp +=5
		self.lesson += 1 #
	def ShowExp(self):
		print(self.name,self.exp,'เรียนมาแล้ว {} ครั้ง'.format(self.lesson))


	def learning(self,score):
		self.exp += score
		self.lesson += 1



class Specialstudent(Student):   #inheritant class สืบทอดคลาส
	
	def __init__(self,name,father):
		super().__init__(name)
		self.father = father
		mafia = ['Bill Gate','Thomas Edison']
		if father in mafia:
			self.exp += 100

	def learning(self,score):
		self.exp += (score*3)
		self.lesson += 1

	def AskExp(self,score=10):
		print('ขอคะแนนหน่อยดิวะ')
		self.learning(score)

if __name__ == '__main__':
	print('--------- 1 jan 2021 ---------')

	st0 = Specialstudent('Mark','Bill Gate')
	st0.ShowExp()

	st0.AskExp()

	st0.ShowExp()

	st = Student('Robert')
	print(st.name)
	st.Hello()
	print('--------- 2 jan 2021 ---------')
	st = Student('pravit')
	st2 = Student('prayut')
	print(st2.name)
	st2.Hello()

	st.learning(9)


	print(st.name,st.exp)
	print(st2.name,st2.exp)

	print('--------- 4 jan 2021 ---------')

	for i in range(5):
		st2.Coding()

	st.ShowExp()
	st2.ShowExp()
	


