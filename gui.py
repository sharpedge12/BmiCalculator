from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="anshul",passwd="mysql",database = "GUI")
mycursor = mydb.cursor()

root = Tk()
root.title("Health Companion")
#root.iconbitmap("D:\ip\gui\project\ico.ico")

welcomeL=Label(root,text="Welcome to Health Companion ! ")
welcomeL.grid(row=0,column=0,columnspan=3)
weightL=Label(root,text="Input Your Name = ")
weightL.grid(row=1,column=0)
weightL=Label(root,text="Input Your Weight (KG)= ")
weightL.grid(row=2,column=0)
heightL=Label(root,text="Input Your Height (Metre)= ")
heightL.grid(row=3,column=0)
ageL=Label(root,text="Input Your Age = ")
ageL.grid(row=4,column=0)



name=Entry(root)
name.grid(row=1,column=1)
weight=Entry(root)
weight.grid(row=2,column=1)
height=Entry(root)
height.grid(row=3,column=1)
age=Entry(root)
age.grid(row=4,column=1)


def enter():
	w=int(weight.get())
	h=int(height.get())
	a=int(age.get())
	BMI=int(w/(h*h))
	BMi=str(int(BMI))
	n = str(name.get())

	sqlform = "insert into d2 values (%s,%s,%s,%s,%s)"
	valuess = [n,w,h,a,BMI]
	mycursor.execute(sqlform,valuess)

	mydb.commit()

	if a > 20 or a == 20:
		if BMI < 18.5 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are underweight.Focus on Balanced and Nutrional Diet !").grid(row=5,column=0,columnspan=3)
		elif BMI > 25 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are Overweight.Please Focus on excercise and prohibit Junk food !").grid(row=5,column=0,columnspan=3)
		elif BMI < 25 and BMI > 18.5 :
			LL=Label(root,text="Your BMI is "+BMi+" .Well Done, You are Healthy !").grid(row=5,column=0,columnspan=3)

	if a > 0 and a < 5:
		if BMI < 14 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are underweight.Focus on Balanced and Nutrional Diet !").grid(row=5,column=0,columnspan=3)
		elif BMI > 17 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are Overweight.Please Focus on excercise and prohibit Junk food !").grid(row=5,column=0,columnspan=3)
		elif BMI < 17 and BMI > 14 :
			LL=Label(root,text="Your BMI is "+BMi+" .Well Done, You are Healthy !").grid(row=5,column=0,columnspan=3)


	if a > 5 and a < 10:
		if BMI < 16 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are underweight.Focus on Balanced and Nutrional Diet !").grid(row=5,column=0,columnspan=3)
		elif BMI > 20 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are Overweight.Please Focus on excercise and prohibit Junk food !").grid(row=5,column=0,columnspan=3)
		elif BMI < 20 and BMI > 16 :
			LL=Label(root,text="Your BMI is "+BMi+" .Well Done, You are Healthy !").grid(row=5,column=0,columnspan=3)


	if a > 11 and a < 15:
		if BMI < 17 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are underweight.Focus on Balanced and Nutrional Diet !").grid(row=5,column=0,columnspan=3)
		elif BMI > 22 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are Overweight.Please Focus on excercise and prohibit Junk food !").grid(row=5,column=0,columnspan=3)
		elif BMI < 22 and BMI > 17 :
			LL=Label(root,text="Your BMI is "+BMi+" .Well Done, You are Healthy !").grid(row=5,column=0,columnspan=3)


	if a > 16 and a < 20:
		if BMI < 18 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are underweight.Focus on Balanced and Nutrional Diet !").grid(row=5,column=0,columnspan=3)
		elif BMI > 25 :
			LL=Label(root,text="Your BMI is "+BMi+" .You are Overweight.Please Focus on excercise and prohibit Junk food !").grid(row=5,column=0,columnspan=3)
		elif BMI < 25 and BMI > 18 :
			LL=Label(root,text="Your BMI is "+BMi+" .Well Done, You are Healthy !").grid(row=5,column=0,columnspan=3)





btn=Button(root,text="Check my BMI",command=enter)
btn.grid(row=5,column=0,columnspan=2)


root.mainloop()

#Made by anshul sharma //