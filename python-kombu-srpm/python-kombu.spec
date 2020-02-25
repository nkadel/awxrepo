#
# spec file for package python-kombu
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Imcmpatible with python2
%global with_python3 1
%global with_python2 0

%global pypi_name kombu

# Common SRPM package
Name:           python-%{pypi_name}
Version:        4.6.7
Release:        0%{?dist}
Url:            https://kombu.readthedocs.io
Summary:        Messaging library for Python.
License:        BSD (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Kombu is a messaging library for Python.

The aim of Kombu is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQ protocol, and also
provide proven and tested solutions to common messaging problems.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        4.6.7
Release:        0%{?dist}
Url:            https://kombu.readthedocs.io
Summary:        Messaging library for Python.
License:        BSD (FIXME:No SPDX)
BuildREquires:  python2
BuildREquires:  python2-devel
Requires:	python2-amqp >= 2.5.2
Conflicts:	python2-amqp >= 2.6
# name correctly for RHEL
#Requires:	python2-importlib-metadata >= 0.18
Requires:	python2-importlib_metadata >= 0.18
%{?python_provide:%python_provide python%{python2_pkgversion}-%{pypi_name}}

%description -n python2-%{pypi_name}
Kombu is a messaging library for Python.

The aim of Kombu is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQ protocol, and also
provide proven and tested solutions to common messaging problems.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        4.6.7
Release:        0%{?dist}
Url:            https://kombu.readthedocs.io
Summary:        Messaging library for Python.
License:        BSD (FIXME:No SPDX)
BuildREquires:  python%{python3_pkgversion}
BuildREquires:  python%{python3_pkgversion}-devel
Requires:	python%{python3_pkgversion}-amqp >= 2.5.2
Conflicts:	python%{python3_pkgversion}-amqp >= 2.6
# name correctly for RHEL
#Requires:	python%%{python3_pkgversion}-importlib-metadata >= 0.18
Requires:	python%{python3_pkgversion}-importlib_metadata >= 0.18
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Kombu is a messaging library for Python.

The aim of Kombu is to make messaging in Python as easy as possible by
providing an idiomatic high-level interface for the AMQ protocol, and also
provide proven and tested solutions to common messaging problems.

%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with_python2}
%py2_build
%endif # with_python3

%if %{with_python3}
%py3_build
%endif # with_python3

%install
%if %{with_python3}
%py3_install
%endif # with_python3

%if %{with_python2}
%py2_install
%endif # with_python2

%clean
rm -rf %{buildroot}

%if %{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%endif # with_python3

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%endif # with_python3

%changelog
