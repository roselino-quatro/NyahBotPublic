import random
from datetime import datetime as dt
from random import choice
from telegram import User

class RegisteredUser(User):
    ''' subClasse de User onde as instância faram parte dos usuários cadastrados em cada chat '''
    def __init__(self, user_id, first_name, is_bot, username):
        super(RegisteredUser, self).__init__(user_id, first_name, is_bot, username=username)
        self.cuteness_level = 0
        self.cuteness_error_counter = 0

    def getCutenessLevel(self):
        response_messages = []

        if self.username.lower() == "shodeyou":
            print(self.username + ": " + str(self.id))
            response_messages.append("Hoje " + self.username.title() + " possui 0% de fofura, mas aquele 100% de Melloboy")
            response_messages.append("Uau que surpresa")
            return response_messages

        if self.cuteness_level == 0:
            non_error_chance = 20.0*((1.0 + 0.5)**self.cuteness_error_counter)
            starting_point = 100 - int((2000.0/non_error_chance))
            self.cuteness_level = random.randint(starting_point, 99)

        response_messages.append("Hoje " + self.username.title() + " possui " + str(self.cuteness_level) + "% de fofura, mas aquele "  + str(100 - self.cuteness_level) + "% de Melloboy")

        if self.cuteness_level < 80:
            if self.cuteness_error_counter > 0:
                scream = "aa" * self.cuteness_error_counter
                response_messages.append(scream + " nono isso tá errado dn, real me quebrou com o seu nível de fofura????\nBom, quem sabe não vai na " + str(self.cuteness_error_counter + 2) + "º vez?")
            else:
                response_messages.append("Nono isso tá errado, você deve ter me quebrado com o seu real nível de fofura\nDesculpa o vacilo, por que vc não tenta de novo?")
            
            self.cuteness_error_counter += 1
            self.cuteness_level = 0

        return response_messages

class RegisteredChat():
    ''' Cada instância relativa a essa classe será um chat diferente, para que não haja interferência entre esses '''
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.registration_starting_time = dt.now().timestamp()
        self.message_starting_time = dt.now().timestamp()
        self.uploaded_photos = []
        self.registered_users = {}

    def evaluateRegistrationRestart(self, cool_down):
        current_time = dt.now().timestamp()

        if current_time > self.registration_starting_time + cool_down:
            self.registered_users = {}
            self.registrations_starting_time = current_time 

    def registerUser(self, new_user):
        self.evaluateRegistrationRestart(24*60*60)

        if new_user['username'] not in self.registered_users.keys():
            self.registered_users[new_user['username']] = RegisteredUser(new_user['id'], new_user['first_name'], new_user['is_bot'], new_user['username'])

    def evaluateMessageRestart(self, cool_down):
        current_time = dt.now().timestamp()

        if current_time > self.message_starting_time + cool_down:
            self.uploaded_photos = []
            self.message_starting_time = current_time 

    def chooseRandomPhoto(self, all_photos):
        self.evaluateMessageRestart(10*60)

        photoIsRepetead = True
        while photoIsRepetead:
            random_photo = choice(all_photos)

            if random_photo not in self.uploaded_photos:
                self.uploaded_photos.append(random_photo)
                photoIsRepetead = False

            elif sorted(all_photos) == sorted(self.uploaded_photos):
                photoIsRepetead = False
        
        return random_photo

def registerChat(registered_chats, new_chat_id):
    if new_chat_id not in registered_chats:
        registered_chats[new_chat_id] = RegisteredChat(new_chat_id)

