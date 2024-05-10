class VideoLocadora:
    def __init__(self):
        self.filmes = {}
        self.dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

    def addReserva(self, titulo, cliente, dia):
        if titulo not in self.filmes: self.filmes[titulo] = {dia: [] for dia in self.dias_semana}
        
        self.filmes[titulo][dia].append(cliente)
        print(f"Reserva adicionada: {cliente} reservou '{titulo}' para {dia}.")

    def rmvReserva(self, titulo, dia):
        if titulo not in self.filmes:
            print(f"O filme '{titulo}' não foi encontrado.")
            return
        
        if dia not in self.filmes[titulo]:
            print(f"O dia '{dia}' não é válido.")
            return
        
        if len(self.filmes[titulo][dia]) == 0:
            print(f"Não há reservas para '{titulo}' em '{dia}'.")
            return
        
        cliente = self.filmes[titulo][dia].pop(0)
        print(f"Reserva removida: {cliente} alugou '{titulo}' em {dia}.")

    def listReservas(self, titulo):
        if titulo not in self.filmes:
            print(f"O filme '{titulo}' não foi encontrado.")
            return
        
        print(f"Reservas para '{titulo}':")
        for dia in self.dias_semana:
            clientes = self.filmes[titulo][dia]
            print(f"Dia {dia.capitalize()}: {clientes if clientes else 'Nenhuma reserva'}")

videolocadora = VideoLocadora()

videolocadora.addReserva("O Poderoso Chefão", "Carlos", "segunda")
videolocadora.addReserva("O Poderoso Chefão", "Maria", "terça")
videolocadora.addReserva("O Poderoso Chefão", "José", "segunda")
videolocadora.addReserva("Interstelar", "Antônio", "segunda")
videolocadora.addReserva("Brilho eterno de uma mente sem lembraças", "Vincent", "sexta")
videolocadora.addReserva("Ponyo", "Steven", "quarta")

videolocadora.listReservas("O Poderoso Chefão")
print("\n")
videolocadora.listReservas("Ponyo")
print("\n")
videolocadora.listReservas("Interstelar")
print("\n")

videolocadora.rmvReserva("O Poderoso Chefão", "segunda")
print("\n")
print("\n//====== COMEÇO REGISTRO ======//\n")

while True:
    print("\n\nEscolha uma opção:")
    print("1. Adicionar uma reserva")
    print("2. Remover uma reserva")
    print("3. Listar reservas de um filme")
    print("4. Sair")

    opcao = input("\nDigite sua escolha (1, 2, 3 ou 4):\n")

    if opcao == "1":
        titulo = input("Digite o título do filme:\n")
        cliente = input("Digite o nome do cliente:\n")
        dia = input("Escolha o dia da semana para a reserva (segunda a domingo):\n").lower()
            
        videolocadora.addReserva(titulo, cliente, dia)

    elif opcao == "2":
        titulo = input("Digite o título do filme:\n")
        dia = input("Escolha o dia da semana para remover a reserva (segunda a domingo):\n").lower()
            
        videolocadora.rmvReserva(titulo, dia)

    elif opcao == "3":
        titulo = input("Digite o título do filme:\n")    
        videolocadora.listReservas(titulo)

    elif opcao == "4":
        print("\n//====== Fim do questionário ======//\n")
        break

    else: print("Opção inválida. Tente novamente.\n")


print("\n//====== FIM REGISTRO ======//\n")

print("//=== FILMES ===//\n")

for i in VideoLocadora.filmes: print(i,"\n")