#import funçao de arredondamento
from math import floor

class Funcionario:
    def __init__(self, nome, valorhora, va, vt,horas):
        self.nome = nome
        self.valorhora = float(valorhora)
        self.va = float(va)
        self.vt = float(vt)
        self.horas = float(horas)
        
        #caucula o salario bruto
        self.salario_bruto = self.valorhora * self.horas
        #caucula o inss
        self.inss = self.caucular_inss()
        #cauculo do irrf
        self.irrf = self.caucular_irrf()
        #cauculo do desconto va
        self.desconto_va = self.desconto_va()
        #cauculo do desconto vt 6% do salario bruto
        self.desconto_vt = self.salario_bruto * 0.06
        # limita o desconto do vt ao valor recebido
        if self.desconto_vt > self.vt:
            self.desconto_va = self.va
            
            #total de descontos
            self.total_descontos =(
                self.inss +
                self.irrf +
                self.desconto_va +
                self.desconto_vt
            )
            #salario liquido
            self.salario_liquido = self.salario_bruto - self.total_descontos
        
        
        # funçao para o cauculo do inss
        def caucular_inss(self):
            salario = self.salario_bruto   
            
            faixas = [
                (1412.00, 0.075),
                (266.68, 0.09),
                (4000.03, 0.12),
                (7786.02, 0.14)
            ]   
            inss = 0
            limite_anterior = 0
            
            for limite, aliquota in faixas:
                if salario > limite:
                    base = limite - limite_anterior
                    inss += base * aliquota
                else:
                    base = salario - limite_anterior
                    inss += base * aliquota
                limite_anterior = limite
            teto = 908.85
            if inss > teto:
                return teto
            return round(inss, 2)
        
        
        
        #funçao irrf
        def caucular_irrf(self):
            base = self.salario_bruto - self.inss
            if base <= 2259.20:
                return 0
            elif base <= 2826.65:
                return round(base * 0.075 - 169.44, 2)
            elif base <= 3751.05:
                return round(base * 0.15 - 381.44, 2)
            elif base <= 4664.68:
                return round(base * 0.225 - 662.44, 2)
            else:
                return round(base * 0.275 - 896.00, 2)
            
        