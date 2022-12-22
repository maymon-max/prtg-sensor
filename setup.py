from setuptools import setup

if __name__ == '__main__':
    setup(
        name='prtg-sensor',
        version='0.0.1',
        description='Simple data generator for advanced PRTG sensors',
        author='Max Maymon',
        url='https://github.com/maymon-max/prtg-sensor.git',
        license='MIT',
        packages=['prtg_sensor'],
        classifiers=[
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
    )
