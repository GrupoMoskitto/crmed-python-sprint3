memo_agenda = {}

def minutos(horario):
    h, m = horario.split(":")
    return int(h) * 60 + int(m)

def horario(minutos_total):
    h = minutos_total // 60
    m = minutos_total % 60
    return f"{h:02d}:{m:02d}"

def gerar_horarios(inicio, fim, intervalo):
    horarios = []
    atual = minutos(inicio)
    fim_min = minutos(fim)
    
    while atual < fim_min:
        horarios.append(horario(atual))
        atual += intervalo
    
    return horarios

def duracao(procedimento, db):
    return db.get(procedimento, 60)

def otmizar_agenda_dp(horarios, procedimentos, db, index=0, tempo_usado=0):
    global memo_agenda
    
    key = (index, tempo_usado)
    if key in memo_agenda:
        return memo_agenda[key]
    
    tempo_total = minutos(horarios[-1]) if horarios else 0
    
    if index >= len(procedimentos) or tempo_usado >= tempo_total:
        memo_agenda[key] = (0, [])
        return memo_agenda[key]
    
    dur = duracao(procedimentos[index], db)
    
    if tempo_usado + dur <= tempo_total:
        resultado_com = otmizar_agenda_dp(horarios, procedimentos, db, index + 1, tempo_usado + dur)
        resultado_com = (resultado_com[0] + 1, [procedimentos[index]] + resultado_com[1])
    else:
        resultado_com = (0, [])
    
    resultado_sem = otmizar_agenda_dp(horarios, procedimentos, db, index + 1, tempo_usado)
    
    memo_agenda[key] = resultado_com if resultado_com[0] >= resultado_sem[0] else resultado_sem
    
    return memo_agenda[key]

def calcular_encaixe(horarios, procedimentos, db):
    global memo_agenda
    memo_agenda = {}
    
    tempo_total = minutos(horarios[-1]) if horarios else 0
    selecionados = otmizar_agenda_dp(horarios, procedimentos, db)
    
    tempo_usado = sum(duracao(p, db) for p in selecionados[1])
    
    return {
        "procedimentos_totais": len(procedimentos),
        "procedimentos_agendados": selecionados[0],
        "lista_procedimentos": selecionados[1],
        "tempo_total_disponivel": tempo_total,
        "tempo_usado": tempo_usado,
        "tempo_livre": tempo_total - tempo_usado,
        "horarios_utilizados": gerar_agenda(selecionados[1], db, horarios[0] if horarios else "08:00")
    }

def gerar_agenda(procedimentos, db, inicio):
    agenda = []
    hora = minutos(inicio)
    
    for proc in procedimentos:
        dur = duracao(proc, db)
        agenda.append({
            "procedimento": proc,
            "inicio": horario(hora),
            "fim": horario(hora + dur),
            "duracao": dur
        })
        hora += dur
    
    return agenda

def ordenar_duracao(procedimentos, db):
    lista = list(procedimentos)
    n = len(lista)
    
    for i in range(n):
        for j in range(i + 1, n):
            if duracao(lista[i], db) > duracao(lista[j], db):
                lista[i], lista[j] = lista[j], lista[i]
    
    return lista

def otmizar_gulosa(horarios, procedimentos, db):
    tempo_total = minutos(horarios[-1]) if horarios else 0
    ordenados = ordenar_duracao(procedimentos, db)
    
    tempo_usado = 0
    selecionados = []
    
    for proc in ordenados:
        dur = duracao(proc, db)
        if tempo_usado + dur <= tempo_total:
            selecionados.append(proc)
            tempo_usado += dur
    
    return len(selecionados), selecionados

def comparar(horarios, procedimentos, db):
    global memo_agenda
    memo_agenda = {}
    
    dp = calcular_encaixe(horarios, procedimentos, db)
    guloso = otmizar_gulosa(horarios, procedimentos, db)
    
    return {
        "dp": dp,
        "guloso": {
            "procedimentos_agendados": guloso[0],
            "lista_procedimentos": guloso[1]
        }
    }