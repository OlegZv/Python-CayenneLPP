import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-cayennelpp",
    version="0.0.1",
    author="Oleg Zvonarov",
    author_email="oleg.somov84@gmail.com",
    description="A package to decode a data encoded in a CayenneLPP format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OlegSomov/Python-CayenneLPP",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "License :: OSI Approved :: Apache",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
