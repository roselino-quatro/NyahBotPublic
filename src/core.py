from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from conf.settings import TELEGRAM_TOKEN
from data import quarentena_photos
from libgen_api import LibgenSearch
import random
import chat

def start(update, context):
    response_message = "miau miau miau caralho"
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def fofometro(update, context, registered_chats):
    user = update.message.from_user
    current_username = user['username']
    current_chat = update.message.chat_id

    chat.registerChat(registered_chats, current_chat) 
    registered_chats[current_chat].registerUser(user)
    
    response_messages = registered_chats[current_chat].registered_users[current_username].getCutenessLevel()

    for message in response_messages:
        context.bot.sendMessage(
            chat_id=update.message.chat_id,
            text=message
        )

def parabens(update, context):
    response_message = "༼ つ ◕_◕ ༽つ KANEEE TAKE MY PARABAINS ༼ つ ◕_◕ ༽つ"
    
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )



def paises(update, context):
    paises = ["Afeganistão", "África do Sul", "Akrotiri", "Albânia", "Alemanha", "Andorra", "Angola", "Anguila", "Antárctida", "Antígua e Barbuda", "Arábia Saudita", "Arctic Ocean", "Argélia", "Argentina", "Arménia", "Aruba", "Ashmore and Cartier Islands", "Atlantic Ocean", "Austrália", "Áustria", "Azerbaijão", "Baamas", "Bangladeche", "Barbados", "Barém", "Bélgica", "Belize", "Benim", "Bermudas", "Bielorrússia", "Birmânia", "Bolívia", "Bósnia e Herzegovina", "Botsuana", "Brasil", "Brunei", "Bulgária", "Burquina Faso", "Burúndi", "Butão", "Cabo Verde", "Camarões", "Camboja", "Canadá", "Catar", "Cazaquistão", "Chade", "Chile", "China", "Chipre", "Clipperton Island", "Colômbia", "Comores", "Congo-Brazzaville", "Congo-Kinshasa", "Coral Sea Islands", "Coreia do Norte", "Coreia do Sul", "Costa do Marfim", "Costa Rica", "Croácia", "Cuba", "Curacao", "Dhekelia", "Dinamarca", "Domínica", "Egipto", "Emiratos Árabes Unidos", "Equador", "Eritreia", "Eslováquia", "Eslovénia", "Espanha", "Estados Unidos", "Estónia", "Etiópia", "Faroé", "Fiji", "Filipinas", "Finlândia", "França", "Gabão", "Gâmbia", "Gana", "Gaza Strip", "Geórgia", "Geórgia do Sul e Sandwich do Sul", "Gibraltar", "Granada", "Grécia", "Gronelândia", "Guame", "Guatemala", "Guernsey", "Guiana", "Guiné", "Guiné Equatorial", "Guiné-Bissau", "Haiti", "Honduras", "Hong Kong", "Hungria", "Iémen", "Ilha Bouvet", "Ilha do Natal", "Ilha Norfolk", "Ilhas Caimão", "Ilhas Cook", "Ilhas dos Cocos", "Ilhas Falkland", "Ilhas Heard e McDonald", "Ilhas Marshall", "Ilhas Salomão", "Ilhas Turcas e Caicos", "Ilhas Virgens Americanas", "Ilhas Virgens Britânicas", "Índia", "Indian Ocean", "Indonésia", "Irão", "Iraque", "Irlanda", "Islândia", "Israel", "Itália", "Jamaica", "Jan Mayen", "Japão", "Jersey", "Jibuti", "Jordânia", "Kosovo", "Kuwait", "Laos", "Lesoto", "Letónia", "Líbano", "Libéria", "Líbia", "Listenstaine", "Lituânia", "Luxemburgo", "Macau", "Macedónia", "Madagáscar", "Malásia", "Malávi", "Maldivas", "Mali", "Malta", "Man, Isle of", "Marianas do Norte", "Marrocos", "Maurícia", "Mauritânia", "México", "Micronésia", "Moçambique", "Moldávia", "Mónaco", "Mongólia", "Monserrate", "Montenegro", "Mundo", "Namíbia", "Nauru", "Navassa Island", "Nepal", "Nicarágua", "Níger", "Nigéria", "Niue", "Noruega", "Nova Caledónia", "Nova Zelândia", "Omã", "Pacific Ocean", "Países Baixos", "Palau", "Panamá", "Papua-Nova Guiné", "Paquistão", "Paracel Islands", "Paraguai", "Peru", "Pitcairn", "Polinésia Francesa", "Polónia", "Porto Rico", "Portugal", "Quénia", "Quirguizistão", "Quiribáti", "Reino Unido", "República Centro-Africana", "República Dominicana", "Roménia", "Ruanda", "Rússia", "Salvador", "Samoa", "Samoa Americana", "Santa Helena", "Santa Lúcia", "São Bartolomeu", "São Cristóvão e Neves", "São Marinho", "São Martinho", "São Pedro e Miquelon", "São Tomé e Príncipe", "São Vicente e Granadinas", "Sara Ocidental", "Seichees", "Senegal", "Serra Leoa", "Sérvia", "Singapura", "Sint Maarten", "Síria", "Somália", "Southern Ocean", "Spratly Islands", "Sri Lanca", "Suazilândia", "Sudão", "Sudão do Sul", "Suécia", "Suíça", "Suriname", "Svalbard e Jan Mayen", "Tailândia", "Taiwan", "Tajiquistão", "Tanzânia", "Território Britânico do Oceano Índico", "Territórios Austrais Franceses", "Timor Leste", "Togo", "Tokelau", "Tonga", "Trindade e Tobago", "Tunísia", "Turquemenistão", "Turquia", "Tuvalu", "Ucrânia", "Uganda", "União Europeia", "Uruguai", "Usbequistão", "Vanuatu", "Vaticano", "Venezuela", "Vietname", "Wake Island", "Wallis e Futuna", "West Bank", "Zâmbia", "Zimbabué"]

    random_index = random.randint(0,len(paises) - 2)
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text=paises[random_index]
    )


