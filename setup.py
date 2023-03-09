from setuptools import find_packages, setup

VERSION = "0.1.0"

setup(
    name="openweather",
    version=VERSION,
    license="MIT",
    description="OpenWeather API connector",
    author="An Di",
    author_email="bereich_folio0b@icloud.com",
    url="https://github.com/LeOnAnDi/openwaether",
    packages=find_packages(exclude=("tests", "docs")),
    python_requires=">=3.11.2",
)
