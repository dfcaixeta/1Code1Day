## 📌 Síntese
Esse código é um gerador de tabuadas múltiplas e personalizadas. Ele:

- Permite que o usuário digite vários números separados de uma vez (ex.: 1, 3, 5 ...).
- Usa um laço `for` com a função `range` para percorrer os valores de 1 até o limite informado.
- O programa solicita um *limite* final para a Tabuada.
- Converte a entrada (_string_) em uma lista de inteiros.
   - split(",") divide a _string_ em partes, separados por vírgulas.
   - strip() remove os espaços extras.
   - int() converte cada parte em um número inteiro.
   - O resultado será uma lista de números ([1, 3, 5]).
- Para cada número, calcula sua tabuada até *o limite escolhido*.
   - Usa *f-string* para formatar a saída de forma clara.
- Organiza a saída com títulos e separadores.
- Finaliza com uma mensagem de encerramento.
