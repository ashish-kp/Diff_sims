# Diff_sims
Visualizations of some specific solutions of different differential equations.

## Heat Equation in 1 Dimension

(A very beautiful and elegant explanation for the heat equation and its solution is given ![here](https://youtu.be/ToIXSwZ1pJU)

- The heat diffusion equation gives us the temperature at every part of a conducting 1 dimensional material (specific to the current discussion), given we specify the initial condition, and the boundary conditions.
- The thing to be noted here is that the differential equation has a doble derivative with respect to position and a single derivative with respect to time.
- Hence, one can say that the curvature of the position function and the slope of the time function (of course, assuming one is able to write the solution as independent functions of position and time, which we can) are the key playing factors which determine how the temperature gets diffused, so to speak.
- The co-efficient D is the thermal diffusivity constant, and here, can be thought of to be some positive constant.

![heat_eqn](https://latex.codecogs.com/png.image?\dpi{110}&space;\frac{\partial{}}{\partial&space;t}u(x,&space;t)&space;=&space;D&space;\frac{\partial^2&space;}{\partial&space;x^2}u(x,&space;t))

### The Gaussian

- If the initial temperature distribution were to be in the form of a gaussian, that is of the form:


