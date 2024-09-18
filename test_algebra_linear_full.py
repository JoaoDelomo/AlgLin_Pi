import numpy as np
import pytest

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
    assert np.isclose(trabalho, 9), "O trabalho calculado está incorreto!"

# Vetores - Exercício 5
def test_vetores_ex5():
    E_res, angle = soma_angulos_vetores()  # Call the user's function
    assert E_res is not None and angle is not None, "A função não pode retornar None"
    assert np.allclose(E_res, [1, 7, 1]), "O vetor resultante está incorreto!"
    assert np.isclose(angle, 75.96, atol=1e-2), "O ângulo calculado está incorreto!"

# Sistemas Lineares - Exercício 1
def test_sistemas_ex1():
    X = resolver_mistura_solucoes()  # Call the user's function
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [1, 2, 3]), "A solução do sistema está incorreta!"

# Sistemas Lineares - Exercício 2
def test_sistemas_ex2():
    X = resolver_trafego()  # Call the user's function
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [5, 3, 2]), "A solução do sistema está incorreta!"

# Sistemas Lineares - Exercício 3
def test_sistemas_ex3():
    X = resolver_correntes_circuito()  # Call the user's function
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [1, 2, 3]), "A solução do sistema está incorreta!"

# Sistemas Lineares - Exercício 4
def test_sistemas_ex4():
    X = prever_demanda()  # Call the user's function
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [10, 20, 30]), "A previsão de demanda está incorreta!"

# Sistemas Lineares - Exercício 5
def test_sistemas_ex5():
    X = calcular_tensao_estrutura()  # Call the user's function
    assert X is not None, "A função não pode retornar None"
    assert np.allclose(X, [1, 2, 3]), "As tensões nas barras estão incorretas!"

# Geometria Analítica - Exercício 1
def test_geometria_ex1():
    distancia = calcular_distancia_pontos()  # Call the user's function
    assert distancia is not None, "A função não pode retornar None"
    assert np.isclose(distancia, 7.0711, atol=1e-4), "A distância calculada está incorreta!"

# Geometria Analítica - Exercício 2
def test_geometria_ex2():
    intersecao = encontrar_intersecao_retas()  # Call the user's function
    assert intersecao is not None, "A função não pode retornar None"
    assert np.allclose(intersecao, [3, 0, 3]), "O ponto de interseção está incorreto!"

# Geometria Analítica - Exercício 3
def test_geometria_ex3():
    distancia = calcular_distancia_plano()  # Call the user's function
    assert distancia is not None, "A função não pode retornar None"
    assert np.isclose(distancia, 3.3166, atol=1e-4), "A distância ao plano está incorreta!"

# Geometria Analítica - Exercício 4
def test_geometria_ex4():
    angle = calcular_angulo_planos()  # Call the user's function
    assert angle is not None, "A função não pode retornar None"
    assert np.isclose(angle, 83.44, atol=1e-2), "O ângulo entre os planos está incorreto!"

# Geometria Analítica - Exercício 5
def test_geometria_ex5():
    proj = projetar_ponto_reta()  # Call the user's function
    assert proj is not None, "A função não pode retornar None"
    assert np.allclose(proj, [5, 6, 7]), "A projeção do ponto sobre a reta está incorreta!"

# Bases - Exercício 1
def test_bases_ex1():
    coord = coordenadas_base()  # Call the user's function
    assert coord is not None, "A função não pode retornar None"
    assert np.allclose(coord, [-4, 4.5]), "As coordenadas do vetor estão incorretas!"

# Bases - Exercício 2
def test_bases_ex2():
    u1, u2 = gram_schmidt()  # Call the user's function
    assert u1 is not None and u2 is not None, "A função não pode retornar None"
    assert np.allclose(u1, [0.8944, 0.4472], atol=1e-4), "O vetor u1 está incorreto!"
    assert np.allclose(u2, [0.4472, -0.8944], atol=1e-4), "O vetor u2 está incorreto!"

# Bases - Exercício 3
def test_bases_ex3():
    T = transformacao_base()  # Call the user's function
    assert T is not None, "A função não pode retornar None"
    assert np.allclose(T, [[1, 1, 0], [0, 1, 1], [1, 0, 1]]), "A matriz de transformação está incorreta!"

# Bases - Exercício 4
def test_bases_ex4():
    v2 = verificar_independencia_linear()  # Call the user's function
    assert v2 is not None, "A função não pode retornar None"
    assert np.allclose(v2, 2 * np.array([1, 2, 3])), "A combinação linear está incorreta!"

# Bases - Exercício 5
def test_bases_ex5():
    transformed_v = aplicar_transformacao_linear()  # Call the user's function
    assert transformed_v is not None, "A função não pode retornar None"
    assert np.allclose(transformed_v, [8, 9]), "A transformação linear está incorreta!"

