#
# spec file for package python-azure-nspkg
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# Fedora >= 38 no longer publishes python2 by default
%if 0%{?fedora} >= 30
%global with_python2 0
%else
%global with_python2 1
%endif

# Older RHEL does not use dnf, does not support "Suggests"
%global pypi_name azure-nspkg

# Common SRPM package
Name:           python-%{pypi_name}
Version:        3.0.2
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Namespace Package [Internal]
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  bzip2
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure namespace package.

This package is not intended to be installed directly by the end user.

Since version 3.0, this is Python 2 package only, Python 3.x SDKs will use `PEP420 <https://www.python.org/dev/peps/pep-0420/>`__ as namespace package strategy.
To avoid issues with package servers that does not support `python_requires`, a Python 3 package is installed but is empty.

It provides the necessary files for other packages to extend the azure namespace.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.




%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        3.0.2
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Namespace Package [Internal]
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure namespace package.

This package is not intended to be installed directly by the end user.

Since version 3.0, this is Python 2 package only, Python 3.x SDKs will use `PEP420 <https://www.python.org/dev/peps/pep-0420/>`__ as namespace package strategy.
To avoid issues with package servers that does not support `python_requires`, a Python 3 package is installed but is empty.

It provides the necessary files for other packages to extend the azure namespace.

If you are looking to install the Azure client libraries, see the
`azure <https://pypi.python.org/pypi/azure>`__ bundle package.




%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        3.0.2
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python
Summary:        Microsoft Azure Namespace Package [Internal]
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Microsoft Azure SDK for Python
==============================

This is the Microsoft Azure namespace package.

This package is not intended to be installed directly by the end user.

Since version 3.0, this is Python 2 package only, Python 3.x SDKs will use `PEP420 <https://www.python.org/dev/peps/pep-0420/>`__ as namespace package strategy.
To avoid issues with package servers that does not support `python_requires`, a Python 3 package is installed but is empty.

It provides the necessary files for other packages to extend the azure namespace.

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
