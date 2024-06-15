# Simulação de Algoritmos de Escalonamento de Processos

Este programa implementa cinco algoritmos de escalonamento de processos em Python, permitindo que o usuário escolha um algoritmo, insira os processos e visualize os resultados da simulação.

## Algoritmos Disponíveis

1. FCFS (First-Come, First-Served)
2. SJF (Shortest Job First) Não-Preemptivo
3. SJF (Shortest Job First) Preemptivo
4. Escalonamento por Prioridade
5. Round Robin

## Requisitos

- Python 3.x

## Como Usar

### Passo 1: Clone o Repositório

```sh
git clone https://github.com/cl1sman/Simulador-de-Algoritmos-de-Escalonamento.git
cd Simulador-de-Algoritmos-de-Escalonamento
```

### Passo 2: Execute o Script

```sh
python escalonamento.py
```

### Passo 3: Escolha um Algoritmo

Após executar o script, você verá um menu para selecionar um dos algoritmos de escalonamento:

```
Escolha um algoritmo:
1. FCFS
2. SJF (Não-Preemptivo)
3. SJF (Preemptivo)
4. Prioridade
5. Round Robin
6. Sair
Digite sua escolha:
```

Digite o número correspondente ao algoritmo que você deseja usar e pressione Enter.

### Passo 4: Insira os Processos

Você será solicitado a inserir o número de processos e os detalhes de cada processo, incluindo o PID, tempo de execução, tempo de chegada e prioridade (se aplicável).

Exemplo de entrada para FCFS:

```
Digite o número de processos: 3
Digite o PID do processo 1: 111
Digite o tempo de execução do processo 1: 5
Digite o tempo de chegada do processo 1: 0
Digite a prioridade do processo 1 (0 se não for usado): 0
Digite o PID do processo 2: 222
Digite o tempo de execução do processo 2: 3
Digite o tempo de chegada do processo 2: 1
Digite a prioridade do processo 2 (0 se não for usado): 0
Digite o PID do processo 3: 333
Digite o tempo de execução do processo 3: 4
Digite o tempo de chegada do processo 3: 2
Digite a prioridade do processo 3 (0 se não for usado): 0
```

### Passo 5: Visualize os Resultados

Após inserir os processos, o programa exibirá os detalhes da execução dos processos, incluindo tempo de conclusão, tempo de retorno e tempo de espera.

Exemplo de saída para FCFS:

```
Detalhes da execução dos processos:
PID: 111, Tempo de Execução: 5, Tempo Restante: 0, Prioridade: 0, Tempo de Chegada: 0, Tempo de Conclusão: 5, Tempo de Retorno: 5, Tempo de Espera: 0
PID: 222, Tempo de Execução: 3, Tempo Restante: 0, Prioridade: 0, Tempo de Chegada: 1, Tempo de Conclusão: 8, Tempo de Retorno: 7, Tempo de Espera: 4
PID: 333, Tempo de Execução: 4, Tempo Restante: 0, Prioridade: 0, Tempo de Chegada: 2, Tempo de Conclusão: 12, Tempo de Retorno: 10, Tempo de Espera: 6
```

### Passo 6: Executar Outro Algoritmo ou Sair

Após visualizar os resultados, você pode escolher executar outro algoritmo ou sair do programa selecionando a opção correspondente no menu inicial.

## Exemplo Completo

Aqui está um exemplo completo usando o algoritmo Round Robin com um quantum de tempo de 2:

1. Escolha o algoritmo Round Robin (5).
2. Insira o número de processos (3).
3. Insira os detalhes dos processos:
    - Processo 1: PID 111, Tempo de Execução 5, Tempo de Chegada 0, Prioridade 0.
    - Processo 2: PID 222, Tempo de Execução 3, Tempo de Chegada 1, Prioridade 0.
    - Processo 3: PID 333, Tempo de Execução 4, Tempo de Chegada 2, Prioridade 0.
4. Insira o quantum de tempo (2).
5. Visualize os resultados.
