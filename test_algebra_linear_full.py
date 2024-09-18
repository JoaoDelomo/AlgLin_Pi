import numpy as np
import pytest
from exercicios_complexos_algebra_linear import *

# Vetores - Exercício 1
def test_vetores_ex1():
    F1 = np.array([1, 2, -1])
    F2 = np.array([-1, 0, 3])
    F3 = calcular_forca_equilibrio()  # Call the user's function
    assert F3 is not None, "A função não pode retornar None"
    assert np.allclose(F3, -F1 - F2), "O vetor F3 está incorreto!"

# Vetores - Exercício 2
def test_vetores_ex2():
    t = 1.0  # Example time value
    velocidade = calcular_velocidade_aceleracao(t)  # Call the user's function
    assert velocidade is not None, "A função não pode retornar None"
    assert np.allclose(velocidade, [6*t, 2, -3*t**2]), "A velocidade está incorreta!"

# Vetores - Exercício 3
def test_vetores_ex3():
    F = np.array([6, 8, -2])
    d = np.array([1, 1, 0])
    proj_F_d = projetar_forca()  # Call the user's function
    assert proj_F_d is not None, "A função não pode retornar None"
    assert np.allclose(proj_F_d, [7, 7, 0]), "A projeção está incorreta!"

# Vetores - Exercício 4
def test_vetores_ex4():
    trabalho = calcular_trabalho()  # Call the user's function
    assert trabalho is not None, "A função não pode retornar None"
    assert np.isclose(trabalho, 21), "O trabalho calculado está incorreto!"

# Vetores - Exercício 5
def test_vetores_ex5():
    E_res, angle = soma_angulos_vetores()  # Call the user's function
    assert E_res is not None and angle is not None, "A função não pode retornar None"
    assert np.allclose(E_res, [1, 7, 1]), "O vetor resultante está incorreto!"
    assert np.isclose(angle, 62.188156861783895, atol=1e-2), "O ângulo calculado está incorreto!"

import numpy as np

# Sistemas Lineares - Exercício 1
def test_sistemas_ex1():
    X = resolver_mistura_solucoes()
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [2, 1.33333333, 2.66666667]), "A solução do sistema está incorreta!"

# Sistemas Lineares - Exercício 2
def test_sistemas_ex2():
    X = resolver_trafego()
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [7.08333333, -1.66666667, -0.41666667]), "A solução do sistema está incorreta!"

# Sistemas Lineares - Exercício 3
def test_sistemas_ex3():
    X = resolver_correntes_circuito()
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [1.46728972, 0.3364486, 2.17757009]), "A solução do sistema está incorreta!"

# Sistemas Lineares - Exercício 4
def test_sistemas_ex4():
    X = prever_demanda()
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [18.52941176, 10.58823529, 43.23529412]), "A previsão de demanda está incorreta!"

# Sistemas Lineares - Exercício 5
def test_sistemas_ex5():
    X = calcular_tensao_estrutura()
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [-0.22875817, 1.11111111, 2.18954248]), "As tensões nas barras estão incorretas!"

# Geometria Analítica - Exercício 1
def test_geometria_ex1():
    distancia = calcular_distancia_pontos()
    assert distancia is not None, "A função não pode retornar None"
    assert np.isclose(distancia, 8.12403840463596, atol=1e-4), "A distância calculada está incorreta!"

# Geometria Analítica - Exercício 2
def test_geometria_ex2():
    intersecao = encontrar_intersecao_retas()
    assert intersecao is not None, "A função não pode retornar None"
    assert np.allclose(intersecao, [1.72727273, 2.45454545, 0.09090909]), "O ponto de interseção está incorreto!"

# Geometria Analítica - Exercício 3
def test_geometria_ex3():
    distancia = calcular_distancia_plano()
    assert distancia is not None, "A função não pode retornar None"
    assert np.isclose(distancia, 1.8708286933869707, atol=1e-4), "A distância ao plano está incorreta!"

# Geometria Analítica - Exercício 4
def test_geometria_ex4():
    angle = calcular_angulo_planos()
    assert angle is not None, "A função não pode retornar None"
    assert np.isclose(angle, 113.07431657230504, atol=1e-2), "O ângulo entre os planos está incorreto!"

# Geometria Analítica - Exercício 5
def test_geometria_ex5():
    proj = projetar_ponto_reta()
    assert proj is not None, "A função não pode retornar None"
    assert np.allclose(proj, [5.67532468, 7.84415584, 10.01298701]), "A projeção do ponto sobre a reta está incorreta!"

# Bases - Exercício 1
def test_bases_ex1():
    coord = coordenadas_base()
    assert coord is not None, "A função não pode retornar None"
    assert np.allclose(coord, [-4., 4.5]), "As coordenadas do vetor estão incorretas!"

# Bases - Exercício 2
def test_bases_ex2():
    u1, u2 = gram_schmidt()
    assert u1 is not None and u2 is not None, "A função não pode retornar None"
    assert np.allclose(u1, [0.89442719, 0.4472136], atol=1e-4), "O vetor u1 está incorreto!"
    assert np.allclose(u2, [0.4472136, -0.89442719], atol=1e-4), "O vetor u2 está incorreto!"

# Bases - Exercício 3
def test_bases_ex3():
    T = transformacao_base()
    assert T is not None, "A função não pode retornar None"
    assert np.allclose(T, [[1., 1., 0.], [0., 1., 1.], [1., 0., 1.]]), "A matriz de transformação está incorreta!"

# Bases - Exercício 4
def test_bases_ex4():
    v2 = verificar_independencia_linear()
    assert v2 is not None, "A função não pode retornar None"
    assert np.allclose(v2, [2, 4, 6]), "A combinação linear está incorreta!"

# Bases - Exercício 5
def test_bases_ex5():
    transformed_v = aplicar_transformacao_linear()
    assert transformed_v is not None, "A função não pode retornar None"
    assert np.allclose(transformed_v, [8, 9]), "A transformação linear está incorreta!"

