# 🌌 Matrix: An Introduction to Linear Algebra

[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Project Style: 42](https://img.shields.io/badge/Project-42_Network-lightgrey.svg?style=flat-square)](https://42.fr/)
[![Code: Standard Library Only](https://img.shields.io/badge/dependencies-None-brightgreen.svg?style=flat-square)](https://docs.python.org/3/)

A high-performance, **zero-dependency** implementation of fundamental linear algebra concepts in Python. This library implements vectors, matrices, linear transformations, vector norms, and systems of linear equations (including Reduced Row Echelon Form, determinants, matrix inversions, and ranks) strictly from scratch using Python's standard library. 

Developed as part of the **42 Network** curriculum, this project aims to demystify the core mathematical machinery behind modern computer graphics, physics engines, and machine learning models.

---

## 🎨 Interactive Visualizations

Below are the custom high-contrast technical visualizations showing the mathematical concepts implemented in this library in action.

### 1. Vector Operations & LERP (Linear Interpolation)
Linear interpolation (LERP) allows us to smoothly morph or transition between two points or vectors $\vec{u}$ and $\vec{v}$ in a linear path using a parameter $t \in [0, 1]$. This is implemented in `ex02/Lerp.py` and supports numbers, vectors, and matrices.

<p align="center">
  <img src="./vector-lerp.gif" width="480" alt="Vector Addition and LERP Animation"/>
</p>

### 2. Linear Transformation (2D Shear & Scale)
A linear transformation is a mapping between vector spaces that preserves vector addition and scalar multiplication. By applying a transformation matrix $M$ to standard basis vectors $\hat{i}$ and $\hat{j}$, we can transform the entire grid. This is implemented in `ex07/LinearMap.py` and visualizes the standard 3Blue1Brown "grid-morphing" effect.

<p align="center">
  <img src="./linear-transformation.gif" width="480" alt="2D Linear Transformation Grid Animation"/>
</p>

### 3. Gauss-Jordan Elimination & Reduced Row Echelon Form (RREF)
To solve systems of linear equations, compute matrix inverses, and determine the rank of a matrix, we use Gauss-Jordan elimination. This algorithm applies row operations step-by-step to transform an augmented matrix $[A | b]$ into its Reduced Row Echelon Form. This is implemented in `ex10/RowEchelonForm.py` and `ex12/Inverse.py`.

<p align="center">
  <img src="./gauss-jordan.gif" width="480" alt="Step-by-Step Gauss-Jordan Elimination Matrix Grid Animation"/>
</p>

---

## 🗺️ Exercises Map & Project Structure

The repository contains 14 structured exercises (`ex00` to `ex13`), each covering a critical pillar of linear algebra:

| Module | Filename | Topic | Mathematical Core |
| :--- | :--- | :--- | :--- |
| **`ex00`** | `AddSubtractScale.py` | Vector & Matrix Basics | Vector/Matrix addition ($\vec{u} + \vec{v}$), subtraction ($\vec{u} - \vec{v}$), and scalar scaling ($a\vec{u}$) |
| **`ex01`** | `LinearCombination.py` | Linear Combinations | Linear combinations of vectors $\sum c_i \vec{v}_i$ |
| **`ex02`** | `Lerp.py` | Linear Interpolation | Morphing between scalars, vectors, and matrices $\text{lerp}(u, v, t) = (1-t)u + tv$ |
| **`ex03`** | `DotProduct.py` | Dot Product | Vector dot (scalar) product $\vec{u} \cdot \vec{v}$ |
| **`ex04`** | `Norm.py` | Vector Norms | Manhattan ($L^1$), Euclidean ($L^2$), and Supremum ($L^\infty$) vector norms |
| **`ex05`** | `Cosine.py` | Vector Angle | Cosine of the angle between two vectors $\cos(\theta) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$ |
| **`ex06`** | `CrossProduct.py` | Cross Product | 3D vector cross product $\vec{u} \times \vec{v}$ |
| **`ex07`** | `LinearMap.py` | Matrix Multiplication | Matrix-vector ($A\vec{v}$) and matrix-matrix ($AB$) multiplications |
| **`ex08`** | `Trace.py` | Matrix Trace | Sum of the main diagonal elements of a square matrix $\text{Tr}(A) = \sum a_{ii}$ |
| **`ex09`** | `Transpose.py` | Matrix Transpose | Swapping rows and columns of a matrix $A^T$ |
| **`ex10`** | `RowEchelonForm.py` | Gaussian Elimination | Reduced Row Echelon Form (RREF) using row reduction |
| **`ex11`** | `determinant.py` | Determinants | Calculating the determinant of a square matrix $\det(A)$ |
| **`ex12`** | `Inverse.py` | Matrix Inversion | Computing the inverse of a square matrix $A^{-1}$ using augmented Gauss-Jordan |
| **`ex13`** | `Rank.py` | Matrix Rank | Dimension of vector space spanned by rows/columns (nonzero rows in RREF) |

---

## 🚀 Key Implementations

This library avoids floating point drift issues using a tiny threshold value $\epsilon = 10^{-10}$ for rounding near-zero float values, keeping RREF results highly clean.

### Reduced Row Echelon Form (RREF)
Our `row_echelon()` method implements complete Gaussian Elimination with partial pivoting:

```python
def row_echelon(self):
    m = [row[:] for row in self.data]
    rows = len(m)
    cols = len(m[0])
    pivot_row = 0
    for col in range(cols):
        if pivot_row >= rows:
            break
        pivot = pivot_row
        while pivot < rows and abs(m[pivot][col]) < EPSILON:
            pivot += 1
        if pivot == rows:
            continue
        m[pivot_row], m[pivot] = m[pivot], m[pivot_row]
        pivot_value = m[pivot_row][col]
        for j in range(cols):
            m[pivot_row][j] /= pivot_value
        for i in range(rows):
            if i != pivot_row:
                factor = m[i][col]
                if abs(factor) < EPSILON:
                    continue
                for j in range(cols):
                    m[i][j] -= factor * m[pivot_row][j]
        pivot_row += 1
    return Matrix(m)
```

---

## 🛠️ Getting Started & Usage

### 📦 Installation
Simply clone the repository to your local system:

```bash
git clone https://github.com/RadiantVixen/matrix.git
cd matrix
```

### 🏃 Running the Exercises
No virtual environments, packages, or external installations required! Every module can be run directly as a standalone Python script to execute its built-in unit tests and output examples:

```bash
# Run Vector & Matrix basics tests
python3 ex00/AddSubtractScale.py

# Run Gauss-Jordan Elimination / Row Echelon tests
python3 ex10/RowEchelonForm.py

# Run Matrix Inversion tests
python3 ex12/Inverse.py
```

---

## 🎓 Mathematical Reference

For a complete breakdown of the theoretical concepts, proofs, and vector space axioms covered in this project, you can refer to the **`en.subject.pdf`** file located in the root directory. This comprehensive subject guide provides formal definitions for:
- Vector Space Axioms (closure, associativity, commutativity, distributivity)
- Linear Maps & Morphisms
- Projection and Householder Matrices
- Matrix Properties (Invertibility, Linear Independence, Bases)

---

Developed with 💜 by **RadiantVixen**. For suggestions, contributions, or issues, please open a pull request or file an issue.
