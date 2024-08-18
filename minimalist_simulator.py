# Use esse código para testar entradas em python
# OBS: O destino é lido antes da origem

def covert_timezone(partida, origem, destino):
    return destino - origem + partida

def get_timezone_signal(is_east, time):
    return -(time) if is_east else time


origem_oeste = False # altere aqui para mudar para oeste ou leste
destino_oeste = True # altere aqui para mudar para oeste ou leste

fuso_destino = get_timezone_signal(destino_oeste, int(input()) / 2)
fuso_origem = get_timezone_signal(origem_oeste, int(input()) / 2)



hora_partida_origem = int(input())
duracao = int(input())


def format_24h(time):
    if time >= 24:
        return time - 24
    if time < 0:
        return time + 24
    return time



hora_partida_destino = covert_timezone(hora_partida_origem, fuso_origem, fuso_destino)

result = format_24h(hora_partida_destino + duracao)

print(result)



