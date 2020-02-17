#
# spec file for package python-gitdb2
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

%global with_python2 0

%global pypi_name gitdb2
%global old_name gitdb

# Common SRPM package
Name:           python-%{pypi_name}
Version:        3.0.2
Release:        0%{?dist}
Url:            https://github.com/gitpython-developers/gitdb
Summary:        Git Object Database
License:        BSD License (FIXME:No SPDX)
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
GitDB is a pure-Python git object database

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        3.0.2
Release:        0%{?dist}
Url:            https://github.com/gitpython-developers/gitdb
Summary:        Git Object Database
License:        BSD License (FIXME:No SPDX)

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Conflicts:  python2-%{old_name}
Obsoletes:  python2-%{old_name} <= %{version}
Provides:  python2-%{old_name} = %{version}-%{release}

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
GitDB is a pure-Python git object database

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        3.0.2
Release:        0%{?dist}
Url:            https://github.com/gitpython-developers/gitdb
Summary:        Git Object Database
License:        BSD License (FIXME:No SPDX)

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{old_name}}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Conflicts:  python%{python3_pkgversion}-%{old_name}
Obsoletes:  python%{python3_pkgversion}-%{old_name} <= %{version}
Provides:  python%{python3_pkgversion}-%{old_name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{pypi_name}
GitDB is a pure-Python git object database

%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with_python2}
%py2_build
%endif # with_python2

%if %{with_python3}
%py3_build
%endif # with_python3

%install
%if %{with_python2}
%py2_install
%endif # with_python2

%if %{with_python3}
%py3_install
%endif # with_python3

%clean
rm -rf %{buildroot}

%if %{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%{python2_sitelib}/*
%endif # with_python2

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitelib}/*
%endif # with_python3

%changelog
