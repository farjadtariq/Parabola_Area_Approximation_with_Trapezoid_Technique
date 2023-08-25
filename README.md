# Parabola_Area_Approximation_with_Trapezoid_Technique

## Overview

This project, written in Python, approximates the area under a parabola using the trapezoid technique. The user can specify the dimensions of the parabola (half-width `h` and height `k`) and the number of intervals for the approximation.

## Prerequisites
- Python 3.x

## How to Run
1. Clone this repository.
2. Open your terminal and navigate to the project directory.
3. Run `python main.py`.
4. Follow the on-screen prompts to input the number of intervals, half-width, and height of the parabola.

## Features
- **User-Friendly Input**: The program accepts user input for the number of intervals and the dimensions of the parabola.
- **Accuracy and Error Calculation**: The approximate area, actual area, and error in approximation are displayed.

## Functions
- `computeXcoordinates`: Function to generate the x-coordinates based on the intervals.
- `computeYcoordinates`: Function to calculate the y-coordinates using the equation of the parabola.
- `computeArea`: Function to approximate the area using the trapezoid technique.
- `main`: The main driver function. Takes user input and calculates the approximate area and error.

## Author
Farjad Tariq

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
