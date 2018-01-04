# montyhall
A small python (2.7) program to simulate the monty hall problem

```
usage: montyhallsim [-h] [--plot] [--export FILENAME] runs

Monty Hall Problem Simulator

positional arguments:
  runs               Number of iterations

optional arguments:
  -h, --help         show this help message and exit
  --plot             Generate and show a plot
  --export FILENAME  Generate and save a plot to FILENAME
```

Upon running, the program will run through the provided number of iterations
for both strategies of the monty hall problem: changing your original pick, and
not changing your original pick. Upon completion, a report will be presented
to the user. The user can also generate plots of sucess rates vs. number of
runs using the `--plot` and `--export` flags.

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

Note: This program requires the `matplotlib` library.
Please see instructions on how to install `matplotlib` here :
https://matplotlib.org/users/installing.html