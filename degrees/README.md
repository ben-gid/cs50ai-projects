# Degrees of Separation 🎮

A program that determines the number of “degrees of separation” between any two actors based on movies they’ve appeared in together. Inspired by the *Six Degrees of Kevin Bacon* game, this project uses **Breadth-First Search (BFS)** to find the shortest connection path between two actors through shared films.

---

## 📘 Overview

According to the Six Degrees of Kevin Bacon game, any actor can be connected to Kevin Bacon through a chain of co-starring appearances.
In this project, we generalize that idea — finding the shortest connection between **any two actors** using movie data from IMDb.

For example:

```
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

---

## 🧠 How It Works

The program models the movie network as a **graph**:

* **Nodes:** actors
* **Edges:** shared movies

Using **Breadth-First Search (BFS)**, it explores the graph layer by layer to find the **shortest path** between two actors.

Each step connects two actors through a movie they both appeared in.

---

## 🧬 Data Structure

The program loads data from CSV files into the following dictionaries:

* `names` → `{ name (lowercase): set of person_ids }`
* `people` → `{ person_id: { name, birth, movies (set) } }`
* `movies` → `{ movie_id: { title, year, stars (set of person_ids) } }`

### Files

Each dataset (small and large) contains:

* `people.csv` — list of actors and their IDs
* `movies.csv` — list of movies and their IDs
* `stars.csv` — links actors to movies

---

## ⚙️ Implementation Details

You implement the `shortest_path(source, target)` function in `degrees.py`.

### Function Specification

```python
def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs that connect the source to the target.
    If no connection exists, returns None.
    """
```

* Uses **Breadth-First Search** with a `QueueFrontier`
* Tracks visited actors to avoid cycles
* Stops early when the goal is found for efficiency
* Returns the chain of (movie_id, person_id) pairs representing the path

Example return value:

```python
[(1, 2), (3, 4)]
```

Means:

* Source starred in movie 1 with person 2
* Person 2 starred in movie 3 with person 4 (the target)

---

## 🚀 Getting Started

### 1. Clone and unzip the distribution code

Download from [CS50 AI distribution](https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip):

```bash
wget https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip
unzip degrees.zip
cd degrees
```

### 2. Run the program

You can test it with either dataset:

```bash
python degrees.py small
```

or

```bash
python degrees.py large
```

---

## 🥪 Testing

You can check your work using CS50’s automated tests.

Run correctness checks:

```bash
check50 ai50/projects/2024/x/degrees
```

Run style checks:

```bash
style50 degrees.py
```

---

## 🦯 Example Interaction

```
$ python degrees.py small
Loading data...
Data loaded.
Name: Tom Cruise
Name: Kevin Bacon
2 degrees of separation.
1: Tom Cruise and Jack Nicholson starred in A Few Good Men
2: Jack Nicholson and Kevin Bacon starred in A Few Good Men
```

---

## 📁 Repository Structure

```
degrees/
│
├── small/                     # Small dataset for quick testing
│   ├── people.csv
│   ├── movies.csv
│   └── stars.csv
│
├── large/                     # Full IMDb dataset
│   ├── people.csv
│   ├── movies.csv
│   └── stars.csv
│
├── degrees.py                 # Main program
├── util.py                    # Search utilities (Node, StackFrontier, QueueFrontier)
└── README.md                  # This file
```

---

## 🧮 Algorithmic Complexity

* **Time Complexity:** O(V + E)
* **Space Complexity:** O(V)
  Where:
* V = number of actors
* E = number of connections (shared movies)

BFS ensures the shortest possible connection path is always found.

---

## 🗳️ Submission Instructions

If using `submit50`:

```bash
submit50 ai50/projects/2024/x/degrees
```

If submitting via GitHub manually, push only your modified files (not the large/small directories) to:

```
https://github.com/me50/YOUR_USERNAME.git
```

on branch:

```
ai50/projects/2024/x/degrees
```

---

## 🙏 Acknowledgements

Data provided courtesy of **IMDb**, used with permission.
Assignment from **CS50’s Introduction to Artificial Intelligence with Python (CS50 AI)**.

---

**Author:** [Your Name]
**Course:** Harvard CS50 AI — Project 0: Degrees
**Language:** Python 3.12
