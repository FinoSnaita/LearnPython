import turtle
import math

def piece_of_pie(t,angle, base_len):
    
    iso_angle = (180-angle)/2 # angle of an isosceles side 
    iso_radians = iso_angle*math.pi/180
    iso_len = (base_len/2)/math.cos(iso_radians) # length of an isosceles side

    t.fd(base_len)
    t.lt(180-iso_angle)
    t.fd(iso_len)
    t.lt(180-angle)
    t.fd(iso_len)
    t.lt(180-iso_angle)

def n_sided_pie(t,n,side_len):
    
    if n < 3 :
        return
    angle = 360/n
    for _ in range(n):
        piece_of_pie(t,angle,side_len)
        t.fd(side_len)
        t.lt(angle)

bob = turtle.Turtle()

n_sided_pie(bob,12,100)