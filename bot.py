import telebot

CHAVE_API = '7228074426:AAEpmNc8o2n4R5e0GbeXWFOY6LzYCf--XDU'

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['pizza'])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Sua Pizza Sai em 30 Minutos!")

@bot.message_handler(commands=['hamburguer'])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "Seu Hamburguer Sai em 20 Minutos!")

@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.send_message(mensagem.chat.id, "Não Tem Salada, Clique em /iniciar")

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    texto = """
    Qual Seu Pedido? (Clique Em Uma Opção)
    /pizza -> Pizza
    /hamburguer -> Hamburguer
    /salada -> Salada
    Clique Para Iniciar: /iniciar
"""

    bot.reply_to(mensagem, texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.send_message("7104633177", "Faça uma reclamação.")

@bot.message_handler(commands=['opcao3'])
def opcao3(mensagem):
    print(mensagem)
    bot.send_message(mensagem.chat.id, f"Valeu {mensagem.from_user.first_name}, o Doug Mandou Um Oi de Volta")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):

    texto = """
    Olá, aqui é o Bot do Barcelos Bar!
    Escolha uma opção para continuar (Clique no Item):
        /opcao1 -> Fazer Um Pedido
        /opcao2 -> Reclamar de Um Pedido
        /opcao3 -> Mandar um Oi Para o Doug
    Responder Qualquer Outra Coisa Não Vai Funcionar, Clique Em Uma Das Opções
"""

    bot.reply_to(mensagem, texto)

bot.polling()