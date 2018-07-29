#!/usr/bin/env python

"""
Edit an attribute in a NetCDF file.
"""

import argparse
from netCDF4 import Dataset

def cli():

    parser = argparse.ArgumentParser(description='Edit an attribute in a NetCDF file')
    parser.add_argument('ncfile', help='NetCDF file to edit')
    parser.add_argument('attr', help='NetCDF attribute to edit')
    parser.add_argument('value', help='Value for the attribute')
    args = parser.parse_args()

    with Dataset(args.ncfile, 'r+') as nc:
        nc.setncattr(args.attr, args.value)
