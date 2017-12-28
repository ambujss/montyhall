# montyhall
A small python program to simulate the monty hall problem

Usage: `./montyhallsim <number of iterations>`

Upon running, the program will run through the provided number of iterations
for both strategies of the monty hall problem: changing your original pick, and
not changing your original pick. Upon completion, a report will be presented
to the user. An example is provided below:

```
$./montyhallsim 100

Running No Change strategy
Number of runs : 100
 Successes : 43, Failures : 57
 Success rate : 0.430000
 ========
Running Change strategy
Number of runs : 100
 Successes : 64, Failures : 36
 Success rate : 0.640000
 --------
```
