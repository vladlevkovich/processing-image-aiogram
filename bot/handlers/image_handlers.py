from aiogram.types import Message, CallbackQuery, FSInputFile, ContentType, InputFile
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router, F
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from services.users_services import check_user
from keyboards.image_keyboard import image_kb
from fsm.image_fsm import UploadImage
from services.images.images_processing import hot_image, grayscale_image, image_noise, resize_image
import uuid
import time


router = Router()


@router.message(Command('processing'))
async def processing(message: Message, session: AsyncSession):
    user = await check_user(user_id=message.from_user.id, session=session)
    if user:
        return await message.answer('Image processing choose', reply_markup=image_kb)
    await message.answer('jdjdjjd', reply_markup=image_kb)
    # await message.error_message('User not found')


@router.callback_query(F.data == 'hot_image')
async def hot_image_processing(callback: CallbackQuery, state: FSMContext):
    print(F.data)
    await callback.answer('')
    await state.set_state(UploadImage.image)
    await state.update_data(processing_type='hot')
    await callback.message.edit_text('Upload image')


@router.callback_query(F.data == 'black_white')
async def black_white_image_processing(callback: CallbackQuery, state: FSMContext):
    # print(callback.data)
    await callback.answer('')
    await state.set_state(UploadImage.image)
    await state.update_data(processing_type='black')
    await callback.message.edit_text('Upload image')


@router.callback_query(F.data == 'noise_image')
async def noised_image_processing(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(UploadImage.image)
    await state.update_data(processing_type='noise')
    await callback.message.edit_text('Upload image')


@router.callback_query(F.data == 'resize_image')
async def resize_image_processing(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(UploadImage.image)
    await state.update_data(processing_type='resize')
    await callback.message.edit_text('Upload image')


@router.message(UploadImage.image, F.photo)
async def image_processing_handler(message: Message, state: FSMContext):
    try:
        media_dir = Path(__file__).parent.parent / 'media'
        user_path = media_dir / str(message.from_user.id)
        user_path.mkdir(parents=True, exist_ok=True)
        file_path = user_path / f'{message.from_user.id}-{uuid.uuid4()}.jpg'
        await message.bot.download(file=message.photo[-1].file_id, destination=file_path)
        data = await state.get_data()
        # processed_file_path = hot_image(user_id=message.from_user.id, image_path=file_path)
        print(data['processing_type'])
        if data['processing_type'] == 'hot':
            time.sleep(5)
            processed_file_path = hot_image(user_id=message.from_user.id, image_path=file_path)
            await message.reply_document(document=FSInputFile(path=processed_file_path))
        elif data['processing_type'] == 'black':
            time.sleep(5)
            processed_file_path = grayscale_image(user_id=message.from_user.id, image_path=file_path)
            await message.reply_document(document=FSInputFile(path=processed_file_path))
        elif data['processing_type'] == 'noise':
            time.sleep(5)
            processed_file_path = image_noise(user_id=message.from_user.id, image_path=file_path)
            await message.reply_document(document=FSInputFile(path=processed_file_path))
        elif data['processing_type'] == 'resize':
            time.sleep(5)
            processed_file_path = resize_image(user_id=message.from_user.id, image_path=file_path)
            await message.reply_document(document=FSInputFile(path=processed_file_path))
        # time.sleep(5)
        # await message.reply_document(document=FSInputFile(path=processed_file_path))
        await state.clear()
    except ValueError:
        await message.answer('Failed to upload image. Please try again with a valid photo.')
