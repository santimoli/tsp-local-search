# TSP Solver — Local Search Algorithms

Solver for the **Travelling Salesman Problem (TSP)** implemented in Python. Given a set of cities and distances between them, the goal is to find the shortest circular route that visits every city exactly once.

## Problem

The TSP is a classic NP-hard combinatorial optimisation problem. This project explores and compares several **local search** strategies, reading benchmark instances from the [TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) library.

## Algorithms implemented

| Algorithm | Description |
|-----------|-------------|
| `Greedy` | Hill-climbing: always picks the best neighbour (2-opt swap) |
| `sGreedy` | Stochastic greedy: randomly picks from the top-b neighbours |
| `pGreedy` | Partial greedy: fixes one city and searches for its best swap partner |
| `rGreedy` | Random-restart greedy: runs Greedy multiple times from shuffled starts |
| `Greedy2` | Inversion-based neighbourhood (reversal of subsequences) |
| `rGreedy2` | Random-restart version of Greedy2 |

All algorithms use an **early stopping** condition based on accumulated improvement over the last *k* iterations.

## Technologies

- Python 3
- `tkinter` — graphical visualisation of the TSP tour
- `math`, `random`, `queue` — standard library only

## Project structure

```
algicFinal.py   # All algorithms and core functions
libic.py        # Graphical interface (tkinter)
validate.py     # Solution validator against .opt.tour files
test.py         # Empirical study runner (outputs CSV results)
ic-test.py      # Interactive graphical runner
*.tsp           # TSPLIB benchmark instances
*.opt.tour      # Optimal tour references
```

## How to run

**Requirements:** Python 3.x (no external packages needed)

### Interactive graphical mode
```bash
python ic-test.py
```
Opens a tkinter window where you can select a `.tsp` instance and watch the algorithm optimise the tour in real time.

### Empirical study (batch runner)
```bash
python test.py
```
Runs all algorithms across multiple instances and saves results to a `.csv` file.

### Validate a solution
```bash
python validate.py
```
Compares a computed tour against the known optimal tour from the corresponding `.opt.tour` file.

## Neighbour structure

Two neighbourhood operators are used:
- **2-opt swap** — exchange positions of two cities in the tour
- **Inversion** — reverse a subsequence of the tour

## Course

Artificial Intelligence — 2nd year, 2nd semester (2024/2025)
