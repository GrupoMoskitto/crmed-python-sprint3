from data.mock_data import LEADS_CSV, PROCEDIMENTOS
from src.duplicated_check import verificar_duplicidade_recursiva, verificar_com_memo, verificar_todas_combinacoes
from src.agenda_optimizer import calcular_encaixe, gerar_horarios, comparar

def demo_duplicidade():
    print("=" * 50)
    print("Verificacao de Duplicidade de Leads")
    print("=" * 50)
    
    novo = {"nome": "Joao Silva", "email": "joao@teste.com", "telefone": "(71) 96809-2606", "cpf": "066.788.705-90"}
    print(f"\nNovo lead: {novo['nome']}")
    print(f"CPF: {novo['cpf']}")
    
    print("\n--- Recursiva ---")
    resultado = verificar_duplicidade_recursiva(novo, LEADS_CSV)
    print(f"Duplicado: {resultado}")
    
    print("\n--- Memoizacao ---")
    resultado, comparacoes, cache = verificar_com_memo(novo, LEADS_CSV)
    print(f"Duplicado: {resultado}")
    print(f"Comparacoes: {comparacoes}")
    
    print("\n--- Detalhada ---")
    resultado = verificar_todas_combinacoes(novo, LEADS_CSV)
    print(f"Duplicado: {resultado['duplicado']}")

def demo_agenda():
    print("\n" + "=" * 50)
    print("Otimizacao de Agenda")
    print("=" * 50)
    
    horarios = gerar_horarios("08:00", "14:00", 30)
    print(f"\nHorarios: {len(horarios)} slots ({horarios[0]} - {horarios[-1]})")
    
    procedimentos = ["Abdominoplastia", "Mamoplastia", "Blefaroplastia", "Rinoplastia", "Proteses", "Otoplastia", "Lipo HD"]
    print(f"Procedimentos: {procedimentos}")
    
    print("\n--- DP ---")
    resultado = calcular_encaixe(horarios, procedimentos, PROCEDIMENTOS)
    print(f"Agendados: {resultado['procedimentos_agendados']}/{resultado['procedimentos_totais']}")
    print(f"Tempo usado: {resultado['tempo_usado']} min")
    print(f"Tempo livre: {resultado['tempo_livre']} min")
    
    print("\nAgenda:")
    for item in resultado['horarios_utilizados']:
        print(f"  {item['inicio']} - {item['fim']}: {item['procedimento']}")
    
    print("\n--- Comparacao ---")
    comp = comparar(horarios, procedimentos, PROCEDIMENTOS)
    print(f"DP: {comp['dp']['procedimentos_agendados']} | Guloso: {comp['guloso']['procedimentos_agendados']}")

def main():
    print("\n" + "#" * 50)
    print("CRMed - Dynamic Programming")
    print("#" * 50)
    
    demo_duplicidade()
    demo_agenda()
    
    print("\n" + "#" * 50)
    print("Demo concluida!")
    print("#" * 50 + "\n")

if __name__ == "__main__":
    main()