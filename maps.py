#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:49:15 2021

@author: xavier
"""

import numpy as np


class Maps:
    def __init__(self, maps):
        self.maps = maps
        
    def generate_maps(self):
        

        if self.maps == 1:
            obstacles_simple, obstacles_medium, obstacles_hard, start, goal, rand_area = self.map_simple()
            
        elif self.maps == 2:
            obstacles_simple, obstacles_medium, obstacles_hard, start, goal, rand_area = self.map_medium()
            
        elif self.maps == 3:
            obstacles_simple, obstacles_medium, obstacles_hard, start, goal, rand_area = self.map_hard()
        
        return obstacles_simple, obstacles_medium, obstacles_hard, start, goal, rand_area
    
    @staticmethod
    def map_simple():
        
        obstacles_medium = []
        obstacles_hard = []
        obstacles_simple= [(6,40-0-16,8,16),
                              (9,40-22-14,7,14),
                              (19,40-10-30,7,30),
                              (31,40-4-24,6,24),]
        
        start = [5.0, 20.0, np.deg2rad(90.0)]
        goal = [38.0, 2.0, np.deg2rad(0.0)]      
        rand_area = [0, 40]
        return obstacles_simple, obstacles_medium, obstacles_hard, start, goal, rand_area
    
        
    @staticmethod
    def map_medium():
            obstacles_simple = []
            obstacles_hard = []
            obstacles_medium = [(11,40-0-8,3,8),
                              (6,40-8-8,8,8),
                              (9,40-22-6,3,6),
                              (12,40-22-14,4,14),
                              (19,40-10-8,7,8),
                              (23,40-18-22,3,22),
                              (34,40-4-16,3,16),
                              (31,40-20-8,6,8)]
            
            start = [5.0, 20.0, np.deg2rad(90.0)]
            goal = [38.0, 2.0, np.deg2rad(0.0)]      
            rand_area = [0, 40]
            return obstacles_simple, obstacles_medium, obstacles_hard, start, goal, rand_area
    
    @staticmethod
    def map_hard():
            obstacles_simple = []
            obstacles_medium = []
            obstacles_hard =  [(11,40-0-8,3,8),
                              (6,40-8-8,8,8),
                              (5,40-28-8,3,8), #a b c d*2  27
                              (5,40-22-6,14,6),
                              (12,40-28-12,4,12),
                              (19,40-10-8,7,8),
                              (23,40-18-22,3,22),
                              (19,40-32-4,4,4),
                              (31,40-4-4,6,4),
                              (35,40-8-14,2,14),
                              (31,40-12-10,2,10),
                              (31,40-22-6,9,6)]
            start = [5.0, 20.0, np.deg2rad(90.0)]
            goal = [38.0, 2.0, np.deg2rad(0.0)]      
            rand_area = [0, 40]
            return obstacles_simple, obstacles_medium, obstacles_hard, start, goal, rand_area
        
        