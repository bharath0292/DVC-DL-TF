from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="bharath0292",
    description="A small package for dvc DL temsorflow pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bharath0292/DVC-DL-TF",
    author_email="bharath0292@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "tensorflow",
        "pandas",
        "numpy",
        "matplotlib",
        "tqdm",
        "PyYAML",
        "boto3"
    ]
)