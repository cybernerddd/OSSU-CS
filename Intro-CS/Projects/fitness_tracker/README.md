# Fitness Tracker (MIT 6.100L - Lecture 20)

A simple object-oriented fitness tracker built while following **MIT 6.100L: Introduction to Computer Science and Programming Using Python**.
This project was recreated from scratch to reinforce Object-Oriented Programming concepts rather than copying the lecture code.

--- 

## Concepts Practiced

- Classes and Objects
- Constructors (`__init__`)
- Instance Variables
- Class Variables
- Getters and Setters
- Information Hiding
- Inheritance
- Method Overriding
- Polymorphism
- Equality Methods (`__eq__`)
- String Representation (`__str__`)
- Working with Python's `datetime`
- GPS distance calculations

---

## Project Structure

```text
fitness_tracker/
│
├── fitness_tracker.py
├── gps.py
└── README.md
```

---

## Classes

### Workout

Base class representing a generic workout.

Attributes include:

- Start time
- End time
- Calories
- Workout type
- Workout icon

Provides methods for:

- Calculating workout duration
- Estimating calories burned
- Updating workout information
- Printing workout summaries
- Comparing workouts

---

### RunWorkout

Subclass of `Workout`.

Additional features:

- Elevation tracking
- GPS route support
- Distance-based calorie estimation

---

### SwimWorkout

Subclass of `Workout`.

Additional features:

- Swimming pace
- Swimming-specific calorie calculation

---

## Helper Module

`gps.py`

Contains a helper function:

```python
gpsDistance(point1, point2)
```

Uses the Haversine formula to calculate the distance between two GPS coordinates.

---

## Example

```python
w = Workout(
    "9/30/2021 1:35 PM",
    "9/30/2021 2:05 PM"
)

print(w.get_calories())
```

Create a running workout:

```python
run = RunWorkout(
    "9/30/2021 1:35 PM",
    "9/30/2021 3:35 PM",
    elev=150
)
```

Calculate total calories:

```python
total_calories([w, run])
```

---

## Learning Outcome

This project strengthened my understanding of:

- Designing reusable classes
- Building inheritance hierarchies
- Using `super()`
- Overriding methods
- Applying polymorphism
- Organizing larger Python projects

---

## Course

- **MIT OpenCourseWare**
- **6.100L – Introduction to Computer Science and Programming Using Python**
- Lecture 20 – Object-Oriented Programming
