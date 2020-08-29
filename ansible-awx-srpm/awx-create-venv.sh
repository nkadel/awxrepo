#!/bin/bash

set -e
set -x


if [ `id -u` -ne 0 ]; then
    echo Error: $0 will require root privileges to write system files
    exit 1
fi

# AWX is no longer compatible with python 2, stop supporting it
PYTHONBIN=/usr/bin/python3
TARBALL=awx-14.1.0.tar.gz

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
    echo Using obsolete pypi.org version of ansible
    # pypi.org 2.9.12, version of Ansible, *way* behind 14.1.0 tag in git repo
    ${DIRNAME}/bin/pip3 install --upgrade ansible
fi
