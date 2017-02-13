# Useful python recipes

#===========================================================================
# Recipe 1 take group of inputs and make a string, e.g. for a line in AERMOD
#===========================================================================
height=10 
width=0.5
x_coordinate=200500
y_coordinate=700500
temperature=100
velocity=6
source_name='stack_1' 
source_group='group_1'
    
# Create a template string from the result, replacing all of the data items with 
# {} placeholders.

myline = '{} {} {} {} {} {}'.format(source_name, source_group,
                                    x_coordinate, y_coordinate,
                                    temperature, velocity)

print myline


#============================================================================
# Recipe 2 Rewriting a string using a colon as a breakpoint
#============================================================================
title = "Recipe 5: Rewriting an Immutable String"
from string import whitespace, punctuation

# explode the string into a list object
title_list = list(title)

# find the partition character
colon_position = title_list.index(':')

# delete the characters no longer needed
del title_list[:colon_position+1]

# replace punctuation by stepping through each position in the list
for position in range(len(title_list)):
    if title_list[position] in whitespace+punctuation:
        title_list[position]='_'

# join it all together
title = ''.join(title_list)
print title


#============================================================================
# Recipe 3 An example docstring for a script
#============================================================================

''' 
Downloads and decodes the current Special Marine Warning (SMW) 
for the area 'AKQ' 

SYNOPSIS 
======== 

:: 

    python3 akq_weather.py 

DESCRIPTION 
=========== 

Downloads the Special Marine Warnings 

Files 
===== 

Writes a file, ``AKW.html``. 

EXAMPLES 
======== 

Here's an example:: 

    slott$ python3 akq_weather.py 
    <h3>There are no products active at this time.</h3> 
''' 

#============================================================================
# Recipe 4 get file sizes for items in a folder
#============================================================================
import pathlib
home = pathlib.Path('/Users/scottlynn73/Documents/Python/Python books/')
for path in home.glob('*.pdf'):
    print(path.stat().st_size, path.parent)

#============================================================================
# Recipe 5 build a list with append method- using previous example
#============================================================================

file_sizes = []
home = pathlib.Path('/Users/scottlynn73/Documents/Python/Python books/')
for path in home.glob('*.pdf'):
    file_sizes.append(path.stat().st_size) 

print(sum(file_sizes))

#============================================================================
# Recipe 6 writing a list comprehension
#============================================================================

my_list = [path.stat().st_size for path in home.glob('*.pdf')]
print my_list

# or
my_list = list(path.stat().st_size for path in home.glob('*.pdf'))

# get some info about the list
max(my_list)
min(my_list)

from statistics import mean
print round(mean(my_list),3)

# simple example
number_list = range(1,100,1)
print list(i*100 for i in number_list)

#============================================================================
# Recipe 7 insert items into a list at certain positions
#============================================================================
p = [3, 5, 11, 13] 
print p
p.insert(0, 2) 
print p
p.insert(3, 7) # insert a 7 at position 3
print p

#============================================================================
# Recipe 8 dealing with data that has messy headers,  slicing n dicing lists
#============================================================================

# the slice operator- works on lists, tuples, strings and other sequences

#  [start:stop] make a list between start and stop
#  [start:] make a list to the end starting at start
#  [:stop] make a list form the start ending at stop
#  [::step] make a list of the sequence using step value
#  [start::step]] make a list starting at start for the step value
#  [:stop:step] make a list stopping at stop using step value
#  [start:stop:step] make a list between the start and stop using the step

from pathlib import Path
import csv
with Path('/Users/scottlynn73/Documents/Python/ModernPythonCookbook_Code/Code/fuel2.csv').open() as source_file:
    reader = csv.reader(source_file)
    log_rows = list(reader)

# get the head and tail
head, tail = log_rows[:2], log_rows[2:]
print head
print tail

print " "

# take a slice every second step starting at 0
print log_rows[0::2]

print " "

# take a slice every second step starting at 1
print log_rows[1::3]

print " "

# zip two sliced lists together (based on previous two slices)
paired_rows =  list(zip(log_rows[0::2], log_rows[1::3]))

# print with list comprehension
print [a+b for a,b in paired_rows]

# remove items from list
del log_rows[2:]

# remove items matching an input
row = ['10/25/13', '08:24:00 AM', '29', '', '01:15:00 PM', '27']
print row
row.remove('')
print row

#============================================================================
# Recipe 9 Getting user inputs, building dates
#============================================================================
year = int(input("year: ")) 

# validate inputs on the way in
month = None 
while month is None: 
    month_text = input("month [1-12]: ") 
    try: 
        month = int(month_text) 
        if 1 <= month <= 12: 
            pass 
        else: 
            raise ValueError("Month of range 1-12") 
    except ValueError as ex: 
        print(ex) 
        month = None 

#============================================================================
# Recipe 10 writing a simple class
#============================================================================

# problem statement
# The game of craps has two dice
# Each die has six faces with values 1 - 6
# Dice are rolled by a player
# Total of dice changes the state of the craps game
# If the two dice match, the number was rolled the hard way.
# If the two dice do not match, the number was easy.
# Some bets depend on this hard-easy distinction.

# Tips

# Nouns in the sentences identify classes- e.g. game, player
# Verbs are methods, e.g. rolled, match
# Adjectives are like properties of an object, e.g. total of dice


# first the class statement
class Dice:
    # initialise with __init__
    def __initi__(self):
        self.faces = None
    # define the methods
    def roll(self):
        self.faces = (random.randint(1,6), random.randint(1,6))
    def total(self):
        return sum(self.faces)
    def hardway(self):
        return self.faces[0] == self.faces[1]
    def easyway(self):
        return self.afces[0] != self.faces[1]

import random
random.seed(1)
d1 = Dice()
d1.roll()
d1.total()
