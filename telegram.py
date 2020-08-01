import telepot
import time
from operacoes import Operacoes

token = "sua chave do telegram bot aqui"


def receberMsg(msg):
    text = msg['text']
    _id = msg['from']['id']
    nome = msg['from']['first_name']

    # info recebe uma lista que contém os 4 parâmetros necessários para a classe Operacoes
    info = text.split()
    if len(info) == 4 and not text.isdigit():
        op = Operacoes(info[0], info[1], info[2], info[3])

        # verifica a autenticidade do cliente
        if op.validarCliente():

            tele.sendMessage(
                _id, "Pronto! Dados confirmados, escolha a opção desejada abaixo:\n\n1 - Meu pacote de serviços \n2 - Pacotes de serviços disponíveis \n3 - Atualizar pacote de serviços\n4 - Sair")

            # abre o arquivo de sessão criado ao validar o cliente e reatribui os valores das variáveis
            arquivo = open("sessao.txt", "r").read()

            info = arquivo.split()
            op = Operacoes(info[0], info[1], info[2], info[3])

        else:
            tele.sendMessage(
                _id, "Dados incorretos! Tente confirmar seus dados novamente:\n Digite nessa ordem separado por um espaço:\n CPF AGENCIA CONTA SENHA")

    # se info não for um dígito e tiver 4 posições, então é necessário que o cliente confirme os dados
    elif not text.isdigit() and len(info) != 4:
        tele.sendMessage(
            _id, "Olá {}, antes de começarmos, confirme seus dados:\n Digite nessa ordem separado por um espaço:\n CPF AGENCIA CONTA SENHA".format(nome))

    else:
        arquivo = open("sessao.txt", "r").read()
        info = arquivo.split()
        op = Operacoes(info[0], info[1], info[2], info[3])
        
        tele.sendMessage(
                _id, "1 - Meu pacote de serviços \n2 - Pacotes de serviços disponíveis \n3 - Atualizar pacote de serviços\n4 - Sair\n________________________________")

        if int(text) > 100:
            tele.sendMessage(_id, op.atualizarPacoteCliente(int(text)))
        else:
            tele.sendMessage(_id, op.menuOpcoes(text))


tele = telepot.Bot(token)
tele.message_loop(receberMsg)

while True:
    time.sleep(10)
