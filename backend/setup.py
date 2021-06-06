import os
from setuptools import setup


setup(
    name = "backend",
    version = "0.0.1",
    author = "Martin Kibui Ndirangu",
    author_email = "m.k.ndirangu@gmail.com",
    description = ("CryptoJungle File Encryptor/Decryptor."),
    license = "BSD",
    keywords = "Crypto Jungle",
    packages=[
        "utils"
    ],
    package_dir={'':'src'},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)