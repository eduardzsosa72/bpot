import asyncio
import sys
import logging
import os

# SOLUCIÓN CRÍTICA para Windows - debe estar AL PRINCIPIO
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from pyrogram import Client
from pyrogram.types import CallbackQuery

class PepitoBot():
    def __init__(self):
        self.app = Client(
            "@Macrzz6",
            api_id=32835018,
            api_hash='10dc92dbf18c8abd345d2ee2a0d0f137',
            bot_token='8454388731:AAF8GHffHrsaSB8uAy8WEZLhsHcPptAIDFk',
            plugins=dict(root="plugins")
        )

        # Configurar el manejador de callbacks
        @self.app.on_callback_query()
        def handle_callback(client, call: CallbackQuery):
            data = call.data.split(":")

            if call.from_user.id != int(data[1]):
                return call.answer("Botones bloqueados.")
            else: 
                call.continue_propagation()

    def runn(self):
        os.system("cls")
        logging.basicConfig(level=logging.INFO)
        print("🚀 Iniciando PepitoBot...")
        self.app.run()

if __name__ == "__main__":
    PepitoBot().runn()