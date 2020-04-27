import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imperium",
    version="0.0.1",
    author="DSRetro",
    author_email="dsretro@protonmail.com",
    description="A programming language written in Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DSRetro/imperium",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={"console_scripts": ["imperium = imperium.imperium:main"]},
)

