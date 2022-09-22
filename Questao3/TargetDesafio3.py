from statistics import median
import numpy as np
import json

if __name__ == "__main__":
    with open("dados.json") as f:
        dados = json.load(f)

        faturamento = np.array([], dtype="float")
        for ponto in dados:
            valor = ponto["valor"]
            if valor != 0:
                faturamento = np.append(faturamento, valor)

        media = np.mean(faturamento)

        print("Menor faturamento: R$", np.min(faturamento))
        print("Maior faturamento: R$", np.max(faturamento))
        print("Dias com faturamento superior à média:", len(faturamento[faturamento > media]))
