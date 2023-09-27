def desafio_progressoes():
    v_emprestado=100
    juros_sem_posto=0.02
    inflacao_mensal=[0.015,0.02,0.017,0.025,0.03,0.018]
    emprestimo_devido=v_emprestado*(1+juros_sem_posto)**(len(inflacao_mensal))
    print(f'Emprestimo devido (sem correção): R$ {round(emprestimo_devido,2)}')
    neutro=1
    for i in inflacao_mensal:
        neutro*=(i+1)
    inflacao_acumulada=(neutro-1)
    print(f'Inflacao acumulada no período: {round(inflacao_acumulada*100,2)}%')
    print(f'Poder de compra do empréstimo após 6 meses: R$ {round(v_emprestado/(1+inflacao_acumulada),2)}')
    print(f'Valor final devido: R$ {round(emprestimo_devido*(1+inflacao_acumulada),2)}')
desafio_progressoes()