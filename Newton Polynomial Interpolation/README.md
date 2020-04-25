Generate four random points x∈(0.10), y∈(0.10).  
For these points, should be performed interpolation using Newton polynomial.

#### Mathematical formulas used
![equation](https://latex.codecogs.com/gif.latex?b_%7B1%7D%20%3D%20f%5Cleft%20%28%20x_%7B0%7D%20%5Cright%20%29)   
![equation](https://latex.codecogs.com/gif.latex?b_%7B2%7D%20%3D%20%5Cfrac%7By_%7B1%7D%20-%20y_%7B0%7D%7D%7Bx_%7B1%7D%20-%20x_%7B0%7D%7D)  
![equation](https://latex.codecogs.com/gif.latex?b_%7B3%7D%20%3D%20%5Cfrac%7B%5Cfrac%7By_%7B2%7D%20-%20y_%7B0%7D%7D%7Bx_%7B2%7D%20-%20x_%7B0%7D%7D%20-%20%5Cfrac%7By_%7B1%7D%20-%20y_%7B0%7D%7D%7Bx_%7B1%7D%20-%20x_%7B0%7D%7D%7D%7Bx_%7B2%7D%20-%20x_%7B1%7D%7D)  
![equation](https://latex.codecogs.com/gif.latex?b_%7B3%7D%20%3D%20%5Cfrac%7B%5Cfrac%7B%5Cfrac%7By_%7B3%7D%20-%20y_%7B0%7D%7D%7Bx_%7B3%7D%20-%20x_%7B0%7D%7D%20-%20%5Cfrac%7By_%7B1%7D%20-%20y_%7B0%7D%7D%7Bx_%7B1%7D%20-%20x_%7B0%7D%7D%7D%7Bx_%7B3%7D%20-%20x_%7B1%7D%7D%20-%20%5Cfrac%7B%5Cfrac%7By_%7B2%7D%20-%20y_%7B0%7D%7D%7Bx_%7B2%7D%20-%20x_%7B0%7D%7D%20-%20%5Cfrac%7By_%7B1%7D%20-%20y_%7B0%7D%7D%7Bx_%7B1%7D%20-%20x_%7B0%7D%7D%7D%7Bx_%7B2%7D%20-%20x_%7B1%7D%7D%7D%7Bx_%7B3%7D%20-%20x_%7B2%7D%7D)
