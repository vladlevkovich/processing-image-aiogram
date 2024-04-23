from aiogram.fsm.state import State, StatesGroup


class UploadImage(StatesGroup):
    image = State()
    processing_type = State()
