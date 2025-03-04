import asyncio, os
from aiogram import Bot, Dispatcher, types
from handlers import CommandHandler, CreateWalletHandler
from routers import CommandRouter, WalletRouter
from services import UserService, WalletService
from repositories import UserRepository, WalletRepository
from sqlite3 import connect
from dotenv import load_dotenv


load_dotenv(override=True)


bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher()


async def start_bot():
    connection = connect("finances.sqlite")
    ur = UserRepository(connection)
    wr = WalletRepository(connection)
    us = UserService(ur)
    ws = WalletService(wr)
    command_handler = CommandHandler(us, ws)
    create_wallet_handler = CreateWalletHandler(ws)

    command_router = CommandRouter(dp, command_handler)
    command_router.register_paths()

    wallet_router = WalletRouter(dp, create_wallet_handler)
    wallet_router.register_paths()

    await dp.start_polling(bot)
    print('Бот запущен')


if __name__ == '__main__':
    asyncio.run(start_bot())