import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier_benchmark_data", # Replace with your own username
    version="0.0.1",
    author="Jan Diers",
    author_email="jan.diers@uni-jena.de",
    description="Convenience package to load common benchmarking data sets used for outlier detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'pandas>=0.25.0',
        'scipy>=1.3.2',
        'numpy>=1.18.1'
    ]
)
