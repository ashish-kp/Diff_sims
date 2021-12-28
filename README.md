# Diff_sims
Visualizations of some specific solutions of different differential equations.

## Heat Equation in 1 Dimension

(A very beautiful and elegant explanation for the heat equation and its solution is given [here](https://youtu.be/ly4S0oi3Yz8)

- The heat diffusion equation gives us the temperature at every part of a conducting 1 dimensional material (specific to the current discussion), given we specify the initial condition, and the boundary conditions.
- The thing to be noted here is that the differential equation has a doble derivative with respect to position and a single derivative with respect to time.
- Hence, one can say that the curvature of the position function and the slope of the time function (of course, assuming one is able to write the solution as independent functions of position and time, which we can) are the key playing factors which determine how the temperature gets diffused, so to speak.
- The co-efficient D is the thermal diffusivity constant, and here, can be thought of to be some positive constant. (Let's henceforth assume D = 1)

![heat_eqn](https://latex.codecogs.com/png.image?\dpi{110}&space;\frac{\partial{}}{\partial&space;t}u(x,&space;t)&space;=&space;D&space;\frac{\partial^2&space;}{\partial&space;x^2}u(x,&space;t))

### The Gaussian

- If the initial temperature distribution were to be in the form of a gaussian, that is of the form:

![gauss](https://latex.codecogs.com/png.image?\dpi{110}&space;u(x,0)=&space;e^{-x^2})

This function looks like a bell shaped curve centred at the origin. In other words, it tells us that at the very centre of the rod, the temperature is the highest, and as we move along in either direction it decreases very fast, and some distance from the centre, the temperature is almost zero. This ditribustion might be due to a source which is in contact with the conductor initially, exactly at the centre. 

Laying off rigor, the solution can be written in the following manner:

![Soln](https://latex.codecogs.com/png.image?\dpi{110}&space;u(x,t)=&space;\sqrt{\frac{\pi}{1&plus;t}}&space;e^{\frac{-x^2}{1&plus;t}})

The denominator in the exponential part, actually tells us how much spread out the bell shape is, the higher it's value, more spread out it will be. 
The factor multiplied in the beginning is a normalizing factor, which makes sure that the energy remains constant at all times.

Hence, intuitively, we can see that as time increases, the temperature function smooths out.

- One more thing to be noted, is that as the heat starts spreading, it takes more and more time for it to move farther. This is because temperature is an axponentially decaying function of time.
