import pytest
from src.duplicated_check import (
    verificar_duplicidade_recursiva,
    verificar_com_memo,
    verificar_com_lru_cache,
    verificar_todas_combinacoes,
    sao_duplicados,
    comparar_campos,
)

from src.agenda_optimizer import (
    otmizar_agenda_dp,
    calcular_encaixe,
    gerar_horarios,
    otmizar_gulosa,
    comparar,
    minutos,
    horario,
)


class TestDuplicatedCheck:
    def setup_method(self):
        self.cadastros = [
            {"nome": "Joao Silva", "email": "joao@email.com", "telefone": "(11) 99999-0000", "cpf": "123.456.789-00"},
            {"nome": "Maria Santos", "email": "maria@email.com", "telefone": "(11) 99999-1111", "cpf": "987.654.321-00"},
            {"nome": "Pedro Costa", "email": "pedro@email.com", "telefone": "(11) 99999-2222", "cpf": "456.123.789-00"},
        ]
    
    def test_campos_iguais(self):
        assert comparar_campos("Joao Silva", "joao silva") is True
        assert comparar_campos("  Maria  ", "maria") is True
        assert comparar_campos("Teste", "Diferente") is False
        assert comparar_campos(None, "Teste") is False
    
    def test_sao_duplicados_cpf(self):
        lead1 = {"nome": "Joao Silva", "cpf": "123.456.789-00"}
        lead2 = {"nome": "Joao Diferente", "cpf": "123.456.789-00"}
        assert sao_duplicados(lead1, lead2) is True
    
    def test_sao_duplicados_email(self):
        lead1 = {"nome": "Joao Silva", "email": "joao@email.com"}
        lead2 = {"nome": "Maria Santos", "email": "joao@email.com"}
        assert sao_duplicados(lead1, lead2) is True
    
    def test_sao_duplicados_telefone(self):
        lead1 = {"nome": "Joao Silva", "telefone": "(11) 99999-0000"}
        lead2 = {"nome": "Maria Santos", "telefone": "(11) 99999-0000"}
        assert sao_duplicados(lead1, lead2) is True
    
    def test_nao_sao_duplicados(self):
        lead1 = {"nome": "Joao Silva", "cpf": "111.111.111-11"}
        lead2 = {"nome": "Maria Santos", "cpf": "222.222.222-22"}
        assert sao_duplicados(lead1, lead2) is False
    
    def test_verificacao_recursiva_encontra_duplicado(self):
        novo = {"nome": "Joao Silva", "cpf": "123.456.789-00"}
        assert verificar_duplicidade_recursiva(novo, self.cadastros) is True
    
    def test_verificacao_recursiva_sem_duplicado(self):
        novo = {"nome": "Novo Lead", "cpf": "000.000.000-00"}
        assert verificar_duplicidade_recursiva(novo, self.cadastros) is False
    
    def test_verificacao_com_memo(self):
        novo = {"nome": "Joao Silva", "cpf": "123.456.789-00"}
        resultado, comparacoes, cache = verificar_com_memo(novo, self.cadastros)
        assert resultado is True
        assert comparacoes > 0
    
    def test_verificacao_com_lru_cache(self):
        novo = {"nome": "Joao Silva", "cpf": "123.456.789-00"}
        resultado = verificar_com_lru_cache(novo, self.cadastros)
        assert resultado is True
    
    def test_verificar_todas_combinacoes(self):
        novo = {"nome": "Novo", "cpf": "987.654.321-00"}
        resultado = verificar_todas_combinacoes(novo, self.cadastros)
        assert resultado["duplicado"] is True
        assert resultado["campo_duplicado"] == "cpf"
        assert resultado["indice_encontrado"] == 1


class TestAgendaOptimizer:
    def setup_method(self):
        self.horarios = ["08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30"]
        self.db = {"Blefaroplastia": 45, "Rinoplastia": 90, "Abdominoplastia": 90, "Proteses": 60, "Mamoplastia": 60}
        self.procedimentos = ["Rinoplastia", "Blefaroplastia", "Abdominoplastia", "Proteses"]
    
    def test_minutos(self):
        assert minutos("08:00") == 480
        assert minutos("08:30") == 510
        assert minutos("18:00") == 1080
    
    def test_horario(self):
        assert horario(480) == "08:00"
        assert horario(510) == "08:30"
        assert horario(1080) == "18:00"
    
    def test_gerar_horarios(self):
        horarios = gerar_horarios("08:00", "10:00", 30)
        assert len(horarios) == 4
        assert horarios[0] == "08:00"
        assert horarios[-1] == "09:30"
    
    def test_otmizar_agenda_dp(self):
        resultado = otmizar_agenda_dp(self.horarios, self.procedimentos, self.db)
        assert resultado[0] > 0
        assert len(resultado[1]) == resultado[0]
    
    def test_calcular_encaixe(self):
        resultado = calcular_encaixe(self.horarios, self.procedimentos, self.db)
        assert "procedimentos_agendados" in resultado
        assert "tempo_total_disponivel" in resultado
        assert resultado["tempo_usado"] <= resultado["tempo_total_disponivel"]
    
    def test_otmizar_gulosa(self):
        resultado = otmizar_gulosa(self.horarios, self.procedimentos, self.db)
        assert resultado[0] > 0
    
    def test_comparar(self):
        resultado = comparar(self.horarios, self.procedimentos, self.db)
        assert "dp" in resultado
        assert "guloso" in resultado
        assert resultado["dp"]["procedimentos_agendados"] >= resultado["guloso"]["procedimentos_agendados"]
    
    def test_agenda_vazia(self):
        import src.agenda_optimizer as agenda_module
        agenda_module.memo_agenda = {}
        resultado = otmizar_agenda_dp(self.horarios, [], self.db)
        assert resultado[0] == 0
        assert resultado[1] == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
