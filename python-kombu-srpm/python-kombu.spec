#
# spec file for package python-kombu
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# python3_pkgversion macro for EPEL in older RHEL
%if 0%{?rhel}
BuildRequires: epel-rpm-macros
%endif

# Imcmpatible with python2
%global with_python3 1
%global with_python2 0

# Older RHEL does not use dnf, does not support "Suggests"
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_dnf 1
%else
%global with_dnf 0
%endif

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

%description


%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        4.6.7
Release:        0%{?dist}
Url:            https://kombu.readthedocs.io
Summary:        Messaging library for Python.
License:        BSD (FIXME:No SPDX)
Requires:	python%{python3_pkgversion}-amqp >= 2.5.2
Conflicts:	python%{python3_pkgversion}-amqp >= 2.6
Requires:	python%{python3_pkgversion}-importlib-metadata >= 0.18

# requires stanza of py2pack
# install_requires stanza of py2pack
%if %{with_dnf}
%endif # with_dnf
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}


%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with_python3}
%py3_build
%endif # with_python3

%install
%if %{with_python3}
%py3_install
%endif # with_python3

%clean
rm -rf %{buildroot}

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%endif # with_python3

%changelog
