# Importa Path para montar caminhos de arquivos de forma compatível com o sistema operacional.
from pathlib import Path

# Importa PyArrow para manipular tabelas e arquivos Parquet.
import pyarrow as pa
import pyarrow.parquet as pq


# Define a pasta onde este script e os arquivos Parquet de origem estão localizados.
PASTA = Path(__file__).resolve().parent
# Limita cada amostra aos primeiros 500 registros do arquivo de origem.
QUANTIDADE = 500
# Relaciona cada arquivo de origem ao nome do respectivo arquivo de amostra.
ARQUIVOS = (
    ("corpus.parquet", "amostra_500_corpus.parquet"),
    ("corpus_20.parquet", "amostra_500_corpus_20.parquet"),
)


# Cria uma amostra de um arquivo Parquet e retorna a quantidade de registros gravados.
def criar_amostra(arquivo_origem: Path, arquivo_destino: Path) -> int:
    # Abre o arquivo sem carregar todo o seu conteúdo na memória.
    parquet = pq.ParquetFile(arquivo_origem)
    # Lê apenas um lote, com no máximo a quantidade de registros solicitada.
    primeira_lote = next(
        parquet.iter_batches(batch_size=QUANTIDADE),
        None,
    )
    # Converte o lote em tabela e mantém o esquema original, inclusive se estiver vazio.
    tabela = (
        pa.Table.from_batches([primeira_lote], schema=parquet.schema_arrow)
        if primeira_lote is not None
        else pa.Table.from_batches([], schema=parquet.schema_arrow)
    )
    # Grava a tabela de amostra no caminho de destino informado.
    pq.write_table(tabela, arquivo_destino)
    # Informa quantos registros foram efetivamente gravados.
    return tabela.num_rows


# Processa os arquivos configurados e salva as amostras na pasta output.
def main() -> None:
    # Define a pasta de saída e a cria caso ainda não exista.
    pasta_saida = PASTA / "output"
    pasta_saida.mkdir(parents=True, exist_ok=True)

    # Cria uma amostra para cada par de arquivo de origem e destino.
    for origem, destino in ARQUIVOS:
        # Monta o caminho de origem junto à pasta do script.
        caminho_origem = PASTA / origem
        # Monta o caminho de destino dentro da pasta output.
        caminho_destino = pasta_saida / destino
        # Lê e grava a amostra e guarda a quantidade de registros gerados.
        quantidade = criar_amostra(caminho_origem, caminho_destino)
        # Exibe o nome do arquivo de saída e a quantidade de registros gravados.
        print(f"{caminho_destino.name}: {quantidade} registros")


# Executa o processamento apenas quando este arquivo é chamado diretamente.
if __name__ == "__main__":
    main()
