renda = float(input("digite sua renda mensal: "))
emprestimo = float(input("digite o valor do emprestimo solicitado: "))
parcelas = int(input("digite o valor da parcela: "))

valor_maximo_emprestimo = renda * 10
prestacao_maxima = renda * 0.3

valor_prestacao = emprestimo/parcelas

if emprestimo <= valor_maximo_emprestimo and valor_prestacao <= prestacao_maxima:
    print("emprestimo aprovado")
else:
    print("emprestimo negado")    
