from setuptools import setup
from setuptools import find_packages

setup(
    name='car_scraper', ## This will be the name your package will be published with
    version='0.0.2',
    description='Mock package that allows extract second-hand car data from ebay',
    #long_description=read_me, #README file
    url='https://github.com/Simeon94/ebay_car_scraper_pypi.git', # Add the URL of your github repo if published
                                                              # in GitHub
    author='Simeon Bamgbaye', # Your name
    license='MIT',
    packages=find_packages(), # This one is important to explain. See the notebook for a detailed explanation
    install_requires=['selenium', 'sqlalchemy', 'pandas', 'psycopg2-binary'], # For this project we are using two external libraries
                                                     # Make sure to include all external libraries in this argument
)