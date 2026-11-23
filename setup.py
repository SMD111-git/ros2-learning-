nano setup.py
from setuptools import setup

package_name = 'car5_learning'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ZAS Robotics',
    description='Practical Car-5 ROS 2 learning projects',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'odom_monitor = car5_learning.odom_monitor:main',
        ],
    },
)

