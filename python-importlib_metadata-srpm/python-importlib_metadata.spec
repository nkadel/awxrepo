#
# spec file for package python-importlib-metadata
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

%global with_python2 0

%global pypi_name importlib_metadata

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.5.0
Release:        0%{?dist}
Url:            http://importlib-metadata.readthedocs.io/
Summary:        Read metadata from Python packages
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
``importlib_metadata`` is a library to access the metadata for a Python
package.  It is intended to be ported to Python 3.8.

%if %{with_python2}
%package -n python2-%%{pypi_name}
Version:        1.5.0
Release:        0%{?dist}
Url:            http://importlib-metadata.readthedocs.io/
Summary:        Read metadata from Python packages
License:        Apache-2.0

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm

BuildRequires:  python2-zipp >= 0.5
BuildRequires:  python2-pathlib2
BuildRequires:  python2-contextlib2
BuildRequires:  python2-configparser >= 3.5

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
``importlib_metadata`` is a library to access the metadata for a Python
package.  It is intended to be ported to Python 3.8.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        1.5.0
Release:        0%{?dist}
Url:            http://importlib-metadata.readthedocs.io/
Summary:        Read metadata from Python packages
License:        Apache-2.0

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm

BuildRequires:  python%{python3_pkgversion}-zipp >= 0.5
#BuildRequires:  python%%{python3_pkgversion}-pathlib2
#BuildRequires:  python%%{python3_pkgversion}-contextlib2
#BuildRequires:  python%%{python3_pkgversion}-configparser >= 3.5


%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
``importlib_metadata`` is a library to access the metadata for a Python
package.  It is intended to be ported to Python 3.8.

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
