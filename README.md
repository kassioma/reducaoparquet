# Amostras de arquivos Parquet

Este projeto cria arquivos Parquet menores, contendo até os primeiros 500 registros de cada arquivo de origem. A leitura é feita em lotes, evitando carregar os arquivos completos na memória.

## Arquivos de entrada

Os arquivos Parquet não são incluídos neste repositório. Baixe `corpus.parquet` e `corpus_20.parquet` pelo link disponibilizado no Aprender 3 e coloque-os na mesma pasta que `script.py`:

- `corpus.parquet`
- `corpus_20.parquet`

O script está configurado para processar esses dois arquivos. Se os nomes mudarem, atualize a lista `ARQUIVOS` no início do script.

## Requisitos

- Python 3
- PyArrow

Instale o PyArrow com:

```bash
python3 -m pip install pyarrow
```

Se o Python do sistema não permitir instalação global, crie e use um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pyarrow
```

No Windows, ative o ambiente com:

```powershell
.venv\Scripts\Activate.ps1
```

## Como executar

No terminal, entre na pasta do projeto e execute:

```bash
python3 script.py
```

Se estiver usando o ambiente virtual ativado, também pode executar:

```bash
python script.py
```

O script imprime o nome de cada arquivo gerado e a quantidade de registros gravados.

## Arquivos gerados

As amostras são salvas dentro da pasta `output`, criada automaticamente se ainda não existir:

```text
output/
├── amostra_500_corpus.parquet
└── amostra_500_corpus_20.parquet
```

Se um arquivo de origem tiver menos de 500 registros, a amostra conterá todos os registros disponíveis. Executar o script novamente substitui as amostras com nomes correspondentes.

## Como funciona

1. Localiza os arquivos de origem na mesma pasta que o script.
2. Abre cada Parquet com `pyarrow.parquet.ParquetFile`.
3. Lê apenas o primeiro lote, limitado a 500 registros.
4. Mantém o esquema (colunas e tipos) do arquivo de origem.
5. Cria a pasta `output` se necessário e grava nela a amostra em formato Parquet.

Para alterar a quantidade de registros, modifique `QUANTIDADE` no início de `script.py`.
