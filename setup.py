from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name='simon-bot',
    version='0.5',
    packages=find_packages(),
    install_requires=[
        'prompt_toolkit'
    ],
    entry_points={
        "console_scripts": [
            "simon-bot = project.main:main"
        ]
    },
    long_description=description,
    long_description_content_type="text/markdown"
)
