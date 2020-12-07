from setuptools import find_packages, setup

setup(
    name='memedagsins_bakendi',
    version='0.0.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask', 'python-dotenv', 'python-pam', 'flask-cors'
    ],
)