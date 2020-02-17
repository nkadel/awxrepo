#
# spec file for package python-ansible-runner
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Fedora >= 38 no longer publishes python2 by default
# RHEL 8 no longer supports python2 by default
%if 0%{?fedora} >= 30 || 0%{?rhel} > 7
%global with_python2 0
%else
%global with_python2 1
%endif

%global pypi_name ansible-runner

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.4.4
Release:        0%{?dist}
Url:            https://github.com/ansible/ansible-runner
Summary:        A tool and python library to interface with Ansible
License:        ASL 2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Ansible Runner is a tool and python library that helps when interfacing with
Ansible directly or as part of another system whether that be through a container
mage interface, as a standalone tool, or as a Python module that can be imported.
The goal is to provide a stable and consistent interface abstraction to Ansible.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        1.4.4
Release:        0%{?dist}
Url:            https://github.com/ansible/ansible-runner
Summary:        A tool and python library to interface with Ansible
License:        ASL 2.0

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-daemon
BuildRequires:  python2-mock
BuildRequires:  python2-pexpect
BuildRequires:  python2-psutil
BuildRequires:  python2-pytest
BuildRequires:  python2-pyyaml

Requires:       ansible
Requires:       python2-daemon
Requires:       python2-pexpect
Requires:       python2-psutil
Requires:       python2-pyyaml
Requires:       python2-setuptools

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Ansible Runner is a tool and python library that helps when interfacing with
Ansible directly or as part of another system whether that be through a container
mage interface, as a standalone tool, or as a Python module that can be imported.
The goal is to provide a stable and consistent interface abstraction to Ansible.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        1.4.4
Release:        0%{?dist}
Url:            https://github.com/ansible/ansible-runner
Summary:        A tool and python library to interface with Ansible
License:        ASL 2.0

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pexpect
BuildRequires:  python%{python3_pkgversion}-daemon
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pyyaml

Requires:       ansible
Requires:       python%{python3_pkgversion}-daemon
Requires:       python%{python3_pkgversion}-pexpect
Requires:       python%{python3_pkgversion}-psutil
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Ansible Runner is a tool and python library that helps when interfacing with
Ansible directly or as part of another system whether that be through a container
mage interface, as a standalone tool, or as a Python module that can be imported.
The goal is to provide a stable and consistent interface abstraction to Ansible.

%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if %{with_python2}
%py2_build
%endif # with_python2

%if %{with_python3}
%py3_build
%endif # with_python3

%install
%if %{with_python2}
%py2_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/ansible-runner $RPM_BUILD_ROOT%{_bindir}/ansible-runner2
%{__ln_s} ansible-runner2 $RPM_BUILD_ROOT%{_bindir}/ansible-runner
%endif # with_python2

%if %{with_python3}
%py3_install
%{__mv} $RPM_BUILD_ROOT%{_bindir}/ansible-runner $RPM_BUILD_ROOT%{_bindir}/ansible-runner%{python3_pkgversion}
%{__ln_s} ansible-runner%{python3_pkgversion} $RPM_BUILD_ROOT%{_bindir}/ansible-runner
%endif # with_python3

%clean
rm -rf %{buildroot}

%if %{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%{_bindir}/ansible-runner2
%if ! %{with_python3}
%{_bindir}/ansible-runner
%endif
%endif # with_python2

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/ansible-runner%{python3_pkgversion}
%{_bindir}/ansible-runner
%endif # with_python3

%check
%if %{with_python2}
%{__python2} setup.py test ||:
%endif

%if %{with_python3}
%{__python3} setup.py test ||:
%endif

%changelog
