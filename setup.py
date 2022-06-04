import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='svfl',
    version='0.1.0',
    description='A package for computing the average marginal contribution (Shapley Value) for each client in a Federated Learning environment',
    url='https://github.com/akassharjun/ShapleyValueFL',
    author='Akassharjun Shanmugarajah',
    author_email='akassharjun@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],

    classifiers=[
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)