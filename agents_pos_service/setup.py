from setuptools import setup

package_name = 'agents_pos_service'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='drone',
    maintainer_email='drone@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'agent_service = agents_pos_service.service_member_function:main',
            'agent_client = agents_pos_service.client_member_function:main',
            'agent0 = agents_pos_service.agent0:main',
            'agent1 = agents_pos_service.agent1:main',
            'agent2 = agents_pos_service.agent2:main',
            'vagent0 = agents_pos_service.v_agent0:main',
            'vagent1 = agents_pos_service.v_agent1:main',
            'vagent2 = agents_pos_service.v_agent2:main',
            'bridge = agents_pos_service.bridge_gazebo:main',
            'twin0 = agents_pos_service.v_twin0:main',
            'twin1 = agents_pos_service.v_twin1:main',
            'test = agents_pos_service.test:main',
        ],
    },
)
