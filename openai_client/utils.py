import logging
import base64
import io
import cv2
import numpy as np
from typing import Union


def setup_logger(name: str = __name__, level: int = logging.INFO) -> logging.Logger:
    """建立 logger，方便追蹤 request/response 與錯誤"""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        fmt = "[%(asctime)s] %(levelname)s %(name)s: %(message)s"
        handler.setFormatter(logging.Formatter(fmt))
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def decode_base64_image(b64_string: str) -> io.BytesIO:
    """
    將 Base64 字串解碼為可傳給 openai API 的 BytesIO 物件
    """
    header, _, data = b64_string.partition(',')
    img_bytes = base64.b64decode(data or header)
    return io.BytesIO(img_bytes)


def encode_image_to_base64(
    source: Union[str, bytes, np.ndarray],
    is_raw: bool = False
) -> str:
    """
    將影像轉換為 Base64 字串：
    - source: 可以是檔案路徑、影像 bytes、或 numpy.ndarray
    - is_raw: 為 True 時，source 應為 bytes 或 numpy
    """
    if not is_raw:
        # 預設：來源為檔案路徑
        with open(source, 'rb') as img_file:
            image_data = img_file.read()
    else:
        if isinstance(source, np.ndarray):
            success, buffer = cv2.imencode('.jpg', source)
            if not success:
                raise ValueError("無法將影像編碼為 JPG 格式")
            image_data = buffer.tobytes()
        elif isinstance(source, bytes):
            image_data = source
        else:
            raise TypeError("不支援的影像類型，必須是 numpy.ndarray 或 bytes")

    # 回傳 base64 編碼字串
    return base64.b64encode(image_data).decode('utf-8')
