from setuptools import setup

setup(
    name='edit-ncattr',
    version='0.1.0',
    description='Edits an attribute in a NetCDF file',
    author='Cloudrun Inc.',
    author_email='hello@cloudrun.co',
    url='https://github.com/cloudruninc/edit-ncattr',
    packages=['edit_ncattr'],
    install_requires=['netCDF4'],
    entry_points={'console_scripts': ['edit-ncattr = edit_ncattr.cli:cli']},
    license='MIT'
)
