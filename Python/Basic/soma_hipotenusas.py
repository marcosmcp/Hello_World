#!/usr/bin/env python
# -*- coding: utf-8 -*-

def soma_hipotenusas(n):
    soma = 0
    i = 1       
    while i <= n:   
        l1 = 1
        l2 = 1
        eHip = False
        while l1 < n and not eHip:
            l2 = l1           
            while l1**2 + l2**2 < i**2:
                l2 = l2 + 1
            eHip = (l1**2 + l2**2 == i**2)
            if eHip:                
                soma = soma + i
            l1 = l1 + 1
        i = i + 1

    return soma