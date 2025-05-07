# Desafio Técnico – Vaga Programador(a) Júnior

Bem-vindo(a) ao desafio prático para a vaga **Programador(a) Júnior (Python + Firebird + n8n + Front‑end)**.

> **Como entregar**
>
> 1. **Fork** deste repositório na sua conta GitHub.
> 2. Crie uma branch **`desafio/<seu-nome>`**.
> 3. Siga as instruções de cada pasta e faça *commits* objetivos.
> 4. Abra um **Pull Request** para a branch `main` **antes do prazo informado**.

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

## Desafio Back‑end (Python + Firebird)

### Objetivo

Conectar ao Firebird, extrair dados e gerar relatório.

### Passos

1. Crie um ambiente virtual:
   `python -m venv venv && source venv/bin/activate`
2. Instale dependências:
   `pip install -r backend/requirements.txt`
   *(ex.: `fdb`, `pandas`, `matplotlib`)*
3. Implemente **main.py**:

   * Conexão: host `localhost`, db `employee.fdb`, usuário `sysdba`, senha `masterkey`.
   * Duas consultas:
     `vendas_por_mes` e `total_por_vendedor` (tabelas já presentes).
   * Salve resultados em CSV e gere `grafico.png` (barras).
4. Preencha **backend/README.md** com até 10 linhas (setup e execução).

### Avaliação

| Peso | Item                           |
| ---: | ------------------------------ |
| 40 % | Roda sem erros, gera CSV + PNG |
| 30 % | SQL correta e performática     |
| 20 % | Código limpo (PEP‑8, funções)  |
| 10 % | README objetivo                |

---

## 3. Desafio n8n

### Objetivo

Criar automação Webhook → Firebird → E‑mail.

### Tarefas

1. Suba o container n8n (use `docker-compose.yml`).
2. Montar workflow:

   1. **Webhook (POST)** – recebe `vendas_mes.csv`.
   2. **Function** – parse CSV → JSON.
   3. **Firebird** – insere em tabela `csv_import`.
   4. **E‑mail** – confirma para `processo@empresa.com`.
3. Teste o fluxo e exporte `workflow.json`.
4. Adicione 3 prints em `n8n/prints/`:

   * Fluxo completo
   * Execução OK
   * E‑mail recebido

### Avaliação

| Peso | Item                               |
| ---: | ---------------------------------- |
| 40 % | Fluxo executa sem erro             |
| 30 % | Uso correto dos nós                |
| 20 % | Tratamento de exceções no Function |
| 10 % | Organização dos arquivos           |

---

## 4. Desafio Front‑end

### Objetivo

Interface simples para consultar e exportar vendas.

### Requisitos

1. Campo **Mês/Ano**.
2. Botão **Buscar**: exibir tabela responsiva.
3. Botão **Exportar Excel** (.xlsx).
4. Stack livre (Flask ou framework que preferir +Bootstrap **ou** HTML+JS fetch).
5. Executar com `python frontend/app.py` **ou** abrir `index.html`.

### Avaliação

| Peso | Item                       |
| ---: | -------------------------- |
| 30 % | Funciona (busca + exporta) |
| 25 % | UX simples e limpa         |
| 20 % | Organização de código      |
| 15 % | Responsividade             |
| 10 % | README claro               |

---

## 5. Entrega do Pull Request

1. Revise se cada pasta contém README e que o passo de execução funciona.
2. Remova senhas ou dados sensíveis dos commits.
3. Abra o PR intitulado **`Desafio – <Seu Nome>`** antes do deadline.
4. Informe no corpo:

   * Tempo gasto em cada etapa.
   * Desafios encontrados.
   * O que faria diferente com mais tempo.

