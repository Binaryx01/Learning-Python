
#Ask the user to input three sides of a #triangle and determine its type:
#- Equilateral: All sides are equal.
#- Isosceles: Two sides are equal.
#- Scalene: No sides are equal.
#- Not a triangle: If the sides do not #satisfy the triangle inequality theorem.

print("progam to determine types of triangle")
a = int(input("Enter lenght of first side"))
b = int(input("Enter length of 2nd side"))
c = int(input("Enter the length of 3rd side"))

if(a==b==c):
	print("This is Equilateral triangle")	
elif(a==b or a==c or b==c):
	print("This is isosceles triangle")
else:
	print("Sclen triangle")



