                # /***********************************//* Aluno: Kauê Vitor Pereira Santos-RA: N083BC-4//* TURMA:CC2A13//* Profa. Eliane *//***********************************/
class UrnaEletronica:
    # O método __init__ é chamado quando uma nova instância da classe é criada.
    def __init__(self, zona, secao, total_eleitores):
         # Inicialize os atributos da urna eletrônica com os valores fornecidos.
        self.zona = zona
        self.secao = secao
        self.total_eleitores = total_eleitores
        self.cod_urna = f"{zona}-{secao}"
        self.votos_prefeito = {'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'VB': 0, 'VN': 0}
        self.votos_vereador = {'V1': 0, 'V2': 0, 'V3': 0, 'V4': 0, 'VB': 0, 'VN': 0}
# Este método registra o voto para um candidato a prefeito.
    def votar_prefeito(self, candidato):
        if candidato in self.votos_prefeito:
            self.votos_prefeito[candidato] += 1
# Este método registra o voto para um candidato a vereador.
    def votar_vereador(self, candidato):
        if candidato in self.votos_vereador:
            self.votos_vereador[candidato] += 1
# Este método calcula os resultados da votação e retorna um dicionário com os resultados.
    def totalizar(self):
         # Calcule o total de eleitores que votaram somando os votos para prefeito e vereador.
        total_eleitores_votaram = sum(self.votos_prefeito.values()) + sum(self.votos_vereador.values())
        # Calcule o total de eleitores que faltaram votar subtraindo do total esperado.
        total_eleitores_faltaram = self.total_eleitores - total_eleitores_votaram
        # Calcule o total de votos em branco somando os votos brancos para prefeito e vereador.
        total_votos_brancos = self.votos_prefeito['VB'] + self.votos_vereador['VB']
        # Calcule o total de votos nulos somando os votos nulos para prefeito e vereador.
        total_votos_nulos = self.votos_prefeito['VN'] + self.votos_vereador['VN']
        # Encontre o candidato a prefeito mais votado usando a função max.
        candidato_prefeito_mais_votado = max(self.votos_prefeito, key=self.votos_prefeito.get)
        # Encontre o candidato a vereador mais votado usando a função max.
        candidato_vereador_mais_votado = max(self.votos_vereador, key=self.votos_vereador.get)

# Crie um dicionário com os resultados da eleição.
        resultados = {
            "IDENTIFICACAO DA URNA ELETRONICA": {
                "Identificacao da Seção e Zona Eleitoral": f"{self.secao}-{self.zona}",
                "Total dos Eleitores que podem votar": self.total_eleitores,
                "Codigo de Identificacao da Urna Eletronica": self.cod_urna
            },
            "VOTACAO INDIVIDUAL": {},
            "ENCERRAMENTO DAS ELEICOES": {
                "Totalizacao": {
                    "Total de votos para cada candidato": {
                        "C1": self.votos_prefeito['C1'],
                        "C2": self.votos_prefeito['C2'],
                        "C3": self.votos_prefeito['C3'],
                        "C4": self.votos_prefeito['C4'],
                        "VB": self.votos_prefeito['VB'],
                        "VN": self.votos_prefeito['VN']
                    },
                    "Total de eleitores que votaram": total_eleitores_votaram,
                    "Total de eleitores que faltaram": total_eleitores_faltaram,
                    "Total de votos brancos e nulos": {
                        "Brancos": total_votos_brancos,
                        "Nulos": total_votos_nulos
                    }
                },
                "Resultados": {
                    "Candidato a Prefeito mais votado": candidato_prefeito_mais_votado,
                    "Candidato a Vereador mais votado": candidato_vereador_mais_votado
                }
            }
        }
# Preencha o dicionário com os votos individuais de cada eleitor.
        for i, (candidato, votos) in enumerate(self.votos_prefeito.items()):
            resultados["VOTACAO INDIVIDUAL"][f"Eleitor {i + 1}"] = {
                "Voto ao Candidato à Prefeitura": f"{candidato}: {votos}",
                "Voto ao Candidato a Vereador": f"V{votos}"
            }

        for i, (candidato, votos) in enumerate(self.votos_vereador.items()):
            resultados["VOTACAO INDIVIDUAL"][f"Eleitor {i + 1}"].update({
                "Voto ao Candidato à Prefeitura": f"V{votos}",
                "Voto ao Candidato a Vereador": f"{candidato}: {votos}"
            })
 # Retorne o dicionário com os resultados.
        return resultados


if __name__ == "__main__":
    # Solicite informações da urna eletrônica ao usuário.
    zona = int(input("Digite o número da Zona Eleitoral: "))
    secao = int(input("Digite o número da Seção Eleitoral: "))
    total_eleitores = int(input("Digite o total de eleitores esperados: "))

# Crie uma instância da UrnaEletronica com as informações fornecidas.
    urna = UrnaEletronica(zona=zona, secao=secao, total_eleitores=total_eleitores)

# Inicie um loop para permitir que os eleitores votem.
    while True:
        print("\nOpções:")
        print("1. Votar para Prefeito")
        print("2. Votar para Vereador")
        print("3. Encerrar a votação")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            candidato_prefeito = input("Digite o número do candidato a Prefeito: ")
            urna.votar_prefeito(candidato_prefeito)
        elif opcao == "2":
            candidato_vereador = input("Digite o número do candidato a Vereador: ")
            urna.votar_vereador(candidato_vereador)
        elif opcao == "3":
            resultados = urna.totalizar()

            for secao, resultado in resultados.items():
                print(secao)
                for categoria, valores in resultado.items():
                    print(f"{categoria}:")
                    if isinstance(valores, dict):
                        for chave, valor in valores.items():
                            if isinstance(valor, dict):
                                for subchave, subvalor in valor.items():
                                    print(f"{subchave}: {subvalor}")
                            else:
                                print(f"{chave}: {valor}")
            break
        else:
            print("Opção inválida. Tente novamente.")  