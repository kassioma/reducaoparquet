# Changelog

## [1.0.1] - 2026-11-03

- Organiza os arquivos e a documentação do projeto.
- Documenta a relação deste repositório com
  [LLama_to_chinese](https://github.com/saramendesoliveiralima/LLama_to_chinese).

## [1.0.0] - 2026-11-03

- Cria amostras com até 500 registros dos arquivos `corpus.parquet` e
  `corpus_20.parquet`.
- Lê os arquivos em lotes e preserva o esquema original, inclusive para
  arquivos vazios.
- Grava os arquivos de saída na pasta `src/output`.
