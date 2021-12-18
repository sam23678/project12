num=float(input("Enter the height in centimeter: "))
num2=float(input("enter the weight in kilograms: "))
num3=float(input("enter the temperature in fahrenit: "))
inches=0.394*num
feet=0.0328*num
meter=0.01*num
pounds=2.2*num2
tons=0.001102*num2
gram=1000*num2
C = (num3-32)/1.8
k= (num3+459.67)/1.8
R=num3+459.67
print("The height in inches is : ",inches)
print("The height in feet is: ",feet)
print("The height in meter: ",meter)
print("The weight in pounds: ",pounds)
print("The weight in tons: ",tons)
print("The weight in grams: ",gram)
print("The temperature in celsius is:",C)
print("The temperature in kelvin: ",k)
print("The temperature in rankine: ",R)