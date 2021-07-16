import numpy 
from grid_plotter import plot_grid

plot_grid(5, filename="img/square_plot.png")
plot_grid(-1, 10, filename="img/square_uneven.png")
plot_grid(-4 * numpy.pi, 4 * numpy.pi, -1.1, 1.1, 21, 11, filename="img/rectangle.png")