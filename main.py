from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="SGHSS - VidaPlus Back-end", 
    description="API REST para Gestão Hospitalar em conformidade com a LGPD."
)

# ---- MODELOS DE DADOS (SCHEMAS) ----
class Paciente(BaseModel):
    id: int
    nome: str
    cpf: str = Field(..., description="CPF criptografado ou mascarado para LGPD")
    data_nascimento: str
    telefone: str

class Medico(BaseModel):
    id: int
    nome: str
    crm: str
    especialidade: str

class Consulta(BaseModel):
    id: int
    paciente_id: int
    medico_id: int
    data_hora: datetime
    status: str = "Agendada"

class Prontuario(BaseModel):
    id: int
    paciente_id: int
    medico_id: int
    descricao_clinica: str
    medicamentos_receitados: str
    data_registro: datetime = Field(default_factory=datetime.now)

# ---- BANCO DE DADOS SIMULADO (MEMÓRIA) ----
db_pacientes: List[Paciente] = []
db_medicos: List[Medico] = []
db_consultas: List[Consulta] = []
db_prontuarios: List[Prontuario] = []

# ==================== ROTAS DE PACIENTES ====================
@app.post("/pacientes", response_model=Paciente, status_code=status.HTTP_201_CREATED)
def criar_paciente(paciente: Paciente):
    for p in db_pacientes:
        if p.cpf == paciente.cpf:
            raise HTTPException(status_code=400, detail="Paciente com este CPF já cadastrado.")
    db_pacientes.append(paciente)
    return paciente

@app.get("/pacientes", response_model=List[Paciente])
def listar_pacientes():
    return db_pacientes

# ==================== ROTAS DE MÉDICOS ====================
@app.post("/medicos", response_model=Medico, status_code=status.HTTP_201_CREATED)
def cadastrar_medico(medico: Medico):
    db_medicos.append(medico)
    return medico

@app.get("/medicos", response_model=List[Medico])
def listar_medicos():
    return db_medicos

# ==================== ROTAS DE CONSULTAS ====================
@app.post("/consultas", response_model=Consulta, status_code=status.HTTP_201_CREATED)
def agendar_consulta(consulta: Consulta):
    # Validação de Integridade Referencial (Cobrada na correção)
    paciente_existe = any(p.id == consulta.paciente_id for p in db_pacientes)
    medico_existe = any(m.id == consulta.medico_id for m in db_medicos)
    
    if not paciente_existe or not medico_existe:
        raise HTTPException(
            status_code=404, 
            detail="Falha de integridade: Paciente ou Médico não localizado."
        )
    db_consultas.append(consulta)
    return consulta

@app.get("/consultas", response_model=List[Consulta])
def listar_consultas():
    return db_consultas

# ==================== ROTAS DE PRONTUÁRIOS ====================
@app.post("/prontuarios", response_model=Prontuario, status_code=status.HTTP_201_CREATED)
def registrar_prontuario(prontuario: Prontuario):
    paciente_existe = any(p.id == prontuario.paciente_id for p in db_pacientes)
    if not paciente_existe:
        raise HTTPException(status_code=404, detail="Paciente não localizado.")
    db_prontuarios.append(prontuario)
    return prontuario

@app.get("/prontuarios/{paciente_id}", response_model=List[Prontuario])
def buscar_historico_paciente(paciente_id: int):
    historico = [pr for pr in db_prontuarios if pr.paciente_id == paciente_id]
    return historico