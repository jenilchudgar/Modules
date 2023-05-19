from setuptools import setup,find_packages

setup(
    name="your-module-name",
    version="1.0.0",
    author="Your Name",
    author_email="your@email.com",
    description="Description of your module",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-module",
    packages=setuptools.find_packages(),
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
