#!/bin/bash

set -e
set -x


if [ `id -u` -ne 0 ]; then
    echo Error: $0 will require root privileges to write system files
    exit 1
fi

# System requirements for pip installs to work
yum -y install gcc openldap-devel libpq-devel krb5-devel xmlsec1 postgresql-devel


# AWX is no longer compatible with python 2, stop supporting it
PYTHONBIN=/usr/bin/python3
TARBALL=awx-14.1.0.tar.gz
VERSION=14.1.0

#DIRNAME=${PWD}/ansible
DIRNAME=/var/lib/awx
#if [ -e $DIRNAME ]; then
#    echo Error: $DIRNAME already exists
#    exit 1
#fi

${PYTHONBIN} -m venv $DIRNAME

source ${DIRNAME}/bin/activate
## Some modules use and benefit from wheel installation
#${DIRNAME}/bin/pip3 install --upgrade wheel
## Silence bitter complants about obsolete pip
#${DIRNAME}/bin/pip3 install --upgrade pip
# Critical dependencies for ansible
${DIRNAME}/bin/pip3 install --upgrade python-memcached psutil
if [ -e $TARBALL ]; then
    echo Using ansible tarball: $%ARBALL
    ${DIRNAME}/bin/pip3 install --upgrade $TARBALL
else
    echo Checkout out git repo in $PWD/awx
    git clone https://github.com/ansible/awx awx
    cd awx
    git checkout $VERSION
    python setup.py install
fi

# Add modules
pip install django
pip install split_settings
pip install ldap


