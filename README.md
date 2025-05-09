# Análise de Algoritmos de Ordenação

Este projeto realiza a análise empírica de três algoritmos de ordenação: **Bubble Sort**, **Selection Sort** e **Insertion Sort**. O código mede e registra o tempo de execução, número de comparações e número de trocas para listas de diferentes tamanhos e distribuições de dados.

## Algoritmos Implementados

- **Bubble Sort**
- **Selection Sort**
- **Insertion Sort**

## Estrutura do Código

### Funções principais

1. **`gerar_lista(tamanho, tipo)`**: 
   - Gera uma lista de tamanho `tamanho` com os elementos de acordo com o tipo de distribuição especificado:
     - **ordenada**: Lista de elementos em ordem crescente.
     - **inversa**: Lista de elementos em ordem decrescente.
     - **aleatória**: Lista com elementos aleatórios.

2. **`testar_algoritmo(nome_algoritmo, funcao, tamanho, tipo_lista)`**: 
   - Testa o algoritmo de ordenação especificado (passado como `funcao`) com listas de diferentes tipos e tamanhos.
   - Registra o tempo de execução, o número de comparações e o número de trocas realizadas pelo algoritmo.
   
3. **Algoritmos de Ordenação**:
   - **`bubble_sort(arr, comparacoes, trocas)`**: Algoritmo de ordenação *Bubble Sort*.
   - **`selection_sort(arr, comparacoes, trocas)`**: Algoritmo de ordenação *Selection Sort*.
   - **`insertion_sort(arr, comparacoes, trocas)`**: Algoritmo de ordenação *Insertion Sort*.

### Testes Realizados

Os algoritmos foram testados em listas de tamanhos 1.000, 10.000, 50.000 e 100.000 elementos. Foram consideradas três distribuições de entrada:
- **Ordenada**
- **Inversamente ordenada**
- **Aleatória**

A cada execução, o tempo de execução, número de comparações e número de trocas foram registrados para cada combinação de algoritmo, tipo de lista e tamanho.

## Como Executar o Código

1. **Instalação**: Não há dependências externas para rodar o código. Apenas Python 3.x é necessário.
2. **Executar o código**: Basta rodar o arquivo Python contendo o código. O programa irá automaticamente gerar e testar as listas, imprimindo os resultados no terminal.

## Exemplo de Saída

O programa imprimirá os resultados de cada execução no formato:

Bubble Sort | Tipo: aleatoria | Tamanho:  1000 | Tempo: 0.034125 segundos | Comparações: 149850 | Trocas: 74950
Selection Sort | Tipo: aleatoria | Tamanho:  1000 | Tempo: 0.022345 segundos | Comparações: 499500 | Trocas: 249500
Insertion Sort | Tipo: aleatoria | Tamanho:  1000 | Tempo: 0.021129 segundos | Comparações: 999000 | Trocas: 499000

## Métricas Avaliadas

Tempo de execução: O tempo necessário para completar a ordenação, medido em segundos ou minutos (caso exceda 60 segundos).

Número de comparações: Quantidade de comparações realizadas durante a ordenação.

Número de trocas: Quantidade de trocas realizadas entre os elementos da lista.

## Observações
O tempo de execução pode variar dependendo da configuração do ambiente de teste.

Os algoritmos foram testados apenas com listas de inteiros. Para uma análise mais completa, seria interessante incluir outros tipos de dados (por exemplo, floats ou strings).

## Link para a planilha com os dados dos testes realizados

https://docs.google.com/spreadsheets/d/12AWR2URLj6S_9n48auovknUo-ZpY0DltAe9AuHYQim8/edit?usp=sharing

## Licença
Este código é fornecido sob a licença MIT. Sinta-se à vontade para usar, modificar e distribuir conforme necessário.
