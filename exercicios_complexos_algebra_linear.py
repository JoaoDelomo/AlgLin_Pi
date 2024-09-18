#!/usr/bin/env python
# coding: utf-8

# 
# # Simulado Avançado - Álgebra Linear e Geometria Analítica (Python)
# 
# Este simulado contém exercícios mais complexos e aplicados sobre os tópicos de vetores, sistemas lineares, geometria analítica e bases. Você poderá resolvê-los utilizando Python e bibliotecas como `numpy`. Esses exercícios têm foco em contextos reais e aplicações práticas.
# 
# ### Boa sorte!
# 

import numpy as np

# ## 1. Vetores - Aplicações

# 
# ### Exercício 1: Direções de forças em um sistema mecânico
# 
# Em um sistema de três forças aplicadas sobre um objeto em equilíbrio, as forças \( F_1 \), \( F_2 \) e \( F_3 \) possuem magnitudes e direções. Sabendo que:
# 
# - \( F_1 \) tem magnitude de 10 N e está na direção \([1, 2, -1]\),
# - \( F_2 \) tem magnitude de 5 N e está na direção \([-1, 0, 3]\),
# - \( F_3 \) mantém o objeto em equilíbrio,
# 
# Encontre o vetor que representa a força \( F_3 \) necessária para que o objeto esteja em equilíbrio. Lembre-se de que a soma das forças em um corpo em equilíbrio deve ser igual a zero.
# 
# Crie uma função chamada calcular_forca_equilibrio() que retorna o vetor de força F3
# 

def calcular_forca_equilibrio():
    F1_direcao = np.array([1, 2, -1])
    F2_direcao = np.array([-1, 0, 3])

    F3 = -(F1_direcao + F2_direcao)

    return F3

# 
# ### Exercício 2: Análise de movimento em 3D
# 
# Um drone se move no espaço 3D seguindo a trajetória descrita pelo vetor posição \( P(t) \), que depende do tempo \( t \). O vetor posição é dado por:
# 
# \[ P(t) = [3t^2, 2t, 5 - t^3] \]
# 
# Encontre a velocidade e aceleração do drone em função do tempo \( t \) e determine o valor de \( t \) para o qual a velocidade é máxima.
# 
# Crie uma função chamada calcular_velocidade_aceleracao() que recebe o tempo t e retorna a velocidade.

import numpy as np

def calcular_velocidade_aceleracao(t):
    velocidade = np.array([6*t, 2, -3*t**2])
    
    return velocidade


# 
# ### Exercício 3: Projeção de vetores
# 
# Dado um vetor de força \( F = [6, 8, -2] \), projete esse vetor na direção do vetor \( d = [1, 1, 0] \). A projeção deve ser calculada para determinar a componente do vetor força ao longo da direção \( d \).
# 
# Crie uma função chamada projetar_forca() que retorna a projeção da força F na direção d.

def projetar_forca():
    F = np.array([6, 8, -2])
    d = np.array([1, 1, 0])

    projecao = (np.dot(F, d)/np.dot(d, d)) * d
    return projecao

# 
# ### Exercício 4: Trabalho realizado por uma força
# 
# Uma partícula se move ao longo de uma trajetória reta, com sua posição em função do tempo dada por \( r(t) = [t, t^2, 2t] \). Uma força constante \( F = [4, -1, 3] \) atua sobre a partícula. Calcule o trabalho realizado pela força ao mover a partícula de \( t = 0 \) até \( t = 3 \).
# 
# Crie uma função chamada calcular_trabalho() que retorna o trabalho realizado.
# 

def calcular_trabalho():
    F = np.array([4, -1, 3])

    rt_3 = np.array([3, 9, 6])
    rt_0 = np.array([0, 0, 0])

    d = rt_3 - rt_0

    trabalho = np.dot(F, d)
    return trabalho


# 
# ### Exercício 5: Operações com vetores em eletricidade
# 
# Dois campos elétricos \( E_1 \) e \( E_2 \) estão presentes em um ponto do espaço. Os vetores que os representam são:
# 
# \[ E_1 = [2, 3, -1], \quad E_2 = [-1, 4, 2] \]
# 
# Encontre o vetor resultante da soma dos campos elétricos e o ângulo entre os vetores \( E_1 \) e \( E_2 \).
# 
# Crie uma função chamada soma_angulos_vetores() que retorna o vetor resultante e o ângulo entre os vetores E1 e E2.
# 

