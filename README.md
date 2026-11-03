# Amostras de arquivos Parquet

Este projeto gera arquivos Parquet menores com até os primeiros 500 registros
de cada arquivo de origem. A leitura é feita em lotes para evitar carregar o
arquivo completo na memória. A versão atual é **1.01**.

Este repositório faz parte de um projeto maior:
[LLama_to_chinese](https://github.com/saramendesoliveiralima/LLama_to_chinese).

## Requisitos

- Python 3
- Dependências listadas em `requirements.txt` (PyArrow)

Para instalar as dependências:

```bash
python -m pip install -r requirements.txt
```

Recomenda-se usar um ambiente virtual:

```bash
python -m venv .venv
```

Ative-o antes de instalar as dependências:

```bash
# Linux ou macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

## Arquivos de entrada

Os arquivos de entrada não são incluídos neste repositório. Coloque-os na
pasta `src`, junto de `script.py`:

- `corpus.parquet`
- `corpus_20.parquet`

Os nomes dos arquivos e os respectivos nomes de saída são definidos em
`ARQUIVOS`, no início de `src/script.py`.

## Execução

Na raiz do projeto, execute:

```bash
python src/script.py
```

O programa informa no terminal o nome de cada arquivo gerado e a quantidade
de registros gravados.

## Saída

Os arquivos são criados na pasta `src/output`, que é criada automaticamente
quando necessário:

```text
src/output/
├── amostra_500_corpus.parquet
└── amostra_500_corpus_20.parquet
```

Se um arquivo tiver menos de 500 registros, todos os registros disponíveis
serão incluídos. Se estiver vazio, será gerado um arquivo vazio que preserva
o esquema original. Uma nova execução substitui os arquivos de saída com os
mesmos nomes.

Para alterar a quantidade máxima de registros por amostra, edite `QUANTIDADE`
em `src/script.py`.
