from setuptools import setup, find_packages


setup(
    name='latex-generator-sesorov',
    version='1.0.0',
    description='Generate LaTeX table and image from input data for ITMO course',
    author='Aleksandr Sesorov',
    author_email='samws@mail.ru',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'latex-generator=src.main:main'
        ],
    },
)
