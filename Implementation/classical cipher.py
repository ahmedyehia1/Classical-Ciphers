import sys
import numpy as np

# complimentary functions
def intChar(c):
    return (ord(c)-65)%32
def charInt(i):
    return chr(i%26+97)
