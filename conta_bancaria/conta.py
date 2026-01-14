class   ContaBancaria:
    def __init__(self, titular, saldo_inicial:float):
        self.saldo = saldo_inicial

        #define cheque especial
        self.cheque_especial = 50.0 if saldo_inicial <= 500 else saldo_inicial * 0.5
        self.uso_cheque = 0.0

    def consultar_saldo(self):
        return self.saldo

    def consultar_cheque_especial(self):
        return {
            "limite": self.cheque_especial,
            "uso": self.uso_cheque
        }       
    def depositar(self, valor:float):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor:float):
        if valor <= self.saldo:
            self.saldo -= valor
        elif valor <= self.saldo + (self.cheque_especial - self.uso_cheque):
            restante = valor - self.saldo
            self.saldo = 0
            self.uso_cheque += restante
            return True
        else:
            return False
        