from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='espy',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'espy=espy.__main__:main',
        ],
    },
    author='Tu Nombre',
    author_email='tu.email@ejemplo.com',
    description='Transpilador de Python en español: ejecuta código Python usando palabras clave y sintaxis en español.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TU_USUARIO/espy',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Spanish',
        'Topic :: Software Development :: Interpreters',
        'Intended Audience :: Developers',
    ],
    install_requires=[],
    include_package_data=True,
)
