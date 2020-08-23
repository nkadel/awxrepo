#
# spec file for package python-azure-common
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Not compatible with pyt9on2
%global with_python2 0

%global pypi_name azure-common

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.1.23
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Client Library for Python (Common)
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
This is the Microsoft Azure common code.

This package provides shared code by the Azure packages.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        1.1.23
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Client Library for Python (Common)
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This is the Microsoft Azure common code.

This package provides shared code by the Azure packages.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        1.1.23
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Client Library for Python (Common)
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This is the Microsoft Azure common code.

This package provides shared code by the Azure packages.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.

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
