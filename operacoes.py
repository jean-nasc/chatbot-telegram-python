import json
import os

class Operacoes:
    def __init__(self, cpf, agencia, conta, senha):
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.senha = senha


    def validarCliente(self):
        with open('dados/clientes.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())

            dataCpf = data[self.cpf]

            if dataCpf:
                if dataCpf["agencia"] == self.agencia and dataCpf["conta"] == self.conta and dataCpf["senha"] == self.senha:
                    with open("sessao.txt", "w") as arquivo:
                        arquivo.write("{} {} {} {}".format(self.cpf, self.agencia, self.conta, self.senha))
                    return dataCpf
                else:
                    return False


    def pacoteCliente(self):
        if self.validarCliente:
            with open('dados/clientes-pacotes-servicos.json', 'r', encoding='utf-8') as f:
                data = json.loads(f.read())

                dataCpf = data[self.cpf]

            return dataCpf["pacote"]


    def pacoteServicosCliente(self):
        if self.pacoteCliente:
            with open('dados/pacotes-servicos.json', 'r', encoding='utf-8') as f:
                data = json.loads(f.read())

                dataPack = data[self.pacoteCliente()]

            return dataPack


    def pacotesServicos(self):
        if self.validarCliente:
            with open('dados/pacotes-servicos.json', 'r', encoding='utf-8') as f:
                data = json.loads(f.read())

            return data

    def logoff(self):
        if self.validarCliente:
            os.remove("./sessao.txt")

    def atualizarPacoteCliente(self, param):
        lista=[]
        for i in self.pacotesServicos():
            lista.append(i)

        if str(param) in lista:

            with open('dados/clientes-pacotes-servicos.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                data[self.cpf]['pacote'] = str(param)

            with open('dados/clientes-pacotes-servicos.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)

        return "Pacote de serviços atualizado com sucesso!"


    def menuOpcoes(self, opcao):
        if opcao == "1":
            lista=""
            for i in self.pacoteServicosCliente():
                lista += "{}: {}\n".format(i.capitalize(), self.pacoteServicosCliente()[i])

            return lista

        elif opcao == "2":
            lista=""
            for i in self.pacotesServicos():
                lista += "{} - {}\n{}\n{}\n\n".format(i, self.pacotesServicos()[i]['titulo'], self.pacotesServicos()[i]['beneficios'], self.pacotesServicos()[i]['valor'])

            return lista

        elif opcao == "3":
            lista=""
            for i in self.pacotesServicos():
                lista += "{} - {}\n{}\n{}\n--------------------------\n".format(i, self.pacotesServicos()[i]['titulo'], self.pacotesServicos()[i]['beneficios'], self.pacotesServicos()[i]['valor'])
            
            return lista

        elif opcao == "4":
            self.logoff()
            return "Sessão finalizada!\nDigite algo para começar novamente!"