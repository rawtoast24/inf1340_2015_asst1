#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Mib_Ani'



def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs: y,n

    Expected Outputs: "Clean terminals and try starting again", "Replace cables and try again", "Replace the battery",
    Check spark plug connections", "Check to ensure the choke opening and closing", "Get it in for service"

    Errors: "User input not recognized. Please enter y or n for each question"

    """
    error = "User input not recognized. Please enter y or n for each question(Please enter in lowercase)."
    carSilent = raw_input("Is the car silent when you turn the key? Please answer using y or n.")
    if carSilent == "n":
        clickingNoise = raw_input("Does the car make a clicking noise? Please answer using y or n.")
        if clickingNoise == "y":
            print("Replace the battery.")
        elif clickingNoise == "n":
            crankButFail = raw_input("Does the car crank up but fail to start? Please answer using y or n.")
            if crankButFail == "y":
                print("Check spark plug connections.")
            elif crankButFail == "n":
                engineDie = raw_input("Does the engine start and then die? Please answer using y or n.")
                if engineDie == "n":
                    print("Engine is not getting enough fuel. Please clean fuel pump.")
                elif engineDie == "y":
                    fuelInjection = raw_input("Does your car have fuel injection? Please answer using y or n.")
                    if fuelInjection == "y":
                        print("Get it in for service.")
                    elif fuelInjection == "n":
                        print("Check to ensure the choke is opening and closing.")
                    else:
                        print(error)
                else:
                    print(error)
            else:
                print(error)
        else:
            print(error)
    elif carSilent == "y":
        batteryTerminal = raw_input("Are the battery terminals corroded? Please answer using y or n.")
        if batteryTerminal == "n":
            print("The battery cables may be damaged. Replace cables and try again.")
        elif batteryTerminal == "y":
            print("The terminals may be dirty. Clean terminals and try again.")
        else:
            print(error)
    else:
        print(error)
diagnose_car()