from setuptools import find_packages, setup

package_name = 'gps_coords'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kiara-sophia',
    maintainer_email='kiara-sophia@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'gps_publisher = gps_coords.gps_publisher:main',
            'gps_subscriber = gps_coords.gps_subscriber:main',
        ],
    },
)
