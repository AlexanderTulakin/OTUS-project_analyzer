from setuptools import setup
import project_analyzer

setup(
    name='project_analyzer',
    version=project_analyzer.__version__,
    packages=['project_analyzer'],
    url='https://github.com/AlexanderTulakin/OTUS-project_analyzer',
    license='',
    author='hudonio',
    author_email='iatulakin@gmail.com',
    description='Util to analyze projects words',
    install_requires=['nltk', 'validator-collection', 'gitpython'],
    entry_points={
        'console_scripts':
            ['project_analyzer=project_analyzer.__main__:run']
        }
)
