from setuptools import setup
setup(
    name='grappelli-tools',
    version='0.1.0',
    description='Handmade tools for an awesome Grappelli (http://grappelliproject.com/) admin interface for Django.',
    keywords='django grappelli admin',
    license='New BSD License',
    author='Alexander Shvetsov',
    author_email='ashvetsov@gmail.com',
    url='https://github.com/ashvetsov/grappelli-tools',
    install_requires=[
        'django',
        'django-grappelli',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'grappelli_tools',
    ],
    include_package_data=True,
)
