# 📌 Síntese do código

Esse código é um *gerador de tabuada usando funções lambda e map* que:

- Pede ao usuário um número inteiro que é armazenado na variável *num*.
- Cria uma *lista* (table) com os resultados da multiplicação desse número por valores de 1 a 10.

  - range(1, 11) gera os números de 1 até 10.
  - lambda x: num * x define uma função anônima que multiplica o número digitado (num) por cada valor x do intervalo.
  - map(...) aplica essa função a todos os valores do range.
  - list(...) transforma o resultado em uma lista chamada table, que contém os produtos da tabuada.

        ➡️ Exemplo: se num = 7, então table = [7, 14, 21, ..., 70]

- Percorre a lista com um laço *for* e imprime cada operação formatada.
  - O laço percorre os índices de 0 a 9 (10 elementos).
  - Em cada repetição:
    - i + 1 representa o incremento multiplicador (de 1 a 10).
    - table[i] acessa o resultado correspondente da lista.

- Finaliza com uma mensagem de encerramento.

👉 Em resumo: é uma versão que combina programação funcional (lambda + map) com um laço for, mostrando que existem diferentes formas de implementar a mesma lógica para uma tabuada em Python.
