# Solving variants of the vehicle routing problem using Gurobi

This repository contains Gurobi experiments on solving variants of the vehicle routing
problem. It contains formulations for 3 VRP variants – TSP, ATSP and CVRP.

## Setup

### 1. The code assumes you have a file "credentials.json"
It has to be with the following content:
```json
{
  "access_id": "some-value-here",
  "secret": "some-other-value-here",
  "license_id": 1234567
}
```

This file is used to fill in credentials for your Gurobi license, which is necessary
when running any of these, as the instances are larger than the allowed limit for the
free version.

### 2. The code assumes you have data to run code with

If you have real industry data (like the repository authors), use it.

If you do not, you can create your own data, in which case, the data needs to be in the
following formats.

First, `data/customers.csv` needs to be in format:
```
latitude,longitude,volume
56.950559,24.115600,404
...
```

Second, `data/distance_matrix.csv` needs to be in format:
```
latitude_1,longitude_1,latitude_2,longitude_2,distance
56.950559,24.115600,56.950559,24.115600,0.0
56.950559,24.115600,56.948574,24.118035,267.314
...
```
, where first N rows are distances from position 1 to all other positions, and so on,
resulting in N*N rows.

### 3. Install packages that are used in the project

Run the following commands:
```bash
conda create -n gurobi-vrp-solvers python=3.12
conda activate gurobi-vrp-solvers
pip install notebook
pip install folium
pip install gurobipy
```

## Running

To run the code:
```bash
jupyter notebook
```

## Cleanup

Delete environment with:
```bash
conda remove -n gurobi-vrp-solvers --all
```

## Results

This section contains results on real industry data.

TSP results:

| Task | Solver    | Route, km   | Optimality gap  | Solving time |
|------|-----------|-------------|-----------------|--------------|
| 1    | Gurobi    | **301,03**  | OPTIMAL         | 1 sec        |
| 1    | Timefold  | 301,97      | 0,31 %          | 16 sec*      |
| 2    | Gurobi    | **554,11**  | OPTIMAL         | 2 sec        |
| 2    | Timefold  | 554,11      | < 0,01 %        | 35 sec*      |
| 3    | Gurobi    | **875,02**  | OPTIMAL         | 59 sec       |
| 3    | Timefold  | 875,25      | 0,03 %          | 213 sec*     |
| 4    | Gurobi    | **1287,76** | OPTIMAL         | 494 sec      |
| 4    | Timefold  | 1294,15     | 0,50%           | 979 sec*     |

ATSP results:

| Task | Solver    | Route, km   | Optimality gap | Solving time |
|------|-----------|-------------|----------------|--------------|
| 1    | Gurobi    | **295,77**  | OPTIMAL        | 3 sec        |
| 1    | Timefold  | 296,01      | 0,08 %         | 41 sec*      |
| 2    | Gurobi    | **548,69**  | OPTIMAL        | 3 sec        |
| 2    | Timefold  | 548,72      | 0,01 %         | 37 sec*      |
| 3    | Gurobi    | **863,20**  | OPTIMAL        | 29 sec       |
| 3    | Timefold  | 863,72      | 0,06 %         | 621 sec*     |
| 4    | Gurobi    | **1269,85** | OPTIMAL        | 701 sec      |
| 4    | Timefold  | 1295,03     | 1,98%          | 1429 sec*    |

CVRP results:

| Task | Solver    | Route, km   | Used cars | Optimality gap                    | Solving time |
|------|-----------|-------------|-----------|-----------------------------------|--------------|
| 1    | Gurobi    | **324,25**  | 5         | OPTIMAL                           | 8 sec        |
| 1    | Timefold  | 325,85      | 5         | 0,49 %                            | 724 sec*     |
| 2    | Gurobi    | **1220,89** | 7         | 0,18 % against proven 1218,68 km  | 1489 sec*    |
| 2    | Timefold  | 1221,21     | 7         | 0,21 % against Gurobi bound       | 336 sec*     |
| 3    | Gurobi    | **1549,78** | 7         | 3,20 % against proven 1500,17 km  | 671 sec*     |
| 3    | Timefold  | 1552,32     | 7         | 3,48 % against Gurobi bound       | 839 sec*     |
| 4    | Gurobi    | **3563,49** | 10        | 12,73 % against proven 3109,78 km | 1693 sec*    |
| 4    | Timefold  | 3566,29     | 10        | 14,68 % against Gurobi bound      | 1612 sec*    |
