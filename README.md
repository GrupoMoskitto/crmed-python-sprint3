<h1 align="center">
  <img src="logo.svg" alt="CRMed" width="80" valign="middle"> CRMed — Dynamic Programming
</h1>
<p align="center">Sistema inteligente de relacionamento e performance clínica para o Hospital São Rafael.</p>
<p align="center">
  <a href="https://github.com/GrupoMoskitto/CRMed-Python-Sprint3/actions/workflows/tests.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/GrupoMoskitto/CRMed-Python-Sprint3/tests.yml?style=flat&branch=main&label=CI&logo=githubactions&logoColor=white" /></a>&nbsp;
  <a href="https://github.com/GrupoMoskitto/CRMed-Python-Sprint3"><img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white" /></a>&nbsp;
  <a href="https://github.com/GrupoMoskitto/CRMed-Python-Sprint3"><img alt="Pytest" src="https://img.shields.io/badge/Pytest-0A9ED9?style=flat&logo=pytest&logoColor=white" /></a>
</p>

<br>

---

### Sobre

O **CRMed** é o cérebro operacional do **Hospital São Rafael** (especializado em cirurgias eletivas e plásticas). Este módulo implementa os conceitos de **Programação Dinâmica** (Recursão + Memoização) aplicados ao CRM.

**Funcionalidades implementadas:**

- **Verificação de Duplicidade** — Detecção recursiva de leads duplicados por CPF, e-mail, telefone ou nome
- **Memoização** — Cache para evitar comparações repetidas entre cadastros
- **Otimização de Agenda** — Algoritmo DP para melhor encaixe de procedimentos nos horários disponíveis

### Stack

| Camada | Tecnologia |
| --- | --- |
| **Linguagem** | Python 3.10+ |
| **Dados** | pandas |
| **Testes** | pytest |
| **CI/CD** | GitHub Actions |


### Quick Start

```bash
# Clone
git clone https://github.com/GrupoMoskitto/crmed-python-sprint3.git
cd crmed-python-sprint3

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Execute a demo
python main.py

# Execute os testes
pytest tests/ -v
```

### Tarefas Implementadas

#### Tarefa 1 — Verificação Recursiva de Duplicidade

```python
from src.duplicated_check import verificar_duplicidade_recursiva

novo_lead = {"nome": "João Silva", "cpf": "123.456.789-00"}
cadastros = [...]

resultado = verificar_duplicidade_recursiva(novo_lead, cadastros)
# Retorna True se encontrar duplicata
```

#### Tarefa 2 — Memoização

```python
from src.duplicated_check import verificar_com_memo

resultado, comparacoes, cache = verificar_com_memo(novo_lead, cadastros)
# Usa cache para evitar recalcular comparações já feitas
```

#### Tarefa 3 — Otimização de Agenda (DP)

```python
from src.agenda_optimizer import calcular_melhor_encaixe

horarios = ["08:00", "08:30", "09:00", ...]
procedimentos = ["Abdominoplastia", "Mamoplastia", "Blefaroplastia"]

resultado = calcular_melhor_encaixe(horarios, procedimentos, PROCEDIMENTOS)
# Retorna melhor combinação usando programação dinâmica
```

### Dados

Os dados são carregados dinamicamente do arquivo CSV [`leads_2026-04-04.csv`](leads_2026-04-04.csv), contendo 58 leads do Hospital São Rafael.

| Campo | Descrição |
| --- | --- |
| **Origens** | Instagram, Facebook, TikTok, Site, Indicação |
| **Procedimentos** | Abdominoplastia, Mamoplastia, Blefaroplastia, Rinoplastia, etc. |
| **Status** | Novo, Contatado, Qualificado, Convertido, Perdido |

### Regras de Negócio

| RN | Descrição | Prioridade |
| --- | --- | --- |
| **RN01** | **Duplicidade Zero** — Proibido cadastrar pacientes com CPF, e-mail ou telefone duplicados | Crítica |

### Scripts

| Comando | Descrição |
| --- | --- |
| `python main.py` | Executa a demo com todas as funcionalidades |
| `pytest tests/ -v` | Executa todos os testes unitários |
| `pytest tests/ -v --cov=src` | Executa testes com coverage |

### CI/CD

O pipeline GitHub Actions executa automaticamente:

- **Testes** — Validação com pytest
- **Cobertura** — Relatório de coverage

> [!TIP]
> Acompanhe os resultados em [GitHub Actions](https://github.com/GrupoMoskitto/CRMed-Python-Sprint3/actions). Cada push mostra se os testes passaram e os logs de execução.

### Equipe

| Nome | GitHub | LinkedIn |
| --- | --- | --- |
| **Gabriel Couto Ribeiro** | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/rouri404) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabricouto/) |
| **Gabriel Kato Peres** | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/kato8088) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabrikato/) |
| **João Vitor de Matos** | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/joaomatosq) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joaomatosq/) |
| **Marcelo Affonso Fonseca** | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/marcelo215) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marcelo-affonso-fonseca-899682333/) |

---

<p align="center">
  Desenvolvido pelo <strong>Grupo Moskitto</strong> para o Challenge FIAP — Dynamic Programming.
</p>
