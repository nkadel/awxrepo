#
# spec file for package python-azure-keyvault-secrets
#
# Copyright (c) 2020 Nico Kadel-Garcia.
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

%global pypi_name azure-keyvault-secrets

# Common SRPM package
Name:           python-%{pypi_name}
Version:        4.0.1
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets
Summary:        Microsoft Azure Key Vault Secrets Client Library for Python
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.zip
BuildArch:      noarch

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

BuildRequires:  unzip

%description
# Azure Key Vault Secret client library for Python
Azure Key Vault helps solve the following problems:
- Secrets management (this library) -
securely store and control access to tokens, passwords, certificates, API keys,
and other secrets
- Cryptographic key management
([azure-keyvault-keys](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets)) -
create, store, and control access to the keys used to encrypt your data
- Certificate management
([azure-keyvault-certificates](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-certificates)) -
create, manage, and deploy public and private SSL/TLS certificates

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        4.0.1
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets
Summary:        Microsoft Azure Key Vault Secrets Client Library for Python
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
# Azure Key Vault Secret client library for Python
Azure Key Vault helps solve the following problems:
- Secrets management (this library) -
securely store and control access to tokens, passwords, certificates, API keys,
and other secrets
- Cryptographic key management
([azure-keyvault-keys](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets)) -
create, store, and control access to the keys used to encrypt your data
- Certificate management
([azure-keyvault-certificates](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-certificates)) -
create, manage, and deploy public and private SSL/TLS certificates

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        4.0.1
Release:        0%{?dist}
Url:            https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets
Summary:        Microsoft Azure Key Vault Secrets Client Library for Python
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
# Azure Key Vault Secret client library for Python
Azure Key Vault helps solve the following problems:
- Secrets management (this library) -
securely store and control access to tokens, passwords, certificates, API keys,
and other secrets
- Cryptographic key management
([azure-keyvault-keys](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-secrets)) -
create, store, and control access to the keys used to encrypt your data
- Certificate management
([azure-keyvault-certificates](https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/keyvault/azure-keyvault-certificates)) -
create, manage, and deploy public and private SSL/TLS certificates

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
