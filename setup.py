from setuptools import setup
import aiosoundcloud

with open("README.md", "r",encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="aiosoundcloud",  # Library name                                  
    version= aiosoundcloud.__version__,  # Version
    
    install_requires=[
        "aiohttp"
    ],
    description="A lightweight AI  library for building chatbot applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    author="sioxty",
    author_email="maksymslushayev@gmail.com",
    
    packages=[
        "aiosoundcloud",
    ],
    url="https://github.com/sioxty/aiosoundcloud", 
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version
)