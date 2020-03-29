# Created by pyp2rpm-3.2.2
%global pypi_name pluggy

%global with_python2 0
%global with_python3 1

Name:           python-%{pypi_name}
Version:        0.13.1
Release:        1%{?dist}
Summary:        plugin and hook calling mechanisms for python

License:        MIT license
URL:            https://github.com/pytest-dev/pluggy
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
 pluggy A minimalist production ready plugin system |pypi| |condaforge|
|versions| |travis| |appveyor| |gitter| |black| |codecov|This is the core
framework used by the pytest_, tox_, and devpi_ projects.Please read the docs_
to learn more!A definitive example .. codeblock:: python import pluggy hookspec
pluggy.HookspecMarker("myproject") hookimpl pluggy.HookimplMarker("myproject")
class ...

%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-setuptools
BuildRequires:  python2-sphinx
BuildRequires:  python2-importlib_metadata
 
%description -n python2-%{pypi_name}
 pluggy A minimalist production ready plugin system |pypi| |condaforge|
|versions| |travis| |appveyor| |gitter| |black| |codecov|This is the core
framework used by the pytest_, tox_, and devpi_ projects.Please read the docs_
to learn more!A definitive example .. codeblock:: python import pluggy hookspec
pluggy.HookspecMarker("myproject") hookimpl pluggy.HookimplMarker("myproject")
class ...
%endif

%if %{with_python3}
%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-importlib_metadata

%description -n python%{python3_pkgversion}-%{pypi_name}
 pluggy A minimalist production ready plugin system |pypi| |condaforge|
|versions| |travis| |appveyor| |gitter| |black| |codecov|This is the core
framework used by the pytest_, tox_, and devpi_ projects.Please read the docs_
to learn more!A definitive example .. codeblock:: python import pluggy hookspec
pluggy.HookspecMarker("myproject") hookimpl pluggy.HookimplMarker("myproject")
class ...
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with_python2}
%py2_build
%endif

%if %{with_python3}
%py3_build
%endif

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%if %{with_python3}
%py3_install
%endif

%if %{with_python2}
%py2_install
%endif

%if %{with_python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc changelog/README.rst README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc changelog/README.rst README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Sun Mar 29 2020 Nico Kadel-Garcia - 0.13.1-1
- Initial package.
