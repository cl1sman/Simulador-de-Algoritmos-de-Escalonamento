import queue

class Processo:
    def __init__(self, pid, tempo_execucao, prioridade=0, tempo_chegada=0):
        self.pid = pid
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.prioridade = prioridade
        self.tempo_chegada = tempo_chegada
        self.tempo_conclusao = 0
        self.tempo_retorno = 0
        self.tempo_espera = 0

    def __str__(self):
        return (f"PID: {self.pid}, Tempo de Execução: {self.tempo_execucao}, Tempo Restante: {self.tempo_restante}, "
                f"Prioridade: {self.prioridade}, Tempo de Chegada: {self.tempo_chegada}, Tempo de Conclusão: {self.tempo_conclusao}, "
                f"Tempo de Retorno: {self.tempo_retorno}, Tempo de Espera: {self.tempo_espera}")

def fcfs(processos):
    processos.sort(key=lambda x: x.tempo_chegada)
    tempo_atual = 0
    for processo in processos:
        if tempo_atual < processo.tempo_chegada:
            tempo_atual = processo.tempo_chegada
        processo.tempo_conclusao = tempo_atual + processo.tempo_execucao
        tempo_atual = processo.tempo_conclusao
        processo.tempo_retorno = processo.tempo_conclusao - processo.tempo_chegada
        processo.tempo_espera = processo.tempo_retorno - processo.tempo_execucao
    return processos

def sjf_nao_preemptivo(processos):
    processos.sort(key=lambda x: (x.tempo_chegada, x.tempo_execucao))
    tempo_atual = 0
    processos_concluidos = []
    while processos:
        fila_pronta = [p for p in processos if p.tempo_chegada <= tempo_atual]
        if not fila_pronta:
            tempo_atual = processos[0].tempo_chegada
            fila_pronta = [processos[0]]
        fila_pronta.sort(key=lambda x: x.tempo_execucao)
        processo = fila_pronta.pop(0)
        processos.remove(processo)
        if tempo_atual < processo.tempo_chegada:
            tempo_atual = processo.tempo_chegada
        processo.tempo_conclusao = tempo_atual + processo.tempo_execucao
        tempo_atual = processo.tempo_conclusao
        processo.tempo_retorno = processo.tempo_conclusao - processo.tempo_chegada
        processo.tempo_espera = processo.tempo_retorno - processo.tempo_execucao
        processos_concluidos.append(processo)
    return processos_concluidos

def sjf_preemptivo(processos):
    tempo_atual = 0
    processos_concluidos = []
    fila_pronta = []

    while processos or fila_pronta:
        while processos and processos[0].tempo_chegada <= tempo_atual:
            fila_pronta.append(processos.pop(0))

        if fila_pronta:
            fila_pronta.sort(key=lambda x: x.tempo_restante)
            processo = fila_pronta.pop(0)
            if processo.tempo_restante == processo.tempo_execucao:
                processo.tempo_inicio = tempo_atual

            processo.tempo_restante -= 1
            tempo_atual += 1

            if processo.tempo_restante > 0:
                fila_pronta.append(processo)
            else:
                processo.tempo_conclusao = tempo_atual
                processo.tempo_retorno = processo.tempo_conclusao - processo.tempo_chegada
                processo.tempo_espera = processo.tempo_retorno - processo.tempo_execucao
                processos_concluidos.append(processo)
        else:
            tempo_atual += 1

    return processos_concluidos

def escalonamento_prioridade(processos):
    tempo_atual = 0
    processos_concluidos = []
    fila_pronta = []

    while processos or fila_pronta:
        while processos and processos[0].tempo_chegada <= tempo_atual:
            fila_pronta.append(processos.pop(0))

        if fila_pronta:
            fila_pronta.sort(key=lambda x: x.prioridade)
            processo = fila_pronta.pop(0)
            if processo.tempo_restante == processo.tempo_execucao:
                processo.tempo_inicio = tempo_atual

            processo.tempo_restante -= 1
            tempo_atual += 1

            if processo.tempo_restante > 0:
                fila_pronta.append(processo)
            else:
                processo.tempo_conclusao = tempo_atual
                processo.tempo_retorno = processo.tempo_conclusao - processo.tempo_chegada
                processo.tempo_espera = processo.tempo_retorno - processo.tempo_execucao
                processos_concluidos.append(processo)
        else:
            tempo_atual += 1

    return processos_concluidos

def round_robin(processos, quantum):
    tempo_atual = 0
    fila = []
    processos.sort(key=lambda x: x.tempo_chegada)
    for processo in processos:
        fila.append(processo)

    while fila:
        processo = fila.pop(0)
        if processo.tempo_restante > quantum:
            tempo_atual += quantum
            processo.tempo_restante -= quantum
            while fila and fila[0].tempo_chegada <= tempo_atual:
                fila.append(fila.pop(0))
            fila.append(processo)
        else:
            tempo_atual += processo.tempo_restante
            processo.tempo_restante = 0
            processo.tempo_conclusao = tempo_atual
            processo.tempo_retorno = processo.tempo_conclusao - processo.tempo_chegada
            processo.tempo_espera = processo.tempo_retorno - processo.tempo_execucao
    return processos

def obter_processos():
    n = int(input("Digite o número de processos: "))
    processos = []
    for i in range(n):
        pid = input(f"Digite o PID do processo {i+1}: ")
        tempo_execucao = int(input(f"Digite o tempo de execução do processo {i+1}: "))
        tempo_chegada = int(input(f"Digite o tempo de chegada do processo {i+1}: "))
        prioridade = int(input(f"Digite a prioridade do processo {i+1} (0 se não for usado): "))
        processos.append(Processo(pid, tempo_execucao, prioridade, tempo_chegada))
    return processos

def main():
    while True:
        print("\nEscolha um algoritmo:")
        print("1. FCFS")
        print("2. SJF (Não-Preemptivo)")
        print("3. SJF (Preemptivo)")
        print("4. Prioridade")
        print("5. Round Robin")
        print("6. Sair")
        escolha = int(input("Digite sua escolha: "))

        if escolha == 6:
            break

        processos = obter_processos()

        if escolha == 1:
            processos_concluidos = fcfs(processos)
        elif escolha == 2:
            processos_concluidos = sjf_nao_preemptivo(processos)
        elif escolha == 3:
            processos_concluidos = sjf_preemptivo(processos)
        elif escolha == 4:
            processos_concluidos = escalonamento_prioridade(processos)
        elif escolha == 5:
            quantum = int(input("Digite o quantum de tempo: "))
            processos_concluidos = round_robin(processos, quantum)
        else:
            print("Escolha inválida!")
            continue

        print("\nDetalhes da execução dos processos:")
        for processo in processos_concluidos:
            print(processo)

if __name__ == "__main__":
    main()