def soma_angulos_vetores():
    E_1 = np.array([2, 3, -1])
    E_2 = np.array([-1, 4, 2])

    # Calcula o cosseno do ângulo entre os vetores
    cos = np.dot(E_1, E_2) / (np.linalg.norm(E_1) * np.linalg.norm(E_2))

    # Calcula o ângulo em radianos usando arccos
    angulo_rad = np.arccos(cos)

    # Converte o ângulo para graus
    angulo_graus = np.degrees(angulo_rad)

    # Calcula o vetor resultante
    vetor_resultante = E_1 + E_2

    return vetor_resultante, angulo_graus


# ## 2. Sistemas Lineares - Aplicações

# 
# ### Exercício 1: Mistura de soluções químicas
# 
# Você é responsável por misturar três soluções químicas. Cada uma das soluções contém uma quantidade diferente de três reagentes (A, B e C). As quantidades são descritas pelas seguintes equações:
# 
# \[
# 2x + y + z = 8 \\
# 3x - 2y + 4z = 14 \\
# x + 5y - z = 6
# \]
# 
# Onde \( x \), \( y \) e \( z \) representam as quantidades de cada solução. Resolva o sistema para encontrar as quantidades de cada solução necessárias para obter as quantidades corretas de reagentes.
# 
# Crie uma função chamada resolver_mistura_solucoes() que retorna a solução do sistema.
# 

# 
# ### Exercício 2: Tráfego em interseções de trânsito
# 
# Em um cruzamento de quatro vias, o número de carros que entram e saem por cada via é modelado pelas seguintes equações:
# 
# \[
# x - 2y + z = 10 \\
# 3x + y - z = 20 \\
# 2x - y + 2z = 15
# \]
# 
# Onde \( x \), \( y \) e \( z \) são as quantidades de carros que entram pelas vias A, B e C, respectivamente. Resolva o sistema para encontrar o fluxo de carros em cada via.
# 
# Crie uma função chamada resolver_trafego() que retorna o fluxo de carros.
# 

# 
# ### Exercício 3: Rede de circuitos elétricos
# 
# Em um circuito elétrico com três malhas, as correntes \( I_1 \), \( I_2 \) e \( I_3 \) em cada malha são descritas pelo seguinte sistema de equações:
# 
# \[
# 10I_1 + 5I_2 - 2I_3 = 12 \\
# -3I_1 + 8I_2 + 4I_3 = 7 \\
# 6I_1 - I_2 + 3I_3 = 15
# \]
# 
# Determine as correntes em cada malha resolvendo o sistema de equações.
# 
# Crie uma função chamada resolver_correntes_circuito() que retorna as correntes nas malhas.
# 

# 
# ### Exercício 4: Previsão de demanda de produtos
# 
# Uma empresa utiliza um modelo linear para prever a demanda de três produtos com base no tempo. As demandas de cada produto (A, B e C) em três períodos de tempo são descritas pelas equações:
# 
# \[
# 3x + 2y + z = 120 \\
# 4x - y + 2z = 150 \\
# x + 3y + 3z = 180
# \]
# 
# Onde \( x \), \( y \) e \( z \) representam a demanda de cada produto em três períodos de tempo. Resolva o sistema para encontrar as previsões de demanda.
# 
# Crie uma função chamada prever_demanda() que retorna a previsão da demanda.

# 
# ### Exercício 5: Equilíbrio de forças em uma estrutura
# 
# Em uma estrutura de três barras conectadas, as tensões \( T_1 \), \( T_2 \) e \( T_3 \) nas barras são descritas pelas seguintes equações:
# 
# \[
# 5T_1 + 3T_2 - T_3 = 0 \\
# 4T_1 - 2T_2 + 6T_3 = 10 \\
# -3T_1 + 5T_2 + 4T_3 = 15
# \]
# 
# Resolva o sistema de equações para determinar as tensões nas barras.
# 
# Crie uma função chamada calcular_tensao_estrutura() que retorna as tensões nas barras.

