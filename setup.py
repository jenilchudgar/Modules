from setuptools import setup,find_packages

setup(
    name="PySwitchCase",
    version="1.0.0",
    author="JenilChudgar",
    author_email="jenilchudgar@gmail.com",
    description="The Switch In Python.",
    long_description="The Switch Case construct is a programming structure that allows developers to execute different blocks of code based on the value of a given expression or variable. Although Python does not have a built-in switch statement like some other programming languages (e.g., C++ or Java), there are several ways to achieve similar functionality using alternative approaches.",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-module",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)
