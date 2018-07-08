from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author='Manh Dinh',
    author_email="manh@example.com",
    description='SnapshotAlyzer 3000 is a tool to manage EC2 snapshots',
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/manhcat/snapshotalyser-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',

)
