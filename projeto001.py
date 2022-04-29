# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:

    #CÓDIGO PRINCIPAL

ir = 0.11 #11%
inss = 0.08 #8%
sindicato = 0.05 #5%


print('\nOlá! Vou mostrar a você todos os descontos sobre o seu salário bruto.\n')

def main ():


    valor_hora = input('Informe o valor recebido por hora R$')
    verificacao(valor_hora)

    num_horas = input('Informe o número de horas trabalhadas por dia: ')
    verificacao(valor_hora)

    num_dias = input('Informe o número de dias trabalhadas por mês: ')
    verificacao(valor_hora)

    salario = bruto(num_horas,num_dias,valor_hora)
    print (f'\nSalário bruto: R${salario:,.2f}')

    descontos(salario)

    #Deve calcular primeiro quantas horas trabalhadas por mes, em seguida o salario mensal.

def bruto (tempo_horas,dias_mes,valor_por_hora):

    carga_horaria_mes = int(tempo_horas)*int(dias_mes)
    salario = int(carga_horaria_mes)*int(valor_por_hora)
    return int(salario)

def descontos (salario):

    valor_ir = (salario * ir)
    sobra = (salario-valor_ir)
    print(f'\nImposto renda 11% - R${valor_ir:,.2f} reais.')
    print(f'Saldo RS{sobra:,.2f}.')

    valor_inss = int((salario - valor_ir) * inss)
    sobra = int (sobra - valor_inss)
    print(f'\nINSS 8% - R${valor_inss:,.2f} reais.')
    print(f'Saldo RS{sobra:,.2f}.')

    valor_sindicato = int((salario - (valor_inss + valor_ir)) * sindicato)
    sobra = int(sobra - valor_sindicato)
    print(f'\nSindicato 5% - R${valor_sindicato:,.2f} reais.')
    print(f'Salário líquido: R${sobra:,.2f} reais.')

def verificacao(var):
    teste = var.isdigit()
    if teste == False:
        print('\nResposta inválida!\n')
        main()

main()



