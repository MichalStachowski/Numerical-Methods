### The key of the task is to notice the impact of the step on the accuracy of numerical operations  
For the function ln(x), calculate the approximation of the derivative at x = 0.5 according to the following formula:  
![equation](https://latex.codecogs.com/gif.latex?%7Bf%7D%27%5Cleft%20%28%20x%20%5Cright%20%29%20%3D%20%5Cfrac%7Bf%5Cleft%20%28%20x%20&plus;%20h%20%5Cright%20%29%20-%20f%5Cleft%20%28%20x%20-%20h%20%5Cright%20%29%7D%7B2h%7D)
  
Calculations start from h = 0.4 and in subsequent steps (20 in total) reduce h five times compared to the previous step (h = 0.4, 0.08, 0.016, ...). Present the results in the form of a table, where in each row the current value of h, the value of the calculated derivative and the absolute value of the true absolute error of the derivative will be written. Show this error on the graph as a function of h (take a logarithmic scale for both axes). Find the h value for which we obtain the minimum error. 
  
##### NOTE:  
Do not use loop statements in the program.  
  
To calculate true absolute error of the derivative use:  
![equation](https://latex.codecogs.com/gif.latex?%7B%5Cleft%20%28%20ln%5C%3A%20x%20%5Cright%20%29%7D%27%20%3D%20%5Cfrac%7B1%7D%7Bx%7D) 
