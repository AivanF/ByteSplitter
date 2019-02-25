import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='ByteSplitter',
    version='1.0.0',
    author='AivanF.',
    author_email='projects@aivanf.com',
    description='A tiny Python utility for splitting any binary files into parts and combining them back',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AivanF/ByteSplitter',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Utilities',
        'Topic :: Security',
        'Topic :: System :: Filesystems',
        'License :: Freely Distributable',
    ],
)
