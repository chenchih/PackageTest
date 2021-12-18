from setuptools import setup, find_packages
from os import path as OSPath
with open("README.md", 'r') as f:
    long_description = f.read()

# Setting up
setup(
    name="pkgTest",
    version='0.0.2',
    author='ChenChih.Lee',
    author_email="jacklee26@gmail.com",
    url='https://github.com/chenchih/PackageTest',
    license='MIT',
    description='My first Python Hello world library',   
    long_description_content_type="text/markdown",
    long_description=long_description,
    #adding packagedata for bdistr
    include_package_data=True,
    package_data={'pkgTest': ['tt/*.txt']},
    packages=find_packages(),
    #requirement will automatic install it
    #install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    install_requires=['selenium==3.141.0'],
    #install_requires=install_requires,   

    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    entry_points={
    'console_scripts': [
        'helloworld-cli = pkgTest.helloworld:hellotest',
    ]},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
