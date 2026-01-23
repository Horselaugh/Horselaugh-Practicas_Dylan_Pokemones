from setuptools import setup, find_packages

setup(
    name='odoo',
    version='18.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psycopg2-binary',
        'lxml',
        'pillow',
        'python-dateutil',
        'Babel',
        'Werkzeug',
    ],
)
