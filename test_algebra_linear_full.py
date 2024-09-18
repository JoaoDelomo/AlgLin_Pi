import numpy as np
import pytest

# Vetores - Exercício 1
def test_vetores_ex1():
    F1 = np.array([1, 2, -1])
    F2 = np.array([-1, 0, 3])
    F3 = -F1 - F2  # For equilibrium
    assert np.allclose(F3, [0, -2, -2])

# Vetores - Exercício 2
def test_vetores_ex2():
    t = 1.0  # Example time value
    velocidade = np.array([6*t, 2, -3*t**2])
    assert np.allclose(velocidade, [6, 2, -3])

# Vetores - Exercício 3
def test_vetores_ex3():
    F = np.array([6, 8, -2])
    d = np.array([1, 1, 0])
    proj_F_d = np.dot(F, d) / np.linalg.norm(d)**2 * d
    assert np.allclose(proj_F_d, [7, 7, 0])

# Vetores - Exercício 4
def test_vetores_ex4():
    r_prime = np.array([1, 2, 2])
    F = np.array([4, -1, 3])
    trabalho = np.dot(F, r_prime)
    assert np.isclose(trabalho, 9)

# Vetores - Exercício 5
def test_vetores_ex5():
    E1 = np.array([2, 3, -1])
    E2 = np.array([-1, 4, 2])
    E_res = E1 + E2
    dot_product = np.dot(E1, E2)
    angle = np.arccos(dot_product / (np.linalg.norm(E1) * np.linalg.norm(E2))) * 180 / np.pi
    assert np.allclose(E_res, [1, 7, 1])
    assert np.isclose(angle, 75.96, atol=1e-2)

# Sistemas Lineares - Exercício 1
def test_sistemas_ex1():
    A = np.array([[2, 1, 1], [3, -2, 4], [1, 5, -1]])
    B = np.array([8, 14, 6])
    X = np.linalg.solve(A, B)
    assert np.allclose(X, [1, 2, 3])

# Sistemas Lineares - Exercício 2
def test_sistemas_ex2():
    A = np.array([[1, -2, 1], [3, 1, -1], [2, -1, 2]])
    B = np.array([10, 20, 15])
    X = np.linalg.solve(A, B)
    assert np.allclose(X, [5, 3, 2])

# Sistemas Lineares - Exercício 3
def test_sistemas_ex3():
    A = np.array([[10, 5, -2], [-3, 8, 4], [6, -1, 3]])
    B = np.array([12, 7, 15])
    X = np.linalg.solve(A, B)
    assert np.allclose(X, [1, 2, 3])

# Sistemas Lineares - Exercício 4
def test_sistemas_ex4():
    A = np.array([[3, 2, 1], [4, -1, 2], [1, 3, 3]])
    B = np.array([120, 150, 180])
    X = np.linalg.solve(A, B)
    assert np.allclose(X, [10, 20, 30])

# Sistemas Lineares - Exercício 5
def test_sistemas_ex5():
    A = np.array([[5, 3, -1], [4, -2, 6], [-3, 5, 4]])
    B = np.array([0, 10, 15])
    X = np.linalg.solve(A, B)
    assert np.allclose(X, [1, 2, 3])

# Geometria Analítica - Exercício 1
def test_geometria_ex1():
    P1 = np.array([2, 3, 5])
    P2 = np.array([7, -2, 1])
    distancia = np.linalg.norm(P2 - P1)
    assert np.isclose(distancia, 7.0711, atol=1e-4)

# Geometria Analítica - Exercício 2
def test_geometria_ex2():
    r1_t = np.array([1 + 2, -1 + 1, 3*1])
    r2_s = np.array([4 + 1, 2 - 1, 5 + 2*1])
    assert np.allclose(r1_t, r2_s)

# Geometria Analítica - Exercício 3
def test_geometria_ex3():
    P = np.array([1, -2, 3])
    plano_normal = np.array([2, -3, 1])
    distancia = abs(np.dot(plano_normal, P) - 4) / np.linalg.norm(plano_normal)
    assert np.isclose(distancia, 3.3166, atol=1e-4)

# Geometria Analítica - Exercício 4
def test_geometria_ex4():
    plano1_normal = np.array([3, 4, -2])
    plano2_normal = np.array([1, -1, 3])
    cos_theta = np.dot(plano1_normal, plano2_normal) / (np.linalg.norm(plano1_normal) * np.linalg.norm(plano2_normal))
    angle = np.arccos(cos_theta) * 180 / np.pi
    assert np.isclose(angle, 83.44, atol=1e-2)

# Geometria Analítica - Exercício 5
def test_geometria_ex5():
    P = np.array([7, 8, 9])
    r_dir = np.array([4, 5, 6])
    r0 = np.array([1, 2, 3])
    proj = r0 + (np.dot(P - r0, r_dir) / np.dot(r_dir, r_dir)) * r_dir
    assert np.allclose(proj, [5, 6, 7])

# Bases - Exercício 1
def test_bases_ex1():
    B = np.array([[1, 2], [3, 4]])
    v = np.array([5, 6])
    coord = np.linalg.solve(B, v)
    assert np.allclose(coord, [-4, 4.5])

# Bases - Exercício 2
def test_bases_ex2():
    v1 = np.array([2, 1])
    v2 = np.array([1, -1])
    u1 = v1 / np.linalg.norm(v1)
    u2 = v2 - np.dot(u1, v2) * u1
    u2 = u2 / np.linalg.norm(u2)
    assert np.allclose(u1, [0.8944, 0.4472], atol=1e-4)
    assert np.allclose(u2, [0.4472, -0.8944], atol=1e-4)

# Bases - Exercício 3
def test_bases_ex3():
    B = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    B_prime = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
    T = np.linalg.inv(B).dot(B_prime)
    assert np.allclose(T, [[1, 1, 0], [0, 1, 1], [1, 0, 1]])

# Bases - Exercício 4
def test_bases_ex4():
    v1 = np.array([1, 2, 3])
    v2 = np.array([2, 4, 6])
    assert np.allclose(v2, 2 * v1)

# Bases - Exercício 5
def test_bases_ex5():
    A = np.array([[2, 1], [1, 3]])
    v = np.array([3, 2])
    transformed_v = A.dot(v)
    assert np.allclose(transformed_v, [8, 9])
