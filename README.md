-----

# Dashboard de Monitoramento (SOCF)

## Informações Institucionais

  - **Disciplina:** Sistemas Operacionais Ciberfísicos
  - **Instituição:** Pontifícia Universidade Católica do Paraná
  - **Professor:** Pedro Horchulhack
  - **Turma:** 4U
  - **Equipe:** 12

### Membros da equipe

| Nome Completo | Usuário GitHub |
| :--- | :--- |
| `Mateus Roese Tucunduva`| `@Matizuuu` |
| `Matheus Yamamoto Dias` | `@MatheusYamas` |
| `Victor Ryuki Tamezava` | `@VicRuk` |

-----

## 1\. Objetivo do Projeto

Este projeto consiste no desenvolvimento de um dashboard web simples usando **Python** e o micro-framework **Flask**. O objetivo é expor informações do sistema e do processo da aplicação através de uma API RESTful.

A aplicação serve uma interface HTML (`index.html`) que consome dois endpoints:

1.  `/info`: Retorna informações estáticas sobre os integrantes do grupo.
2.  `/metricas`: Utiliza a biblioteca `psutil` para capturar e retornar métricas em tempo real sobre o processo da aplicação (PID, uso de memória, uso de CPU) e o sistema operacional.

-----

## 2\. Funcionalidades

O sistema foi implementado com as seguintes funcionalidades:

  - **Servidor Web:** Um servidor Flask que gerencia requisições HTTP.
  - **Interface de Usuário:** Uma página HTML simples com botões para interagir com a API.
  - **API de Informações (`/info`):** Endpoint que retorna um JSON com os nomes dos membros da equipe.
  - **API de Métricas (`/metricas`):** Endpoint que utiliza `psutil` e `platform` para coletar e retornar dados dinâmicos sobre o processo atual e o SO.
  - **Requisições Assíncronas:** O frontend usa `fetch` (JavaScript) para consumir os endpoints da API sem recarregar a página.

-----

## 3\. Estrutura do Repositório

O projeto está organizado da seguinte forma para facilitar a execução com Flask:

```bash
.
├── main.py             # Servidor Flask com os endpoints da API
├── templates/
│   └── index.html      # Interface do dashboard (HTML, CSS, JS)
├── requirements.txt    # Dependências do projeto
└── README.md           # Descrição completa do projeto
```

-----

## 4\. Como Executar

Para executar o sistema localmente é necessário ter Python 3 instalado.

### 4.1. Arquivo de Dependências (requirements.txt)

Crie um arquivo `requirements.txt` na raiz do projeto com o seguinte conteúdo:

```
Flask
psutil
```

### 4.2. Passos para Execução

1.  **Clone o Repositório**

    ```bash
    # (Exemplo: git clone ...)
    ```

2.  **Crie e Ative um Ambiente Virtual**

    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as Dependências**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Servidor Flask**

    ```bash
    python main.py
    ```

5.  **Acesse o Dashboard**
    Abra seu navegador e acesse: [http://localhost:8080](https://www.google.com/search?q=http://localhost:8080)

-----

## 5\. Endpoints da API

O sistema expõe os seguintes endpoints:

| Rota | Método | Descrição | Exemplo de Retorno (JSON) |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | Renderiza a página principal do dashboard (`index.html`). | (Renderiza HTML) |
| `/info` | `GET` | Retorna a lista de integrantes do grupo. | `{"integrantes": ["Nome 1", "Nome 2", ... ]}` |
| `/metricas` | `GET` | Retorna métricas do processo e do sistema. | `{"Memória usada": 15.2, "PID": 12345, ...}` |

-----

## 6\. Exemplo de Uso

Ao acessar [http://localhost:8080](https://www.google.com/search?q=http://localhost:8080) no navegador, a seguinte interface será exibida:

### 6.1. Carregando Informações da Equipe

1.  O usuário clica no botão **"Carregar /info"**.
2.  O JavaScript faz uma requisição `fetch` para o endpoint `/info`.
3.  O servidor Flask responde com o JSON dos integrantes.
4.  O resultado é exibido na tela:

<!-- end list -->

```json
{
  "integrantes": [
    "Mateus Roese Tucunduva",
    "Matheus Yamamoto Dias",
    "Victor Ryuki Tamezava"
  ]
}
```

### 6.2. Carregando Métricas do Sistema

1.  O usuário clica no botão **"Carregar /metricas"**.
2.  O JavaScript faz uma requisição `fetch` para o endpoint `/metricas`.
3.  O servidor Flask usa `psutil` para coletar os dados e responde com o JSON.
4.  O resultado (que varia a cada execução) é exibido na tela:

<!-- end list -->

```json
{
  "Memória usada": 21.45,
  "PID": 54321,
  "Sistema Operacional": "Windows (10.0.19045)",
  "Uso da CPU": 0.5
}
```

-----

## 7. Telas da Aplicação (Printscreens)

Seguem os prints solicitados para o relatório, incluindo a interface, as saídas JSON e a configuração do deploy no Render.

![Tela principal do dashboard](https://ibb.co/qLhvF95P)
![Saída JSON da rota /info](https://ibb.co/BHXvpLhX)
![Saída JSON da rota /metricas](https://ibb.co/MxctPcjW)
![Configuração do Render - Parte 1](https://ibb.co/bgJjFkyC)
![Configuração do Render - Parte 2](https://ibb.co/9kLy5WRF)
![Deploy em andamento no Render](https://ibb.co/39L5wpPb)
