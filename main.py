#main.py
#
#Author:        Farjad Tariq
#Version:       2023/08/17
#
#Purpose:       The purpose of this is to write a complete Python program that computes
#               the approximate area under a parabola using the trapezoid technique.

from time import ctime

def computeXcoordinates(h, intervals):
    '''Creates a list of x Coordinates'''
    #xCoords = list of x coordinates
    #intervals = number of equally spaced intervals
    xCoords=[]
    for i in range(intervals+1):
        x = i * (2*h)/intervals
        xCoords.append(x)
    return xCoords    

def computeYcoordinates(xCoords, h, k):
    '''Equates the y Coordinates from an equation and
        creates a list out of it'''
    #yCoords= list of y coordinates
    #h = one half the width of the parabola
    #k = the height of the parabola
    #a = variable used to define (-k / h**2)
    yCoords=[]
    a = -k / h**2

    for i in xCoords:
        yCoords.append(a * (i-h)**2 + k)
    return yCoords

def computeArea(h, k, intervals):
    '''Calculates the approximate area using the trapezoid technique
        from the list of x and y coordinates'''
    #approxArea = approximate area of the parabola
    #deltaX = value of the equally spaced intervals
    #area = summation of the parallel lines (y-coordinates)(yCoords[i]+yCoords[i+1])
    xCoords = computeXcoordinates(h, intervals)
    yCoords = computeYcoordinates(xCoords, h, k)
    approxArea = 0
    for i in range(intervals):
        area = yCoords[i] + yCoords[i+1] 
        approxArea += area
    approxArea = approxArea * h/intervals
    return approxArea  

def main():
    '''Main program gets the input for the intervals, the half width
        and the height of the parabola. Calculates the the actual area,
        the difference between the approximate and actual area and 
        then prints all the results.'''
    #actualArea = the actual area of the parabola
    #error = the difference between the actual and the approximate area of the parabola
    print("\n" + "-" * 80)
    intervals = int(input("Enter the number of intervals (0 to quit): "))

    while intervals > 0:
        h = float(input("Enter half the width of the parabola in cm (>0): "))
        if h <= 0:
            print("The half width, %i, must be greater than zero!" % (h))
            intervals = int(input("Enter the number of intervals (0 to quit): "))
        else:
            k = float(input("Enter the height of the parabola in cm(>0): "))
            if k <= 0:
                print("The height, %i, must be greater than zero!" % (k))
                intervals = int(input("Enter the number of intervals (0 to quit): "))
            else:
                approxArea = computeArea(h, k, intervals)
                actualArea = 4*h*k/3
                error = abs(actualArea - approxArea)

                print("\nThe approximate area of the parabola is %.14e cm^2." % (approxArea) )
                print("\tThe actual area of the parabola is %.14e cm^2." % (actualArea) )
                print("\t The error in the approximation is %.6e cm^2." % (error) )

                intervals = int(input("Enter the number of intervals (0 to quit): "))

def displayTerminationMessage():
    print("""
Programmed by Farjad Tariq
Date: %s
End of processing.""" % ctime())

main()
displayTerminationMessage()                