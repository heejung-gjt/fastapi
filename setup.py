from setuptools import find_packages, setup

install_requires = [
    'fastapi==0.86.0',
    'gunicorn==20.1.0',
    'uvicorn==0.22.0',
    'asyncpg==0.27.0',
    'python-dotenv==1.0.0',
]

debug_requires = [
    'rich==13.4.1',
    'types-ujson==5.7.0.5',
    'asyncpg-stubs==0.27.0',
    'types-requests==2.31.0.1',
]

setup(
    name='fastapi-project',
    version='1.0.0',
    packages=find_packages(),
    include_pacakge_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': debug_requires + install_requires,
    }
)
