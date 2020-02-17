#
# spec file for package python-adal
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

%global pypi_name adal

# Common SRPM package
Name:           python-%{pypi_name}
Version:        1.2.2
Release:        0%{?dist}
Url:            https://github.com/AzureAD/azure-activedirectory-library-for-python
Summary:        The ADAL for Python library makes it easy for python application to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.
License:        MIT
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description


%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        1.2.2
Release:        0%{?dist}
Url:            https://github.com/AzureAD/azure-activedirectory-library-for-python
Summary:        The ADAL for Python library makes it easy for python application to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:	python2-pyjwt >= 1.0.0
Requires:	python2-requests >= 2.0.0
Requires:	python2-dateutil >= 2.1.0
Requires:	python2-cryptography >= 1.1.0
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}


%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        1.2.2
Release:        0%{?dist}
Url:            https://github.com/AzureAD/azure-activedirectory-library-for-python
Summary:        The ADAL for Python library makes it easy for python application to authenticate to Azure Active Directory (AAD) in order to access AAD protected web resources.
License:        MIT
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
Requires:	python%{python3_pkgversion}-pyjwt >= 1.0.0
Requires:	python%{python3_pkgversion}-requests >= 2.0.0
Requires:	python%{python3_pkgversion}-dateutil >= 2.1.0
Requires:	python%{python3_pkgversion}-cryptography >= 1.1.0

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}


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
