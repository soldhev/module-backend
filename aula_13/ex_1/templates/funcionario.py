class Funcionario:
    def __init__(self):
        self._nome = ""
        self._salario_bruto = 0.0
        self._vale_transporte = 0.0
        
        self._inss = 0.0
        self._ir = 0.0
        self._desconto_va = 0.0
        self._desconto_vt = 0.0
        
        def set_nome(self, nome):
            self._nome = self.strip()
        def set_salario_bruto(self, valor):
            self._salario_bruto = float(valor)
        def set_vale_alimentacao(self, valor): 
            self._vale_alimentacao = float(valor)
        def set_vale_transporte(self, valor):
            self._vale_transporte = float(valor)
            
            def ger_nome(self):
                return self._nome
            def get_salario_bruto(self):
                return  self._salario_bruto
            def get_inss(self):
                return self._inss
            def get_ir(self):
                return self._desconto_va
            
            def get_desconto_vt(self)
            return self._desconto_vt
        
        def caucular_inss(self):
            if self._salario_bruto <= 1320:
                self._inss = self._salario_bruto * 0.075
            elif set_salario_bruto <= 2571:
                self._salario_b    
            
            
                         