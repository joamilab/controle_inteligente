#@author: Joamila Brito

#Exercício 1 do capítulo 6 de 
	#Fuzzy and Neural Approaches in Engineering - L.H. Tsoukalas & R.E Uhrig

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#Variáveis de Entrada
erro = ctrl.Antecedent(np.arange(-20,20,1), 'erro')
var_erro = ctrl.Antecedent(np.arange(-10,10,1), 'var_erro')

#Variáves de Saída
saida = ctrl.Consequent(np.arange(-25,25,1), 'saida')

#Funções de pertencimento
erro['N'] = fuzz.trimf(erro.universe, [-20,-20,0])
erro['Z'] = fuzz.trimf(erro.universe, [-20,0,20])
erro['P'] = fuzz.trimf(erro.universe, [0,20,20])

var_erro['N'] = fuzz.trimf(var_erro.universe, [-10,-10,10])
var_erro['P'] = fuzz.trimf(var_erro.universe, [-10,10,10])

saida['N'] = fuzz.trimf(saida.universe, [-25,-25,0])
saida['Z'] = fuzz.trimf(saida.universe, [-25,0,25])
saida['P'] = fuzz.trimf(saida.universe, [0,25,25])

#Regras
r1 = ctrl.Rule(erro['N'] & var_erro['N'], saida['P'])
r2 = ctrl.Rule(erro['N'] & var_erro['P'], saida['P'])
r3 = ctrl.Rule(erro['Z'] & var_erro['N'], saida['Z'])
r4 = ctrl.Rule(erro['Z'] & var_erro['P'], saida['Z'])
r5 = ctrl.Rule(erro['P'] & var_erro['N'], saida['N'])
r6 = ctrl.Rule(erro['P'] & var_erro['P'], saida['N'])

#Definição do sistema de controle para defuzzificação
controle = ctrl.ControlSystem([r1,r2,r3,r4,r5,r6])
controle_sim = ctrl.ControlSystemSimulation(controle)

#Simulação com valores do exercício
controle_sim.input['erro'] = 16.0
controle_sim.input['var_erro'] = -2.0

controle_sim.compute()

#Imprime saída
print (controle_sim.output['saida'])
saida.view(sim=controle_sim)
