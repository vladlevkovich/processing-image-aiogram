from PIL import Image
from pathlib import Path
import numpy as np
import uuid
import cv2


def open_image(image_path):
    img = np.array(Image.open(image_path))
    return img


def save_image(user_id):
    media_dir = Path(__file__).parent.parent / 'media'
    full_path = media_dir / str(user_id) / 'processed'
    full_path.mkdir(parents=True, exist_ok=True)
    file_path = full_path / f'processed-{user_id}-{uuid.uuid4()}.jpg'
    return file_path


def grayscale_image(image_path, user_id):
    # img = np.array(Image.open(image_path))
    img = open_image(image_path)
    height, width, channel = img.shape
    gray_image = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            # c_srgb = None
            r = img[i, j, 0]  # red channel
            g = img[i, j, 1]  # green channel
            b = img[i, j, 2]  # blue channel

            gamma = 1.04
            r_normalized = r / 255
            g_normalized = g / 255
            b_normalized = b / 255

            gray_value = (0.2126 * r_normalized ** gamma
                          + 0.7152 * g_normalized ** gamma + 0.0722 * b_normalized ** gamma)

            gray_image[i, j] = gray_value

    file_path = save_image(user_id=user_id)
    new_gray_image = Image.fromarray(gray_image, mode='L')
    new_gray_image.save(file_path)
    return file_path


def hot_image(user_id, image_path):
    img = open_image(image_path)
    red_coef = 1.2
    blue_coef = 0.8

    warmed_image = img.copy().astype(np.float32)
    warmed_image[:, :, 0] *= red_coef
    warmed_image[:, :, 2] *= blue_coef
    warmed_image = np.clip(warmed_image, 0, 255)
    warmed_image = warmed_image.astype(np.uint8)
    file_path = save_image(user_id=user_id)
    new_image = Image.fromarray(warmed_image)
    new_image.save(file_path)
    return file_path


def image_noise(image_path, user_id):
    img = open_image(image_path)
    img_gray = img[:, :, 1]
    noise = np.random.normal(0, 50, img_gray.shape)
    img_noised = img_gray + noise
    img_noised = np.clip(img_noised, 0, 255).astype(np.uint8)
    file_path = save_image(user_id=user_id)
    new_image = Image.fromarray(img_noised)
    new_image.save(file_path)
    return file_path


def resize_image(user_id, image_path):
    img = cv2.imread(str(image_path))
    scale_percent = 0.7  # зменшити до 70% від оригінального розміру
    width = int(img.shape[1] * scale_percent)
    height = int(img.shape[0] * scale_percent)
    res = cv2.resize(img, dsize=(width, height), interpolation=cv2.INTER_LINEAR)
    file_path = save_image(user_id=user_id)
    cv2.imwrite(str(file_path), res)
    return file_path
