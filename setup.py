import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="transfermarkt-wrapper",
    version="0.0.6",  
    description="Python API wrapper for Transfermarkt undocumented API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tommhe14/transfermarkt-wrapper",
    author="tommhe14",
    author_email="theckley@yahoo.co.uk",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[
        "aiohttp>=3.8.0",  
        "beautifulsoup4>=4.9.3"
    ],
    python_requires=">=3.8",
    keywords="transfermarkt tmk football soccer fotmob sofascore flashscore api wrapper",
    project_urls={
        "Bug Reports": "https://github.com/tommhe14/cs2api/transfermarkt-wrapper",
        "Source": "https://github.com/tommhe14/transfermarkt-wrapper",
    },
)