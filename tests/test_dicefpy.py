#!/usr/bin/python3
import pytest
import sys
sys.path.append( "../" ) # add parent past to python path

import dicefpy

# test parse_arg
# the arguement to dicefpy.parse_arg() is supossed to represent argv

## empty argv
def test_parseArg():
    assert dicefpy.parse_arg( [ "dicefpy" ] ) == [ "empty", 1 ]

## non-empty argv
def test_parseArg1():
    assert dicefpy.parse_arg( [ "dicefpy", "-n", 4 ] ) == [ "number", 4 ]

def test_parseArg2():
    assert dicefpy.parse_arg( [ "dicefpy", "-n", 10 ] ) == [ "number", 10 ]

def test_parseArg3():
    assert dicefpy.parse_arg( [ "dicefpy", "-n", 20 ] ) == [ "number", 20 ]

def test_parseArg4():
    assert dicefpy.parse_arg( [ "dicefpy", "-n", 9 ] ) == [ "number", 9 ]


## usage
def test_usage():
    assert dicefpy.parse_arg( ["dicefpy", "-h" ] ) == [ "help" ]
