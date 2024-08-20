Ex: de entradas e saidas:

-* -> -*11111111111111111111111
-11* -> -11*111111111111111111111 (Isso será processado pelos outros módulos da MT)
-11+111* -> -11+111*111111111111111111111 (Isso será processado pelos outros módulos da MT) *

Quando o estado pop tenta remover e ao invés de encontrar um '1', encontra um *, significa que não tem mais como subtrair pois já estamos em 0h. Então, ao invés de subtrair, adicionamos 23h e aplicamos o reset para continuar o processamento da fita.


*Obs: É possível que adicionemos 23h e logo depois adicionemos mais fazendo com que tenhamos que remover 24h logo depois.
