#
# spec file for package python-pytest-param
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

# Fedora and RHEL split python2 and python3
# Older RHEL requires EPEL and python34 or python36
%global with_python3 1

%global with_python2 0

%global pypi_name pytest-param

# Common SRPM package
Name:           python-%{pypi_name}
Version:        0.1.1
Release:        0%{?dist}
Url:            https://github.com/cr3/pytest-param
Summary:        pytest plugin to test all, first, last or random params
License:        MIT
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
pytest-param
============

pytest-param is a plugin for `py.test <http://pytest.org>`_ that makes it
easy to test all, first, last or random params.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        0.1.1
Release:        0%{?dist}
Url:            https://github.com/cr3/pytest-param
Summary:        pytest plugin to test all, first, last or random params
License:        MIT

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools_scm
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
pytest-param
============

pytest-param is a plugin for `py.test <http://pytest.org>`_ that makes it
easy to test all, first, last or random params.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        0.1.1
Release:        0%{?dist}
Url:            https://github.com/cr3/pytest-param
Summary:        pytest plugin to test all, first, last or random params
License:        MIT

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools_scm

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
pytest-param
============

pytest-param is a plugin for `py.test <http://pytest.org>`_ that makes it
easy to test all, first, last or random params.

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
