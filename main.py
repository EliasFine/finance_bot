import asyncio, os
from aiogram import Bot, Dispatcher, types
from handlers import *
from routers import *
from services import *
from repositories import *
from sqlite3 import connect
from dotenv import load_dotenv


load_dotenv(override=True)


bot = Bot(os.getenv('BOT_TOKEN'))
dp = Dispatcher()


async def start_bot():
    connection = connect("finances.sqlite")
    ur = UserRepository(connection)
    wr = WalletRepository(connection)
    opr = OperationsRepository(connection)
    us = UserService(ur)
    ws = WalletService(wr)
    ops = OperationsService(opr)
    command_handler = CommandHandler(us, ws)
    create_wallet_handler = CreateWalletHandler(ws)
    income_handler = IncomeHandler(ops, ws)
    expense_handler = ExpenseHandler(ops, ws)

    command_router = CommandRouter(dp, command_handler)
    command_router.register_paths()

    wallet_router = WalletRouter(dp, create_wallet_handler)
    wallet_router.register_paths()

    income_router = IncomeRouter(dp,income_handler)
    income_router.register_paths()

    expense_router = ExpenseRouter(dp, expense_handler)
    expense_router.register_paths()

    await dp.start_polling(bot)
    print('Бот запущен')


if __name__ == '__main__':
    asyncio.run(start_bot())