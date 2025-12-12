class Pagamento():
    type=""
    def __init__(self,type):
        self.type=type
    def processar_pagamento(self):
        return self.type
class CartaoCredito(Pagamento):
    numero_cartao=""
    nome_titular=""
    validade=""
    ccv=""
    def __init__(self,numero_cartao,nome_titular,validade,ccv):
        self.numero_cartao=numero_cartao
        self.nome_titular=nome_titular
        self.validade=validade
        self.ccv=ccv
        super().__init__(type="Cartão de Crédito")
    def processar_pagamento(self):
        return self.numero_cartao
class PayPal(Pagamento):
    email=""
    def __init__(self,email):
        self.email=email
        super().__init__(type="PayPal")
    def processar_pagamento(self):
        return self.email
class TransferenciaBancaria(Pagamento):
    banco=""
    agencia=""
    conta=""
    def __init__(self,banco,agencia,conta):
        self.banco=banco
        self.agencia=agencia
        self.conta=conta
        super().__init__(type="Transferência Bancária")
    def processar_pagamento(self):
        return "banco: "+self.banco,"conta: "+self.conta
def realizar_pagamento(pg,qtd):
    info=pg.processar_pagamento()
    print("€",qtd,"com",pg.type,":",info)
cartao_credito=CartaoCredito(numero_cartao="1234 5678 9012 3456",nome_titular="João Silva",validade="12/25",ccv="123")
realizar_pagamento(cartao_credito,150.00)
paypal=PayPal(email="joao.silva@email.com")
realizar_pagamento(paypal,200.00)
transferencia=TransferenciaBancaria(banco="Banco Central",agencia="1234",conta="12345678")
realizar_pagamento(transferencia,300.00)