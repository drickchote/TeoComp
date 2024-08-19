OBS: A nossa MT é por Parada

Ex: de entradas e saidas:

- ␣ -> ␣ (fita vazia)
- 11 -> 11 (fita menor que 24)
- 111111111111111111111111 -> 111111111111111111111111 (fita = 24)
- 1111111111111111111111111 -> 1 (fita = 25)
- 11111111111111111111111111111111111111111111111111 -> 11 (fita = 50)

1. Se a fita estiver em branco, ela para em h1.
2.  Senão, lê os 24 valores de entrada e substitui por x (h1 -> h24) e vai pro estado overflow
3.  Verifica se o próximo valor é vazio ou número, 
    - Caso vazio:
        3.1. chama o estado print 
        3.2. Imprime os 24 números 
        3.3- obs: 0h é o dia atual, 24h é o dia seguinte
    - Caso número: 
        3.1. muda pro estado clean
        3.2. apaga todo os 24 números da esquerda
        3.3. volta para a direita até achar um número
        3.4. após achar um número chama restart e vai para a esquerda
        3.5. restart lê o valor vazio e volta para h1 (passo 1)


