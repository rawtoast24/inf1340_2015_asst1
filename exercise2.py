#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Mib_Ani'


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: The number of sides( 3, 4, 5, 6, 7, 8, 9, 10)

    Expected Outputs: triangle, quadrilateral, pentagon, hexagon, heptagon, octagon, nonagon, decagon

    Errors: less than 3 or greater than 10 sides

    """

#Asks user for the number of sides their shape has and returns the name of that shape

    askUser = raw_input("How many sides does your shape have? Please specify the count in numerals.")

    if askUser == "3":
        print "triangle"
    elif askUser == "4":
        print "quadrilateral"
    elif askUser == "5":
        print "pentagon"
    elif askUser == "6":
        print "hexagon"
    elif askUser == "7":
        print "heptagon"
    elif askUser == "8":
        print "octagon"
    elif askUser == "9":
        print "nonagon"
    elif askUser == "10":
        print "decagon"
#Prints error if the user enters a number of sides less than 3 or greater than 10
    else:
        print "Error"


#name_that_shape()

