# Desafio Técnico – Vaga Programador(a) Júnior

Bem-vindo(a) ao desafio prático para a vaga **Programador(a) Júnior (Python + Firebird 2.5 + n8n + Front‑end)**.

> ⚠️ **IMPORTANTE:** Este desafio foi estruturado para uso com a versão **Firebird 2.5**.  
> O arquivo `employee.fbk` fornecido é um backup gerado nesta versão.  
> Utilize um servidor Firebird 2.5 localmente ou via Docker para restaurá-lo corretamente antes de iniciar.

---

## ✅ Como entregar

1. Faça um **Fork** deste repositório na sua conta GitHub.
2. Crie uma nova branch:  
   `git checkout -b desafio/<seu-nome>`
3. Siga as instruções de cada pasta e faça *commits* claros e objetivos.
4. Ao finalizar, abra um **Pull Request** para a branch `main` **antes do prazo informado**.

---

## Estrutura esperada

```
.
├── backend/
│   ├── README.md            # instruções do desafio back‑end
│   ├── requirements.txt
│   └── main.py              # seu script Python
├── n8n/
│   ├── workflow.json        # export do fluxo
│   ├── docker-compose.yml   # ambiente n8n (opcional)
│   └── prints/              # 3 imagens de execução
├── frontend/
│   ├── app.py               # Fique a vontade e opte pelo framework Python que se sentir confortável
│   ├── index.html           # página estática
│   └── README.md            # instruções front‑end
└── README.md                # este arquivo
└── employee.fbk             # arquivo disponibilizado para a realização do teste
```




---

## 🔧 Desafio Back‑end (Python + Firebird 2.5)

### 🎯 Objetivo
Conectar ao banco Firebird, realizar consultas e gerar relatórios com visualização gráfica.

### 🧩 Tarefas

1. Crie um ambiente virtual:  
   `python -m venv venv && source venv/bin/activate`
2. Instale dependências:  
   `pip install -r backend/requirements.txt`  
   *(exemplos: `fdb`, `pandas`, `matplotlib`)*
3. Implemente o `main.py` com:
   - Conexão ao Firebird:  
     `host=localhost`, `database=employee.fdb`, `user=sysdba`, `password=masterkey`
   - Realize duas consultas SQL:
     - `vendas_por_mes`
     - `total_por_vendedor`
   - Salve os resultados em arquivos `.csv`
   - Gere um gráfico de barras `grafico.png`

4. Documente a execução no `backend/README.md` com até **10 linhas**.

### ✔️ Critérios de Avaliação

| Peso | Item                           |
| ---: | ------------------------------ |
| 40 % | Roda sem erros, gera CSV + PNG |
| 30 % | SQL correta e performática     |
| 20 % | Código limpo (PEP‑8, funções)  |
| 10 % | README objetivo                |

---

## 🔄 Desafio n8n – Automação

### 🎯 Objetivo

Montar um fluxo que receba um CSV via Webhook, insira os dados no Firebird e envie um e‑mail.

### 🧩 Tarefas

1. Suba o ambiente n8n com `docker-compose.yml` (ou use n8n Cloud).
2. Crie o fluxo com os seguintes passos:
   1. **Webhook (POST)** – recebe o arquivo `vendas_mes.csv`
   2. **Function** – transforma CSV em JSON
   3. **Firebird** – insere os dados na tabela `csv_import`
   4. **Email** – envia confirmação para `processo@empresa.com`
3. Exporte o fluxo como `workflow.json`
4. Adicione 3 capturas de tela em `n8n/prints/`:
   - Fluxo completo
   - Execução com sucesso
   - E‑mail recebido

### ✔️ Critérios de Avaliação

| Peso | Item                               |
| ---: | ---------------------------------- |
| 40 % | Fluxo executa sem erro             |
| 30 % | Uso correto dos nós                |
| 20 % | Tratamento de exceções no Function |
| 10 % | Organização dos arquivos           |

---

## 🌐 Desafio Front‑end

### 🎯 Objetivo

Criar uma interface simples para consulta e exportação de vendas por mês.

### 🧩 Requisitos

1. Campo de seleção **Mês/Ano**
2. Botão **Buscar** → exibe resultados em uma tabela
3. Botão **Exportar Excel** → salva como `.xlsx`
4. Use qualquer stack Python que desejar (ex: Flask, Streamlit)
5. Ou opte por uma solução estática com HTML + JavaScript

> A aplicação deve rodar com:  
> `python frontend/app.py`  
> **OU**  
> abrir diretamente o `index.html`

### ✔️ Critérios de Avaliação

| Peso | Item                       |
| ---: | -------------------------- |
| 30 % | Funciona (busca + exporta) |
| 25 % | UX simples e limpa         |
| 20 % | Organização de código      |
| 15 % | Responsividade             |
| 10 % | README claro               |

---

## 📬 Entrega do Pull Request

1. Verifique se cada pasta contém README com instruções claras.
2. Remova quaisquer senhas ou dados sensíveis dos commits.
3. Abra o Pull Request com o título:  
   **`Desafio – <Seu Nome>`**
4. No corpo do PR, inclua:

   - **Tempo gasto em cada etapa**
   - **Principais desafios enfrentados**
   - **O que faria diferente com mais tempo**

---

Boa sorte! 💻🚀
