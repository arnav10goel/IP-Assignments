e = list(map(float, input("Input the three values for the origin i.e. ex ey ez WITH Spaces: ").split()))
ex = e[0]
ey = e[1]
ez = e[2]

d = list(map(float, input("Input the three values for the direction i.e. dx dy dz WITH Spaces: ").split()))
dx = d[0]
dy = d[1]
dz = d[2]

x0 = float(input("X-coordinate of Center of Sphere: "))
y0 = float(input("Y-coordinate of Center of Sphere: "))
z0 = float(input("Z-coordinate of Center of Sphere: "))

center = (x0, y0, z0)

r = float(input("Radius of Sphere: "))

def sphere(x, y, z):
    s = ((x-x0)**2 + (y-y0)**2 + (z-z0)**2 - r**2)
    return s

for t in range(2, 1001):
    prev_pointx = ex + (t-1)*dx
    prev_pointy = ey + (t-1)*dy
    prev_pointz = ez + (t-1)*dz
    next_pointx = ex + (t)*dx
    next_pointy = ey + (t)*dy
    next_pointz = ez + (t)*dz
    if (sphere(prev_pointx, prev_pointy, prev_pointz) < 0 and sphere(next_pointx, next_pointy, next_pointz) > 0) or (sphere(prev_pointx, prev_pointy, prev_pointz) > 0 and sphere(next_pointx, next_pointy, next_pointz) < 0):
        prev = (round(prev_pointx,3), round(prev_pointy,3), round(prev_pointz,3))
        next = (round(next_pointx,3), round(next_pointy,3), round(next_pointz,3))
        print("The ray with origin at", e, "and direction", d, "intersects the circle with radius", r, "and center at", center, "first time somewhere between: point", prev, "at t=", t-1, "and point", next, "at t=", t, ".")
