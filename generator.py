# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:29:53 2018

@author: DLaptop
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr


def gen_maps(maps, precision, dimension):
    
    if dimension == 1:
        coord1, coord2 = one_dim_gen(maps, precision)
        plt.scatter(coord1, coord2, s=0.05)
        plt.axis('off')
        plt.show()
    
    if dimension == 2:
        maps1 = maps[:int(len(maps)/2)]
        maps2 = maps[int(len(maps)/2):]
        coord1, coord2 = two_dim_gen(maps1, maps2, precision)
        plt.scatter(coord1, coord2, s=0.05)
        plt.axis('off')
        plt.show()
    
    if dimension == 3:
        maps1 = maps[:int(len(maps)/3)]
        maps2 = maps[int(len(maps)/3):2*int(len(maps)/3)]
        maps3 = maps[2*int(len(maps)/3):]
        coord1, coord2, coord3 = three_dim_gen(maps1, maps2, maps3, precision)
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(coord1, coord2, coord3, s=0.05)
        ax.view_init(30,185)
        plt.axis('off')
        plt.show()


def one_dim_gen(maps, precision):    
    x = sp.symbols('x')
    number_of_maps = len(maps)
    
    coord1 = np.zeros(precision)
    coord2 = np.zeros(precision)
    coord1[0] = 0.25
    
    maps_as_expr = [parse_expr(func, evaluate = False) for func in maps]

    for ind in range(1,precision):
        random = np.random.randint(number_of_maps)
        f = sp.lambdify(x, maps_as_expr[random])
        coord1[ind] = f(coord1[ind-1])
        
    return coord1, coord2
    

def two_dim_gen(maps1, maps2, precision):    
    x,y = sp.symbols('x y')
    number_of_maps = len(maps1)
    
    coord1 = np.zeros(precision)
    coord2 = np.zeros(precision)
    coord1[0] = 0.25
    coord2[0] = 0.25
    
    maps1_as_expr = [parse_expr(func, evaluate = False) for func in maps1]
    maps2_as_expr = [parse_expr(func, evaluate = False) for func in maps2]        
        
    for ind in range(1,precision):
        random = np.random.randint(number_of_maps)
        f = sp.lambdify([x,y], maps1_as_expr[random])
        g = sp.lambdify([x,y], maps2_as_expr[random])
        coord1[ind] = f(coord1[ind-1], coord2[ind-1])
        coord2[ind] = g(coord1[ind-1], coord2[ind-1])
        
    return coord1, coord2
    

def three_dim_gen(maps1, maps2, maps3, precision):  
    x,y,z = sp.symbols('x y z')
    number_of_maps = len(maps1)
    
    coord1 = np.zeros(precision)
    coord2 = np.zeros(precision)
    coord3 = np.zeros(precision)
    coord1[0] = 0.25
    coord2[0] = 0.25
    coord3[0] = 0.25
    
    maps1_as_expr = [parse_expr(func, evaluate = False) for func in maps1]
    maps2_as_expr = [parse_expr(func, evaluate = False) for func in maps2]        
    maps3_as_expr = [parse_expr(func, evaluate = False) for func in maps3]        
    
    for ind in range(1,precision):
        random = np.random.randint(number_of_maps)
        f = sp.lambdify([x,y,z], maps1_as_expr[random])
        g = sp.lambdify([x,y,z], maps2_as_expr[random])
        h = sp.lambdify([x,y,z], maps3_as_expr[random])
        coord1[ind] = f(coord1[ind-1], coord2[ind-1], coord3[ind-1])
        coord2[ind] = g(coord1[ind-1], coord2[ind-1], coord3[ind-1])
        coord3[ind] = h(coord1[ind-1], coord2[ind-1], coord3[ind-1])
        
    return coord1, coord2, coord3 
    


