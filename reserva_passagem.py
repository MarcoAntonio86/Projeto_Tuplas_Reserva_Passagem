voos_disponiveis = []  # Lista de voos (tuplas)
escolha = 0

menu = ('Menu: \n'
    '1. Listar voos disponíveis \n'
    '2. Reservar passagem \n'
    '3. Cancelar reserva \n'
    '4. Sair \n')

print(menu)

while escolha != 4:
    escolha = int(input('Informe a opção: '))

    if escolha == 1:
        if len(voos_disponiveis) == 0:
            print('Não há voos disponíveis!')
        else:
            print('Voos disponíveis:')
            for voo in voos_disponiveis:
                numero_voo, origem, destino, data, preco = voo
                print(f'Número do Voo: {numero_voo}, Origem: {origem}, Destino: {destino}, Data: {data}, Preço: R${preco:.2f}')

    elif escolha == 2:
        numero_voo = input('Informe o número do voo para reservar: ')
        for voo in voos_disponiveis:
            if voo[0] == numero_voo:
                voos_disponiveis.remove(voo)
                print(f'Você reservou o Voo {numero_voo}.')
                break
        else:
            print(f'Voo {numero_voo} não encontrado.')

    elif escolha == 3:
        numero_voo = input('Informe o número do voo para cancelar a reserva: ')
        origem, destino, data, preco = input('Informe origem, destino, data e preço do voo: ').split()
        voos_disponiveis.append((numero_voo, origem, destino, data, preco))
        print(f'Reserva para o Voo {numero_voo} cancelada.')

    elif escolha == 4:
        print("Aplicativo encerrado.")
        break

    else:
        print('Opção inválida')
