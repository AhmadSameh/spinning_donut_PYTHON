import os
import math

height = 24
width = 80

clear = "cls"
if os.name == "posix":
    clear = "clear"
os.system(clear)

A = B = 0
R = 2
r = 1
K2 = 5
K1 = width*K2*3/(8*(r+R))

while True:
    # INITIALIZE TERMINAL SCREEN
    zbuffer = [0 for _ in range(4*width*height)]
    screen = [' ' for _ in range(width*height)]
    theta = 0
    while theta < 6.28:
        theta += 0.07
        cosTheta = math.cos(theta)
        sinTheta = math.sin(theta) 
        circleX = R + r*cosTheta
        circleY = r*sinTheta
        phi = 0
        while phi < 6.28:
            phi += 0.02
            cosPhi = math.cos(phi)
            sinPhi = math.sin(phi)
            cosA = math.cos(A)
            cosB = math.cos(B)
            sinA = math.sin(A)
            sinB = math.sin(B)
            x = circleX*(cosB*cosPhi+sinA*sinB*sinPhi) - circleY*cosA*cosB
            y = circleX*(cosPhi*cosB-cosB*sinA*sinPhi) + circleY*cosA*cosB
            z = circleX*cosA*sinPhi + circleY*sinA + K2
            ooz = 1/z
            L = cosPhi*cosTheta*sinB - cosA*cosTheta*sinPhi - sinA*sinTheta + cosB*(cosA*sinTheta - cosTheta*sinA*sinPhi)
            N = int(L*8)

    A += 0.04
    B += 0.02