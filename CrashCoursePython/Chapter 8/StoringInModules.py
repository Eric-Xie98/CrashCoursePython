## One advantage of functions is that they store reptitive code in separate blocks of code from the main code.
## With descriptive names, they can simplify program reading and can even be stored in a separate file called a module.

## The module can then be imported into the file with an import statement. Storing functions into a module can:
## let you use it in other programs
## share it easily with other programmers

## There are several ways to import modules:

## Importing an entire module:

import pizza    ## Name of the file with the functions we want / Python copies over the file into this program

pizza.make_pizza(16, 'pepperoni', 'cheese', 'bacon')

## This is the first approach to importing, simply importing the file name and all functions inside
## module_name.function_name()

## What if we wanted to import a specific function from a module?
## Use the from and import statements:

from pizza import make_pizza

## from module_name import function_name
## from module_name import function0, function 1, function2         allows you to import multiple functions

## With this notation, we don't need the dot notation as we explicitly called make_pizza from pizzas:

make_pizza(12, 'banana')

## The as keyword lets you give modules and functions an alias instead of ease of access:

from pizza import make_pizza as mp

mp(12, 'pudding')       ## new alias as mp

## import pizza as p turns the module name into 'p' if you want

## importing all functions in a module can done by using an *:

from pizza import *         ## I get all the functions and don't have to use dot notation

## however be careful, because if the program you're importing from is large, you can get unexpected errors in name etc.

# Styling Guide

# no spaces before or after the spaces in the default values:
# def function_name(string0, string1='default_value')
# same convention goes for calls: function_name(value0, string1='value1')

# if the parameters line goes longer than 79 characters, use the ENTER to put it on a new line
# def function(
#       parameter0, paramter1, 
#       paramter2, parameter3, 
#       parameter4, paramter5):        make sure the paramters are double tabbed so they stand out from the body text
#   body text here


## all imports should be at the beginning of a program


