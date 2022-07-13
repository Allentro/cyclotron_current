from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setup(
    name="cyclotron_current", # Replace with your own username
    version="0.0.1",
    author="Ross Allen",
    author_email="rossallen1996@gmail.com",
    description="Python module for analysing current over time.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Allentro/spec_conv",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'numpy', 
        'matplotlib'])
