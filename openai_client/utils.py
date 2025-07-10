import logging
import base64
import io


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


def encode_image_to_base64(path: str) -> str:
    """
    將指定路徑的影像檔讀取並轉為 Base64 字串(不含 data URI header)
    """
    with open(path, 'rb') as img_file:
        encoded = base64.b64encode(img_file.read()).decode('utf-8')
    return encoded