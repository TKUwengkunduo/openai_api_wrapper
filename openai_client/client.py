import openai
from typing import List, Dict, Optional, Any
from .config import Config
from .utils import setup_logger, encode_image_to_base64


# 在使用前先驗證 API Key
Config.validate()

logger = setup_logger(__name__)

class OpenAIClient:
    """封裝 OpenAI API 的核心類別，支援文字與影像互動，並可自訂多角色輸入。"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        temperature: Optional[float] = None
    ):
        self.api_key = api_key or Config.OPENAI_API_KEY
        openai.api_key = self.api_key

        self.model = model or Config.DEFAULT_MODEL
        self.temperature = temperature or Config.DEFAULT_TEMPERATURE
        logger.debug(f"Initialized OpenAIClient with model={self.model}, temperature={self.temperature}")

    def chat_completion(
        self,
        messages: List[Dict[str, Any]],
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        **kwargs
    ) -> Dict:
        """
        通用 chat completion，支援多角色與影像上傳。
        messages: List of dicts，每個 dict 必須包含：
          - role: "system" | "user" | "assistant"
          - content:
            * str: 一般文字
            * List[Dict]: 多元素清單，元素為 text/image_path/image_url
        """
        api_messages = []
        for m in messages:
            role = m.get('role')
            content = m.get('content')
            if isinstance(content, list):
                processed = []
                for item in content:
                    t = item.get('type')
                    if t == 'text':
                        processed.append({"type": "text", "text": item.get('text')})
                    elif t == 'image_path':
                        b64 = encode_image_to_base64(item.get('path'))
                        processed.append({
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{b64}"}
                        })
                    elif t == 'image_url':
                        processed.append({
                            "type": "image_url",
                            "image_url": {"url": item.get('url')}
                        })
                    elif t == 'image_data':
                        image_data = item.get('data')
                        if image_data is not None:
                            b64 = encode_image_to_base64(image_data, is_raw=True)
                            processed.append({
                                "type": "image_url",
                                "image_url": {"url": f"data:image/jpeg;base64,{b64}"}
                            })
                    else:
                        logger.warning(f"Unknown content type: {t}")
                api_messages.append({"role": role, "content": processed})
            else:
                api_messages.append({"role": role, "content": content})

        params = {
            "model": model or self.model,
            "messages": api_messages,
            "temperature": temperature or self.temperature,
            **kwargs
        }
        logger.info(f"chat_completion params: model={params['model']}, temperature={params['temperature']}")
        try:
            resp = openai.ChatCompletion.create(**params)
            logger.debug(f"chat_completion response: {resp}")
            return resp
        except Exception as e:
            logger.error(f"chat_completion failed: {e}")
            raise