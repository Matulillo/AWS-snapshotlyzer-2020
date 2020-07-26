from setuptools import setup

setup(
    name='AWS-snapshotlyzer-2020',
    version='0.1',
    author='Carlos',
    author_email='carlos@email.com',
    description='Script to manage AWS snapshots',
    license='My',
    packages=['shotty'],
    url='https://github.com/Matulillo/AWS-snapshotlyzer-2020',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
