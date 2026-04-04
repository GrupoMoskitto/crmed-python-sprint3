import os
import pandas as pd
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "leads_2026-04-04.csv"


def carregar_leads() -> list[dict]:
    df = pd.read_csv(CSV_PATH, sep=";")
    df = df.fillna("")
    return df.to_dict(orient="records")


LEADS_CSV = carregar_leads()

MEDICOS = [
    {"id": 1, "nome": "Dr. Rafael", "especialidade": "Cirurgião Plástico", "dias_atendimento": [1, 2, 3, 4, 5], "horario_inicio": "08:00", "horario_fim": "18:00", "tempo_consulta": 45},
    {"id": 2, "nome": "Dra. Ana", "especialidade": "Cirurgião Plástico", "dias_atendimento": [1, 2, 3, 4, 5], "horario_inicio": "09:00", "horario_fim": "17:00", "tempo_consulta": 30},
    {"id": 3, "nome": "Dr. Matheus", "especialidade": "Cirurgião Plástico", "dias_atendimento": [2, 3, 4], "horario_inicio": "08:00", "horario_fim": "16:00", "tempo_consulta": 60},
]

PROCEDIMENTOS = {
    "Abdominoplastia": 90,
    "Mamoplastia": 60,
    "Mamoplastia + Abdominoplastia": 120,
    "Blefaroplastia": 45,
    "Próteses": 60,
    "Rinoplastia": 90,
    "Rinoplastia + Otoplastia": 120,
    "Otoplastia": 45,
    "Lipo HD": 90,
    "Lipoaspiração": 90,
}

ORIGENS = ["Instagram", "Facebook", "TikTok", "Site", "Indicação"]

STATUS_LEAD = ["Novo", "Contatado", "Qualificado", "Convertido", "Perdido"]
