from setuptools import setup, find_packages

DESCRIPTION = "brickproof-cli"
LONG_DESCRIPTION ="The CLI extension of the brickproof testing library."


# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="brickproof-cli",
    version="0.0.2",
    author="Jordan-M-Young",
    author_email="jordan.m.young0@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["tomlkit","requests","brickproof"],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python3", "databricks", "unit test", "test", "cidd"],
    classifiers=["Programming Language :: Python :: 3", "Framework :: Pytest"],
    entry_points={
        "console_scripts": [
            "brickproof = brickproof_cli.__main__:main"
        ]
    },
)