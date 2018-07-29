# edit-ncattr

A simple CLI tool to edit an attribute in a NetCDF file.

## Getting started

### Install

```
pip install git+https://github.com/cloudruninc/edit-ncattr
```

### Usage

```
edit-ncattr -h
usage: edit-ncattr [-h] ncfile attr value

Edit an attribute in a NetCDF file

positional arguments:
  ncfile      NetCDF file to edit
  attr        NetCDF attribute to edit
  value       Value for the attribute

optional arguments:
  -h, --help  show this help message and exit
```

Example:

```
edit-ncattr wrfinput_d01 SF_SURFACE_PHYSICS 1
```

## Comments

This tools replaces a subset of functionality from NCO's `ncatted`.
You could reproduce the above example with `ncatted` like this:

```
ncatted -a SF_SURFACE_PHYSICS,global,m,i,1 wrfinput_d01
```

Thus, if you have access to NCO, use that instead.
