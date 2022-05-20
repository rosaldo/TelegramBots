#!/usr/bin/env python3
# coding: utf-8

import telegram as tg
from telegram import Update
from telegram.ext import CallbackContext, Filters, MessageHandler, Updater


class MyPhone:
    version = "1.0.0"
    token = ""

    def __init__(self):
        if self.token:
            try:
                up = Updater(self.token, use_context=True)
                dp = up.dispatcher
                dp.add_handler(MessageHandler(Filters.contact, self.send_phone))
                dp.add_handler(MessageHandler(Filters.all, self.get_contact), 0)
                print("\nBot inicializado com sucesso!\n")
                up.start_polling()
            except Exception:
                print("\nToken inválido!\n")
        else:
            print("\nInforme o token do bot!\n")

    def get_contact(self, update: Update, context: CallbackContext):
        contact_keyboard = tg.KeyboardButton(text="Enviar meu contato", request_contact=True)
        reply_markup = tg.ReplyKeyboardMarkup([[contact_keyboard]])
        update.message.reply_text("Por favor, envie seu contato!", reply_markup=reply_markup)

    def send_phone(self, update: Update, context: CallbackContext):
        contact = update.effective_message.contact
        update.effective_chat.send_message(text=f"Seu telefone é: {contact.phone_number}")


myphone = MyPhone()
