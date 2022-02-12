#python functions

#this is called a function
def calcVolume(length, breadth, height):
    volume=length * breadth * height
    return volume


while True:
    print('To Calculate Volume, please provide these information')
    l=input("Length = ")
    b=input("Breadth = ")
    h=input("Height = ")
    
    vol= calcVolume(int(l), int(b),int(h))
    print('Volume is ', vol)
    
    cont=input("Hit Enter to Continue, S to stop")
    if cont=="S" or cont=='s':
        break
    

#Exercise - Create a function to calculate Area of Circle.  pi=3.142   