# ## 3. Geometria Analítica - Aplicações

# 
# ### Exercício 1: Distância entre pontos em um sistema de navegação
# 
# Em um sistema de navegação 3D, um drone parte do ponto \( P_1 = [2, 3, 5] \) e se move em direção ao ponto \( P_2 = [7, -2, 1] \). Calcule a distância entre esses dois pontos e a equação da reta que descreve o movimento do drone.
# 
# Crie uma função chamada calcular_distancia_pontos() que retorna a distância entre os pontos.
# 

# 
# ### Exercício 2: Interseção de retas no espaço 3D
# 
# Duas retas no espaço são dadas pelas equações paramétricas:
# 
# \[
# r_1(t) = [1 + 2t, -1 + t, 3t] \\
# r_2(s) = [4 + s, 2 - s, 5 + 2s]
# \]
# 
# Encontre o ponto de interseção (se existir) dessas duas retas.
# 
# Crie uma função chamada encontrar_intersecao_retas() que retorna o ponto de interseção.
# 

# 
# ### Exercício 3: Planos e distâncias
# 
# Dado o plano descrito pela equação \( 2x - 3y + z = 4 \), encontre a distância do ponto \( P = [1, -2, 3] \) até o plano.
# 
# Crie uma função chamada calcular_distancia_plano() que retorna a distância do ponto ao plano.
# 

# 
# ### Exercício 4: Ângulo entre planos
# 
# Dado o plano \( 3x + 4y - 2z = 10 \) e o plano \( x - y + 3z = 5 \), encontre o ângulo entre esses dois planos.
# 
# Crie uma função chamada calcular_angulo_planos() que retorna o ângulo entre os planos.

# 
# ### Exercício 5: Projeção de um ponto sobre uma reta
# 
# Dada a reta descrita pela equação vetorial \( r(t) = [1, 2, 3] + t[4, 5, 6] \), encontre a projeção do ponto \( P = [7, 8, 9] \) sobre a reta.
# 
# Crie uma função chamada projetar_ponto_reta() que retorna a projeção do ponto sobre a reta.
# 

# ## 4. Bases - Aplicações

# 
# ### Exercício 1: Mudança de base em um sistema de coordenadas
# 
# Considere o sistema de coordenadas com a base \( B = \{[1, 2], [3, 4]\} \). Encontre as coordenadas do vetor \( v = [5, 6] \) em relação à base \( B \).
# 
# Crie uma função chamada coordenadas_base() que retorna as coordenadas do vetor na nova base.
# 

# 
# ### Exercício 2: Base ortonormal
# 
# Dado o conjunto de vetores \([2, 1], [1, -1]\), utilize o processo de Gram-Schmidt para encontrar uma base ortonormal para o subespaço gerado por esses vetores.
# 
# Crie uma função chamada gram_schmidt() que retorna a base ortonormal.

# 
# ### Exercício 3: Mudança de base em 3D
# 
# Dada a base \( B = \{[1, 0, 0], [0, 1, 0], [0, 0, 1]\} \) e a nova base \( B' = \{[1, 1, 0], [0, 1, 1], [1, 0, 1]\} \), encontre a matriz de transformação de \( B \) para \( B' \).
# 
# Crie uma função chamada transformacao_base() que retorna a matriz de transformação entre as bases.

# 
# ### Exercício 4: Combinação linear e independência linear
# 
# Verifique se os vetores \( v_1 = [1, 2, 3] \), \( v_2 = [2, 4, 6] \), e \( v_3 = [3, 6, 9] \) são linearmente independentes. Se não forem, expresse um dos vetores como combinação linear dos outros.
# 
# Crie uma função chamada verificar_independencia_linear() que verifica a independência linear e, se necessário, retorna a combinação linear.
# 

# 
# ### Exercício 5: Transformação linear
# 
# Dada a transformação linear \( T: \mathbb{R}^2 \to \mathbb{R}^2 \) representada pela matriz \( A = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} \), encontre a imagem do vetor \( v = [3, 2] \) sob essa transformação.
# 
# Crie uma função chamada aplicar_transformacao_linear() que aplica a transformação ao vetor.
# 
