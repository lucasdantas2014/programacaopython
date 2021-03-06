from model.Pessoa import Pessoa
from datetime import date

import json

def main(args=[]):
    while True:
        try:
                pessoas = []

                # Leitura do Arquivo.
                f = open("pessoas.txt", 'r', encoding="utf8")

                # Parser do JSON em Objeto.
                jsonObjs = json.loads(f.read())

                # Iteração dos elementos do JSON.
                for jsonObj in jsonObjs:
                    nome = jsonObj["nome"]
                    email = jsonObj["email"]
                    data = jsonObj["nascimento"].split("-")
                    nascimento = date(int(data[0]), int(data[1]), int(data[2]))
                    pessoa = Pessoa(nome, email, nascimento)
                    print(pessoa)
                    pessoas.append(pessoa)

                pedro = Pessoa("Pedro", "01/03/2017")
                pessoas.append(pedro)

                pedroJson = {}
                pedroJson['nome'] = pedro.nome
                pedroJson['nascimento'] = pedro.nascimento
                jsonObjs.append(pedroJson)

                with open('data.txt', 'w', encoding='utf-8') as f:
                    json.dump(jsonObjs, f, ensure_ascii=False, indent=4)
                    f.close()

                break
        except FileNotFoundError:
            print("Arquivo não encontrado!")

if __name__ == '__main__':
    main()

