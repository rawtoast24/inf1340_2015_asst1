#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Mib_Ani'


# Created function to diagnose car problems by walking user through a decision tree
def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs: Y or N(The input is case insensitive)

    Expected Outputs:
    Y,Y == "Clean terminals and try starting again";
    Y,N == "Replace cables and try again";
    N,Y == "Replace the battery";
    N,N,Y == "Check spark plug connections";
    N,N,N,N == "Engine is not getting enough fuel. Please clean fuel pump";
    N,N,N,Y,N == "Check to ensure the choke opening and closing";
    N,N,N,Y,Y =="Get it in for service"


    Errors: "User input not recognized. Please enter Y or N for each question"

    """
# Error message created in case user doesn't enter Y,Y, N, or n at any instance

    error = "User input not recognized. Please enter Y or N for each question."
    carSilent = raw_input("Is the car silent when you turn the key? Please answer using Y or N.")
    if carSilent in ["n","N"] :
        clickingNoise = raw_input("Does the car make a clicking noise? Please answer using Y or N.")
        if clickingNoise in ["y","Y"]:
            print("Replace the battery.")
        elif clickingNoise in ["n","N"]:
            crankButFail = raw_input("Does the car crank up but fail to start? Please answer using Y or N.")
            if crankButFail in ["y","Y"]:
                print("Check spark plug connections.")
            elif crankButFail in ["n","N"]:
                engineDie = raw_input("Does the engine start and then die? Please answer using Y or N.")
                if engineDie in ["n","N"]:
                    print("Engine is not getting enough fuel. Clean fuel pump.")
                elif engineDie in ["y","Y"]:
                    fuelInjection = raw_input("Does your car have fuel injection? Please answer using Y or N.")
                    if fuelInjection in ["y","Y"]:
                        print("Get it in for service.")
                    elif fuelInjection in ["n","N"]:
                        print("Check to ensure the choke is opening and closing.")
                    else:
                        print(error)
                else:
                    print(error)
            else:
                print(error)
        else:
            print(error)
    elif carSilent in ["y","Y"]:
        batteryTerminal = raw_input("Are the battery terminals corroded? Please answer using Y or N.")
        if batteryTerminal in  ["n","N"]:
            print("Replace cables and try again.")
        elif batteryTerminal in ["y","Y"]:
            print("Clean terminals and try starting again.")
        else:
            print(error)
    else:
        print(error)
#diagnose_car()