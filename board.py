# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:53:59 2022

@author: Peter Lo
"""
import numpy as np


class Board:
    '''Abstract definition of a board with numRows and numCols. Upon initialization, will create a numpy array to store the board info.'''
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.board = np.zeros((numRows, numCols))
