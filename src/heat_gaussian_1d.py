GlowScript 3.1 VPython

min = -5
max = 5

amp = 2

def f(x, t = 0):
  return amp * exp(-1 * x**2 / (1 + t)) * sqrt(pi / (1 + t))

points = []
# connectors = []
cubes = []

for i in arange(min, max, 0.1):
  points.append(sphere(pos = vec(i, f(i), 0), 
  radius = 0.05, color = vec(0.5 * f(i), 1 - 0.5 * f(i), f(i))))
  cubes.append(box(pos = vec(i, 0, 0), length = 0.2, height = 0.2, width = 0.2, color = color.white))
  
t = 0
dt = 0.01

while True:
  rate(300)
  for point in points:
    x = point.pos.x
    point.pos.y = f(x, t)
    point.color = vec(0.5 * f(x, t),1 - 0.5 * f(x, t), f(x, t))
  for cube in cubes:
    x = cube.pos.x
    cube.color = vec(0.5 * f(x, t),1 - 0.5 * f(x, t), f(x, t))
  t += dt
