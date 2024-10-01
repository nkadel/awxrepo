awxrepo
==========

Wrapper for SRPM building tools for awx on RHEL. RHEL 7 has a
working version published via EPEL, but it's out of date, so this
provides an RPM based upgrade path.

Building awx
===============

Ideally, install "mock" and use that to build for both RHEL 6 and RHEL

* make cfgs # Create local .cfg configs for "mock".
* * centos-stream+epel-8-x86_64.cfg
* * centos-stream+epel-9-x86_64.cfg
* * centos-stream+epel-10-x86_64.cfg
* * fedora-40-x86_64.cfg
# # awxrepo-7-x86_64.cfg
# # awxrepo-8-x86_64.cfg
# # awxrepo-10-x86_64.cfg
# # awxrepo-f40-x86_64.cfg

* make repos # Creates local local yum repositories in $PWD/awxrepo
* * awxrepo/el/8
* * awxrepo/el/9
* * awxrepo/el/10
* * awxrepo/fedora/40

* make # Make all distinct versions using "mock"

Building a compoenent, without "mock" and in the local working system,
can also be done for testing.

* make build

awx has strong dependencies on other python modules that may, or may not,
be available in a particular OS. These are listed in the Makefile

Installing Awx
=================

The relevant yum repository is built locally in awxreepo. To enable the repository, use this:

* make repo

Then install the .repo file in /etc/yum.repos.d/ as directed. This
requires root privileges, which is why it's not automated.

Awx RPM Build Security
====================

There is a significant security risk with enabling yum repositories
for locally built components. Generating GPF signed packages and
ensuring that the compneents are in this build location are securely
and safely built is not addressed in this test setup.

		Nico Kadel-Garcia <nkadel@gmail.com>
