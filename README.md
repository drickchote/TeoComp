# viagem-ao-mundo

Prática de Implementação: Máquina de Turing - Teoria da Computação.

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/drickchote/TeoComp?color=%2304D361">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/drickchote/TeoComp">
  
  <a href="https://github.com/caiovinisl/metodos-hashing/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/drickchote/TeoComp">
  </a>
   
   <a href="https://github.com/drickchote/TeoComp/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/drickchote/TeoComp?style=social">
  </a>
  
 
</p>

<h4 align="center"> 
	🚧 Viagem ao Mundo 🚧
</h4>

<p align="center">
	<img alt="Status Concluído" src="https://img.shields.io/badge/STATUS-CONCLU%C3%8DDO-brightgreen">
</p>

<p align="center">
 <a href="#-sobre-o-projeto">Sobre</a> •
 <a href="#%EF%B8%8F-funcionamento">Funcionamento</a> •
 <a href="#%EF%B8%8F-como-executar-o-projeto">Como executar</a> • 
 <a href="#-tecnologias">Tecnologias</a>
</p>

## 💻 Sobre o projeto
Funcionamento (exemplo minimalista - veja o arquivo [minimalist.yaml](/standard/minimalist.yaml)).

Esse exemplo considera os graus como múltiplos de 2 ao invés de 15.

## ⚙️ Funcionamento
Converter a entrada em operações matemáticas com somas e subtrações. 
O primeiro passo consiste em converter `o11o11#111#11` para `+111+11-1+1*`

Temos 4 entradas: destino, origem, hora de início e hora de fim, respectivamente.
Os sinais da hora de início e hora de fim sempre serão positivos. 
Porém, só alteramos o separador deles na formatação final.

O sinal da primeira entrada depende de ser oeste ou leste, a ideia é calcular a distância dos fuso horários com a fórmula: hora_destino - hora_origem. Sabemos que se a entrada for oeste, o fuso horário é negativo, se a entrada for leste, o fuso horário é positivo.

Para a primeira entrada (destino) temos:
- Caso seja oeste: o sinal é negativo
- Caso seja leste, o sinal é positivo

Para a segunda entrada (origem) temos:
- Caso seja oeste: o sinal é positivo (O sinal se altera por conta do `-` da fórmula destino - origem)
- Caso seja leste, o sinal é negativo (O sinal se altera por conta do `-` da fórmula destino - origem)

Em resumo, temos 2 passos principais:
1. `o11o11#111#11`: pega essa entrada e converte para uma fórmula `+111+11-1+1*`
2. `+111+11-1+1*`: pega esse resultado e põe depois do asterístico e após isso, apaga o asterístico.



### Destrinchamento da parte 1:
A entrada é realizada na ordem:
destino, origem, horário de saída, duração respectivamente

1. O sinal da primeira entrada é calculado:
    - Caso seja oeste: o sinal é negativo
    - Caso seja leste, o sinal é positivo
    - Transição da fita: `o11o11#111#11` -> `11o11#111#11-`

2. Os valores 1 são divididos por 15 (nesse exemplo minimalista dividimos por 2)
    - `11o11#111#11-` -> `o11#111#11-1`
3. O sinal da segunda entrada é calculado:
    - Caso seja oeste: o sinal é positivo
    - Caso seja leste, o sinal é negativo
    - `o11#111#11-1` -> `11#111#11-1+`

4. Os valores 1 são divididos por 15 (nesse exemplo minimalista dividimos por 2)
    - `11#111#11-1+` -> `#111#11-1+1`
5. Usamos o estado format para converter os separadores para +
    - `#111#11-1+1 `-> `+111+11-1+1` 

### Destrinchamento da parte 2:
1. `+111+11-1+1*` -> usa o estado "sum" para mover o `+` para a direita e chamada "add_1"
2. `+11+11-1+1*1` -> usa o estado "sum" para mover o `+` para a direita e chamada "add_1"
3. `+1+11-1+1*11` -> usa o estado "sum" para mover o `+` para a direita e chamada "add_1"
4. `++11-1+1*111` -> usa o estado "sum" para mover o `+` para a direita e chamada "add_1"
4. `+11-1+1*111` -> remove o `+` e volta para "sum"
5. `+1-1+1*1111` -> usa o estado "sum" para mover o `+` para a direita e chamada "add_1"
6. `+-1+1*11111` -> remove o `+` e volta para "sum"
7. `-1+1*11111` -> usa o estado "sub" para mover o `-` para a direita e chamada "sub_1"
8. `-+1*1111` -> remove o `-` e vai para "sub"
9.  `+*11111` -> remove o `+` e volta para "sum"
10. `*11111` -> remove o asterístico e volta para "end"
11. `11111`

## 💻 Como executar o projeto

A Máquina de Turing padrão desenvolvida neste projeto pode ser visualizada e executada passo-a-passo no site **[turingmachine.io](https://turingmachine.io/)**, bastando copiar e colar o conteúdo do arquivo [standard.yaml](/standard/standard.yaml) para servir como as instruções da máquina.

Já para executar a Máquina de Turing alternativa, será necessário usar o software [JFLAP](https://www.jflap.org/) e importar o arquivo [alternative.jff](/alternative/alternative.jff).


## 🛠 Tecnologias

- **[Python](https://www.python.org/)**
- **[JFLAP](https://www.jflap.org/)**
- **[Turing Machine Vizualization](https://turingmachine.io/)**

---
