from aiogram import types
from services import UserService, WalletService
from keyboards import start_keyboard


class CommandHandler:
    def __init__(self, user_service: UserService, wallet_service: WalletService):
        self.user_service = user_service
        self.wallet_service = wallet_service

    async def start_handler(self, message: types.Message):
        print('Информация о пользователе', message.from_user.id, message.from_user.full_name)

        self.user_service.signup(message.from_user.id, message.from_user.full_name, message.from_user.username)

        await message.answer('Привет! Я буду твоим финансовым помощником!', reply_markup=start_keyboard())