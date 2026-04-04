from functools import lru_cache
import time

memo_cache = {}

def normalizar(texto):
    if texto is None:
        return ""
    return texto.strip().lower()

def comparar_campos(campo1, campo2):
    if campo1 is None or campo2 is None:
        return False
    return normalizar(str(campo1)) == normalizar(str(campo2))

def sao_duplicados(lead1, lead2):
    if comparar_campos(lead1.get("cpf"), lead2.get("cpf")):
        return True
    if comparar_campos(lead1.get("email"), lead2.get("email")):
        return True
    if comparar_campos(lead1.get("telefone"), lead2.get("telefone")):
        return True
    if comparar_campos(lead1.get("nome"), lead2.get("nome")):
        return True
    return False


def verificar_duplicidade_recursiva(novo_lead, cadastros, index=0):
    if index >= len(cadastros):
        return False
    
    if sao_duplicados(novo_lead, cadastros[index]):
        return True
    
    return verificar_duplicidade_recursiva(novo_lead, cadastros, index + 1)

def verificar_com_memo(novo_lead, cadastros):
    global memo_cache
    memo_cache = {}
    comparacoes = 0
    
    def verificar_com_cache(idx):
        nonlocal comparacoes
        
        if idx >= len(cadastros):
            return False
        
        key = (
            normalizar(novo_lead.get("cpf", "")),
            normalizar(novo_lead.get("email", "")),
            normalizar(novo_lead.get("telefone", "")),
            normalizar(novo_lead.get("nome", "")),
            idx
        )
        
        if key in memo_cache:
            return memo_cache[key]
        
        comparacoes += 1
        resultado = sao_duplicados(novo_lead, cadastros[idx])
        
        if not resultado:
            resultado = verificar_com_cache(idx + 1)
        
        memo_cache[key] = resultado
        return resultado
    
    resultado = verificar_com_cache(0)
    return resultado, comparacoes, memo_cache

def verificar_com_lru_cache(novo_lead, cadastros):
    @lru_cache(maxsize=1024)
    def comparar(cpf, email, telefone, nome, idx):
        if idx >= len(cadastros):
            return False
        
        cadastro = cadastros[idx]
        
        if (comparar_campos(cpf, cadastro.get("cpf")) or
            comparar_campos(email, cadastro.get("email")) or
            comparar_campos(telefone, cadastro.get("telefone")) or
            comparar_campos(nome, cadastro.get("nome"))):
            return True
        
        return comparar(cpf, email, telefone, nome, idx + 1)
    
    return comparar(
        novo_lead.get("cpf", ""),
        novo_lead.get("email", ""),
        novo_lead.get("telefone", ""),
        novo_lead.get("nome", ""),
        0
    )

def verificar_todas_combinacoes(novo_lead, cadastros):
    resultado = {
        "duplicado": False,
        "campo_duplicado": None,
        "indice_encontrado": None,
        "comparacoes": 0
    }
    
    for idx, cadastro in enumerate(cadastros):
        resultado["comparacoes"] += 1
        
        if comparar_campos(novo_lead.get("cpf"), cadastro.get("cpf")):
            return {**resultado, "duplicado": True, "campo_duplicado": "cpf", "indice_encontrado": idx}
        
        if comparar_campos(novo_lead.get("email"), cadastro.get("email")):
            return {**resultado, "duplicado": True, "campo_duplicado": "email", "indice_encontrado": idx}
        
        if comparar_campos(novo_lead.get("telefone"), cadastro.get("telefone")):
            return {**resultado, "duplicado": True, "campo_duplicado": "telefone", "indice_encontrado": idx}
        
        if comparar_campos(novo_lead.get("nome"), cadastro.get("nome")):
            return {**resultado, "duplicado": True, "campo_duplicado": "nome", "indice_encontrado": idx}
    
    return resultado

def benchmark(novo_lead, cadastros):
    resultados = {}
    
    start = time.time()
    verificar_duplicidade_recursiva(novo_lead, cadastros)
    resultados["recursiva"] = time.time() - start
    
    start = time.time()
    verificar_com_memo(novo_lead, cadastros)
    resultados["memo"] = time.time() - start
    
    start = time.time()
    verificar_com_lru_cache(novo_lead, cadastros)
    resultados["lru_cache"] = time.time() - start
    
    return resultados