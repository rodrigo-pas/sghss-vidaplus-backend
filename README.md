# SGHSS - VidaPlus Back-end

API REST para Sistema de Gestão Hospitalar e de Saúde Suplementar (SGHSS) com foco em conformidade com a Lei Geral de Proteção de Dados (LGPD).

Este projeto foi desenvolvido como parte do currículo da Faculdade ADS (Análise e Desenvolvimento de Sistemas).

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **FastAPI**: Framework web moderno e de alta performance.
- **Pydantic**: Para validação de dados e schemas.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.

## 📋 Funcionalidades

A API permite gerenciar as seguintes entidades:

- **Pacientes**: Cadastro e listagem (com campos preparados para mascaramento/LGPD).
- **Médicos**: Cadastro de profissionais e especialidades.
- **Consultas**: Agendamento de consultas com validação de integridade referencial.
- **Prontuários**: Registro clínico e histórico por paciente.

## 🛠️ Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rodrigo-pas/sghss-vidaplus-backend.git
   cd sghss-vidaplus-backend
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Linux/macOS:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install fastapi uvicorn
   ```

4. **Inicie o servidor:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação interativa:**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📄 Estrutura de Arquivos

- `main.py`: Contém toda a lógica da API, modelos e rotas.
- `README.md`: Documentação do projeto.
- `.gitignore`: Arquivos ignorados pelo Git.

## 👤 Autor

- **Rodrigo P Alcantara**
- RU: 4844626

---
*Projeto desenvolvido para fins acadêmicos.*
