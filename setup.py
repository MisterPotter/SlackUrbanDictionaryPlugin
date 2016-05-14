from setuptools import (
    setup,
    find_packages
)

setup(
    name='udplugin',
    version='0.1',
    author='Tyler Potter',
    author_email='tjpotter@uvic.ca',
    description=(
        'An application to be run on a Heroku server, or other server, '
        'which can then be used as a Slack hook.'
    ),
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=[
        'mock',
        'pytest'
    ],
    test_suite='test',
    package_dir={'': 'src'},
    packages=find_packages('src'),
)
