from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'My first Python Hello world library'
#LONG_DESCRIPTION = 'A basic hello world package.'

# Setting up
setup(
    name="pkgTest",
    version=VERSION,
    author='ChenChih.Lee',
    author_email="jacklee26@gmail.com",
    license='MIT',
    description=DESCRIPTION,   
    #long_description_content_type="text/markdown",
    #long_description=long_description,
    packages=find_packages(),
    #install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
