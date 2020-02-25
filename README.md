Build RPM dependencies along with ansible-awx
=============================================

This is based on work by mrmeee at:

* https://copr.fedorainfracloud.org/fedora/mrmeee/ansible-awx/

The repo files there is at:

* https://copr.fedorainfracloud.org/coprs/mrmeee/ansible-awx/
* https://copr.fedorainfracloud.org/coprs/mrmeee/ansible-awx/repo/epel-7/mrmeee-ansible-awx-epel-7.repo

These are sorking local copies only. Significant re-arrangements include:

* Discarding SCL python3.6 and using the CentOS and EPSL provided python3 layout
* Discarding SCL potgresql10 and using a standard postgresl, from a third party repo
  if necessary
* Using consistent "python{version}-module" names for packages, except where RHEL upstream
  chose to violate the rule. This includes python3-pyjwt and python3-django.
* Building packages in a local 'mock' enabled repo, rather than building them all en mass
  on a live server environment.
