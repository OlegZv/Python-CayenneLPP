import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-cayennelpp",
    version="0.0.3",
    author="Oleg Zvonarov",
    author_email="oleg.somov84@gmail.com",
    description="A package to decode a data encoded in a CayenneLPP format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OlegSomov/Python-CayenneLPP",
    packages=setuptools.find_packages(),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
