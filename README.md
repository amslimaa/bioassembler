# 🧬 Assembler

Programa em Python que **remonta uma sequência genética** a partir de um arquivo texto com os (k,d)-mers em ordem lexicográfica e grava o resultado em um arquivo **FASTA**. Exercício da disciplina de **Bioinformática** (UFPI).

- **Entrada:** arquivo texto com os kdmers — a saída do [`kdmer`](https://github.com/amslimaa/kdmer)
- **Saída:** arquivo FASTA com a sequência remontada

## Como usar

Requer Python 3.

```bash
pipenv install            # ou use o Python do sistema
python assembler.py
```

Arquivos de apoio: [`input.fasta`](input.fasta) (exemplo) e [`getdata.py`](getdata.py) (leitura da entrada).

## Autor

Feito por [Amós Magalhães](https://github.com/amslimaa).
