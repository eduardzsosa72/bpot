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
            "GOKUPELON",
            api_id=24648014,
            api_hash='3575a0f1524c2a08cc297fbd5355e318',
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