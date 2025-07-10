from setuptools import setup, find_packages

setup(
    name="openai_client",
    version="0.1.0",
    packages=find_packages(include=["openai_client", "openai_client.*"]),
    install_requires=[
        "openai==0.28.0",
    ],
    python_requires=">=3.7",
)
