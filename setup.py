# setup.py

from setuptools import setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="pymajic",
    version="1.0.1",
    author="Shagbaor Agber",
    author_email="dxtlive@gmail.com",
    description='PyMajic is a Python package that simplifies working with Django projects by providing convenient commands for environment management, custom commands, and more.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = 'https://github.com/Codewithshagbaor/PyMajic', 
    packages=["pymajic"],
    install_requires=[
        "Django",
        "requests",
    ],
    keywords = [
    'Django',
    'project management',
    'virtual environment',
    'Django development',
    'utility',
    'command-line tool',
    'workflow optimization',
    'automation',
    ],
    entry_points={
        'console_scripts': [
            'pymajic = pymajic.store:main',
            # 'pymajic_run_command = pymajic.store:run_custom_command',
            'pymajic shell = pymajic.store:django_shell',
            'pymajic backup database = pymajic.store:backup_database',
            'pymajic restore database = pymajic.store:restore_database',
            'pymajic project info = pymajic.store:project_info',
            'pymajic check update = pymajic.store:check_update',
            'pymajic edit config = pymajic.store:edit_config',
            'pymajic interactive = pymajic.store:interactive_mode',
            'pymajic set alias = pymajic.store:set_alias',
            'pymajic documentation = pymajic.store:documentation',
        ],
    },
)
