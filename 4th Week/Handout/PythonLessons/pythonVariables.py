#What is a variable
no_redApples = 5
no_greenApples = 4

totalApples = no_redApples + no_greenApples
print('Red Apples = ',no_redApples)
print('Green Apples = ' ,no_greenApples)
print('There are altogether', totalApples, ' Apples')


input('Hit Enter to Continue')
length=20

width=6
area=length * width
print('Area of Rectangle', length, 'cm by ',width, 'cm =', area, 'sq cm')

#The For Loop
input('Hit Enter to Continue')
times=input('Enter the times table you want')
times=int(times)

for number in range(1,13):
    print(number, ' x ', times,' = ' , (number * times))
    
