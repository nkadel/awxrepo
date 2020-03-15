#
# spec file for package python-azure-keyvault
#
# Copyright (c) 2019 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

# azure-keyvault is not python2 compatible
%global with_python2 0

%global pypi_name azure-keyvault

# Common SRPM package
Name:           python-%{pypi_name}
Version:        4.0.0
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault
Summary:        Microsoft Azure Key Vault Client Libraries for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
# Azure Key Vault client libraries for Python

This is the Microsoft Azure Key Vault libraries bundle.

This package does not contain any code in itself. It installs a set
of packages that provide APIs for Key Vault operations:

- [azure-keyvault-keys v4.0.x]
- [azure-keyvault-secrets v4.0.x]
- [azure-keyvault-certificates v4.0.x]

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        4.0.0
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault
Summary:        Microsoft Azure Key Vault Client Libraries for Python
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:  python2-azure-keyvault-secrets
Requires:  python2-azure-keyvault-keys
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
# Azure Key Vault client libraries for Python

This is the Microsoft Azure Key Vault libraries bundle.

This package does not contain any code in itself. It installs a set
of packages that provide APIs for Key Vault operations:

- [azure-keyvault-keys v4.0.x]
- [azure-keyvault-secrets v4.0.x]
- [azure-keyvault-certificates v4.0.x]

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        4.0.0
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault
Summary:        Microsoft Azure Key Vault Client Libraries for Python
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:  python%{python3_pkgversion}-azure-keyvault-secrets
Requires:  python%{python3_pkgversion}-azure-keyvault-keys
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
# Azure Key Vault client libraries for Python

This is the Microsoft Azure Key Vault libraries bundle.

This package does not contain any code in itself. It installs a set
of packages that provide APIs for Key Vault operations:

- [azure-keyvault-keys v4.0.x]
- [azure-keyvault-secrets v4.0.x]
- [azure-keyvault-certificates v4.0.x]

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