# O que esse faz?
def testFoward(update, context):
    current_chat = update.message.chat_id
    channel_id = '-1001281808802'
    messages = update.message.getMessages(id=channel_id)
    print(messages)

def carentena(update, context, registered_chats):
    current_chat = update.message.chat_id
    chat.registerChat(registered_chats, current_chat) 
  
    random_photo = registered_chats[current_chat].chooseRandomPhoto(list(quarentena_photos.keys()))
    url = quarentena_photos[random_photo]['url']
    caption = quarentena_photos[random_photo]['cap']

    context.bot.sendPhoto (
        chat_id=update.message.chat_id,
        photo=url,
        caption=caption,
        parse_mode='html'
    )

# Utiliza a biblioteca libgen-api para buscar livros por titulo
def libgen(update, context):
    title = ' '.join(context.args)
    search = LibgenSearch()
    results = search.search_title(title)
    len_results = len(results)
    if len_results != 0:
        response_message = "Sua busca retornou " + str(len_results) + " resultados. Os valores do primeiro resultado são"
        response_message = response_message + "\nID: " + results[0]['ID']
        response_message = response_message + "\nAutor: " + results[0]['Author']
        response_message = response_message + "\nTitulo: " + results[0]['Title']
        response_message = response_message + "\nEditora: " + results[0]['Publisher']
        response_message = response_message + "\nAno: " + results[0]['Year']
        response_message = response_message + "\nPaginas: " + results[0]['Pages']
        response_message = response_message + "\nLingua: " + results[0]['Language']
        response_message = response_message + "\nTamanho: " + results[0]['Size']
        response_message = response_message + "\nExtensão: " + results[0]['Extension']
        response_message = response_message + "\nPrimeiro Mirror: " + results[0]['Mirror_1']
        response_message = response_message + "\n＼(≧▽≦)／"
    else:
        response_message = "Livro não encontrado =<"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)

def main(): 
    registered_chats = {}

    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )

    dispatcher.add_handler(
        CommandHandler('carentena', lambda bot, update: carentena(bot, update, registered_chats))
    )

    dispatcher.add_handler(
        CommandHandler('fofometro', lambda bot, update: fofometro(bot, update, registered_chats))
    )
    
    dispatcher.add_handler(
        CommandHandler('parabains', parabens)
    )
    
    dispatcher.add_handler(
        CommandHandler('paises', paises)
    )

    dispatcher.add_handler(
        CommandHandler('libgen', libgen)
    )

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
