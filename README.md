# Simulador de Algoritmos de Escalonamento

Este é um programa em Python que simula o escalonamento de processos utilizando diferentes algoritmos de escalonamento, como FCFS, SJF (Preemptivo e Não-Preemptivo), Prioridade e Round Robin.

## Como funciona

O programa consiste em uma implementação de classes e funções que representam processos e algoritmos de escalonamento. Aqui está uma visão geral das principais partes do código:

- `Processo`: Classe que define um processo com atributos como PID, tempo de execução, prioridade, etc.
- Algoritmos de escalonamento:
  - `fcfs`: First-Come, First-Served (FCFS) - executa os processos na ordem em que eles chegaram.
  - `sjf_nao_preemptivo`: Shortest Job First (SJF) Não-Preemptivo - executa o processo mais curto primeiro.
  - `sjf_preemptivo`: Shortest Job First (SJF) Preemptivo - executa o processo mais curto atualmente na fila.
  - `escalonamento_prioridade`: Escalonamento por Prioridade - executa os processos de acordo com sua prioridade.
  - `round_robin`: Round Robin - executa os processos de forma circular, com cada processo recebendo um quantum de tempo de execução.
- `obter_processos`: Função para obter os detalhes dos processos a serem escalonados a partir da entrada do usuário.
- `main`: Função principal que permite ao usuário escolher o algoritmo de escalonamento e exibe os detalhes da execução dos processos.

## Como usar

Para executar o programa, siga estas etapas:

1. Clone o repositório ou baixe o arquivo `escalonamento_processos.py`.
2. Certifique-se de ter o Python instalado em seu sistema.
3. Execute o arquivo `escalonamento_processos.py`.
4. Siga as instruções na tela para escolher o algoritmo de escalonamento e fornecer os detalhes dos processos.

## Exemplo de uso

Aqui está um exemplo de como usar o programa:

```bash
$ python escalonamento_processos.py
```

Em seguida, siga as instruções na tela para selecionar um algoritmo de escalonamento e inserir os detalhes dos processos.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
