# CPSC254
import math

more = True
while(more):
	print('1. Solve Side-Angle-Side triangle.')
	print('2. Solve Angle-Side-Angle triangle.')
	print('3. Solve Angle-Angle-Side triangle.')
	print('4. Solve Side-Side-Side triangle.')

	option = int(input('Choose a method >> '))

	if option == 1:
		side1 = float(input('Enter side 1: '))
		angle1 = float(input('Enter angle 1: '))*(math.pi/180)
		side2 = float(input('Enter side 2: '))
		
		side3 = math.sqrt(side1**2+side2**2-2*side1*side2*math.cos(angle1))
		angle2 = math.asin((side1*math.sin(angle1))/side3)*(180/math.pi)
		angle3 = math.asin((side2*math.sin(angle1))/side3)*(180/math.pi)
		perimeter = side1+side2+side3
		
		print('Side 3 = %f' % side3)
		print('Angle 2 = %f' % angle2)
		print('Angle 3 = %f' % angle3)
		print('Perimeter = %f' % perimeter)
		
	elif option == 2:
		angle1 = float(input('Enter angle 1: '))*(math.pi/180)
		side1 = float(input('Enter side 1: '))
		angle2 = float(input('Enter angle 2: '))*(math.pi/180)
		
		angle3 = math.pi-angle1-angle2
		side2 = (side1*math.sin(angle1))/math.sin(angle3)
		side3 = (side2*math.sin(angle2))/math.sin(angle1)
		angle3 = angle3*(180/math.pi)
		perimeter = side1+side2+side3
		
		print('Angle 3 = %f' % angle3)
		print('Side 2 = %f' % side2)
		print('Side 3 = %f' % side3)
		print('Perimeter = %f' % perimeter)
		
	elif option == 3:
		angle1 = float(input('Enter angle 1: '))*(math.pi/180)
		angle2 = float(input('Enter angle 2: '))*(math.pi/180)
		side1 = float(input('Enter side 1: '))
		
		angle3 = math.pi-angle1-angle2
		side2 = (side1*math.sin(angle3))/math.sin(angle1)
		side3 = (side1*math.sin(angle2))/math.sin(angle1)
		perimeter = side1+side2+side3
		angle3 = angle3*(180/math.pi)
		
		print('Angle 3 = %f' % angle3)
		print('Side 2 = %f' % side2)
		print('Side 3 = %f' % side3)
		print('Perimeter = %f' % perimeter)
		
	elif option == 4:
		side1 = float(input('Enter side 1: '))
		side2 = float(input('Enter side 2: '))
		side3 = float(input('Enter side 3: '))
		
		angle2 = math.acos((side1**2+side2**2-side3**2)/(2*side1*side2))
		angle3 = math.asin((side1*math.sin(angle2))/side3)*(180/math.pi)
		angle1 = math.asin((side2*math.sin(angle2))/side3)*(180/math.pi)
		angle2 = angle2*(180/math.pi)
		
		print('Angle 1 = %f' % angle1)
		print('Angle 2 = %f' % angle2)
		print('Angle 3 = %f' % angle3)
	if (input('Another triangle? (y/n): ') != 'y'):
		more = False