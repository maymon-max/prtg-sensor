from setuptools import setup

if __name__ == '__main__':

    with open('README.md') as f:
        README = f.read()

    setup(
        name='prtg-sensor',
        version='1.0.0',
        description='Simple data generator for advanced PRTG sensors',
        long_description=README,
        long_description_content_type='text/markdown',
        author='Max Maymon',
        url='https://github.com/maymon-max/prtg-sensor.git',
        license='MIT',
        keywords='prtg',
        packages=['prtg_sensor'],
        classifiers=[
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
    )
