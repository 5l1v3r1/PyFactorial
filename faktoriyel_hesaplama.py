#!/usr/bin/env python
# -*- coding:utf-8 -*-

factorial_ico = """
#########################################################
#          PYTHON - Factorial - GH0ST S0FTWARE          #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

star = "#########################################################"

print factorial_ico

print star

girilen_sayi = int(input('Sayı değerini giriniz : '))

print star

carp = 1

for bul in range(girilen_sayi):
	carp = carp*(bul+1)

print 'Girilen sayının faktoriyeli : ',carp

print star
