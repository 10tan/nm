LINEAR EQUATION SOLVING METHODS

Files:
1. gauss_elimination.py
2. gauss_jordan.py
3. lu_decomposition.py
4. jacobi.py
5. gauss_seidel.py
6. sor.py

Requirements:
    python3 -m pip install numpy

Run a file:
    python3 gauss_elimination.py

Each file is independent and uses the same example system:
    10x - y + 2z = 6
    -x + 11y - z = 22
    2x - y + 10z = -10

Expected solution:
    x = 1, y = 2, z = -1

Notes:
- The iterative methods use a tolerance and maximum iteration count.
- SOR uses omega = 1.1 by default. You can change it in the final function call.
- The LU example uses Doolittle decomposition without pivoting. It is suitable
  for this example, but a zero pivot on another system will raise an error.
- Iterative methods are not guaranteed to converge for every system.
