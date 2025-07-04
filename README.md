# Web Scraping com Python 🐍

Este projeto demonstra como realizar web scraping em um site dinâmico utilizando Python. O script `scraping.py` foi desenvolvido para extrair informações sobre passagens de ônibus do site [ClickBus](https://www.clickbus.com.br), automatizando a navegação, preenchimento de formulário e coleta de dados.

## ✨ Funcionalidades

O script realiza as seguintes ações:

-   🚀 Inicia um navegador Chrome em modo headless (sem interface gráfica).
-   🍪 Aceita o banner de cookies para prosseguir com a navegação.
-   🚌 Preenche automaticamente os campos de **origem** (São Paulo, SP) e **destino** (Rio de Janeiro, RJ).
-   📅 Seleciona a primeira data disponível no calendário.
-   🔍 Clica no botão de busca e aguarda o carregamento dos resultados.
-   📊 Extrai os seguintes dados de cada passagem encontrada:
    -   Empresa
    -   Horário de Partida
    -   Horário de Chegada
    -   Preço
-   💾 Salva todas as informações coletadas em um arquivo CSV chamado `passagens_sp_rj.csv`.

## 🛠️ Tecnologias Utilizadas

-   **[Python](https://www.python.org/)**: A linguagem de programação base do projeto.
-   **[Selenium](https://www.selenium.dev/)**: Para automação do navegador e interação com elementos dinâmicos da página.
-   **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)**: Para fazer o parsing do HTML e facilitar a extração dos dados.
-   **[Pandas](https://pandas.pydata.org/)**: Para estruturar os dados coletados em um DataFrame e exportar para CSV.
-   **[tqdm](https://github.com/tqdm/tqdm)**: Para exibir uma barra de progresso durante a extração.

## 🚀 Começando

Siga estas instruções para ter uma cópia do projeto rodando na sua máquina.

### Pré-requisitos

-   Python 3.10+
-   Pip
-   Google Chrome (ou outro navegador compatível com Selenium)
-   ChromeDriver correspondente à sua versão do Google Chrome.

### Instalação

1.  **Clone o repositório:**
    ```sh
    git clone https://github.com/jusansilva/web-scraping-python.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```sh
    cd web-scraping-python
    ```

3.  **Crie e ative um ambiente virtual:**
    ```sh
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

4.  **Instale as dependências a partir do `requirements.txt`:**
    ```sh
    pip install -r requirements.txt
    ```
    *(Se o arquivo `requirements.txt` não existir, você pode criá-lo com `pip freeze > requirements.txt` após instalar as bibliotecas manualmente: `pip install selenium beautifulsoup4 pandas tqdm`)*

5.  **ChromeDriver**: Certifique-se de que o `chromedriver` esteja no `PATH` do seu sistema ou especifique o caminho para ele no script.

## ⚙️ Uso

Para executar o script de scraping, simplesmente rode o seguinte comando no seu terminal:

```sh
python scraping.py
```

O script exibirá o progresso no terminal e, ao final, criará o arquivo `passagens_sp_rj.csv` no mesmo diretório.

## 👨‍💻 Colaborador

<a href="https://github.com/jusansilva">
 <img style="border-radius: 50%;" src="https://github.com/jusansilva.png" width="100px;" alt="Foto de Jusan Magno"/>
 <br />
 <sub><b>Jusan Magno</b></sub>
</a>
<br />

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jusanmagno/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jusansilva)