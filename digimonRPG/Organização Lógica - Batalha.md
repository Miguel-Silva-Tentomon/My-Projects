## Até o final...

Fazer um sistema de batalha que contenha:

Menu, com as opções:

- Atacar
- Mover?
- Defender
- Item
- Fugir

Pelo menos 2 até 3 aliados controláveis.

Pelo menos 2 até 5 inimigos combatíveis.

TALVEZ:

O posicionamento do digimon garantir buff de status a quem está do lado.

Uma barra na batalha que se enche de acordo com os hits causados e levados (de forma similar a barra de DNA do digimon world 3)

Aplicar interface gráfica com pygame que represente a lógica do programa (assim até parece um jogo mesmo, uau!)

## Organização Lógica - Batalha

Batalha começa

Menu aparece com opções:

- Atacar:
  - Altera o hp de algum inimigo **escolhido**
- Mover
  - Move a posição de um aliado (poderia ser baseado em um vetor talvez?)
- Defender
  - Bom, defende. Diminui o dano recebido até ser o **turno** da unidade em específico novamente
  - (Como vou contar o turno de forma que interaja com uma classe e seus atributos???) (É possível criar a função de defesa e largar defesa na classe digimon de acordo com a ordem dos turnos com uma **booleana** de "está defendendo")
- Item
  - Abre outro menu que permite usar funções similares de alteração de HP/MP/Status ou até barra de DNA
- Fugir
  - Roda algum número aleatório pra cancelar a batalha caso seja positivo (decidido por alguma variável lógica talvez?)

Fim do turno (jogador)

O inimigo irá executar alguma ação de acordo com as opções existentes mas de forma totalmente aleatória (sem nenhuma lógica especial).

Exemplo:

Ações possíveis: 1(Atacar) 2(Defender) 3(Fugir) 4(Usar um item aleatório??)
O número é definido por alguma função de pseudoaleatoriedade 

## Classes

### Digimon

| NOME   | DEFENDENDO | HP   | MP   | ATK  | RES  | SPEED |
| ------ | ---------- | ---- | ---- | ---- | ---- | ----- |
| Agumon | TRUE/FALSE |      |      |      |      |       |
|        |            |      |      |      |      |       |

#### Funções

- sofreDano: self.hp - dano
- recuperaVida: self.hp + regen
- defender: defesa * 2
- pararDefesa: defesa / 2