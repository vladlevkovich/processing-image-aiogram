from sqlalchemy.ext.asyncio import AsyncSession
from bot.models.image_models import BaseImage
import uuid
import os


async def upload_image(image, user_id, session: AsyncSession):
    media_path = os.path.join(os.path.dirname(__file__), '../../media')
    user_path = os.path.join(media_path, str(user_id))
    filename = f'{uuid.uuid4()}.jpg'
    save_path = os.path.join(user_path, filename)
    try:
        with open(os.path.join(media_path, filename), 'wb') as f:
            f.write(image)

        base_image = BaseImage(
            image=save_path
        )
        session.add(base_image)
        await session.commit()
        return filename
    except Exception as e:
        raise e

