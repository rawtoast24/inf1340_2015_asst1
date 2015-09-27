#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: 3, 4, 5, 6, 7, 8, 9, 10

    Expected Outputs: Triangle, Quadrilateral, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon

    Errors: less than 3 or greater than 10 sides

    """
    askUser = raw_input("How many sides does your shape have? Please use numerals.")

    if askUser == "3":
        print "Triangle"
    elif askUser == "4":
        print "Quadrilateral"
    elif askUser == "5":
        print "Pentagon"
    elif askUser == "6":
        print "Hexagon"
    elif askUser == "7":
        print "Heptagon"
    elif askUser == "8":
        print "Octagon"
    elif askUser == "9":
        print "Nonagon"
    elif askUser == "10":
        print "Decagon"
    else:
        print "Error"

name_that_shape()
