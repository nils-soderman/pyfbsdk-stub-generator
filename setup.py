from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()
    
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pyfbsdk-stub-generator',
    version='2025.0.0',
    author='Nils Soderman',
    description='Generate pyfbsdk stub files for better intellisense when working with MotionBuilder',
    license='MIT-0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nils-soderman/pyfbsdk-stub-generator',
    keywords='pyfbsdk, motionbuilder, mobu, autodesk, stub, stubfile, generator, gen',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=requirements,
    package_data={
        '': ['*.pyi'],
    },
)