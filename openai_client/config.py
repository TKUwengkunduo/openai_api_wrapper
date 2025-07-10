import os

class Config:
    """集中管理設定參數"""
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DEFAULT_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    DEFAULT_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY:
            raise ValueError("環境變數 OPENAI_API_KEY 未設定。請先設定 API 金鑰。")