# Created by pyp2rpm-3.3.2
%global srcname jaraco.functools
%global pypi_name jaraco-functools
# Fedora doesn't have all the docs deps yet
%bcond_with docs

Name:           python-%{pypi_name}
Version:        2.0
Release:        2%{?dist}
Summary:        Functools like those found in stdlib

License:        MIT
URL:            https://github.com/jaraco/jaraco.functools
Source0:        %{pypi_source %{srcname}}
BuildArch:      noarch
 
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Functools like those found in stdlib

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-jaraco

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-jaraco-classes
BuildRequires:  python%{python3_pkgversion}-more-itertools
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.5
BuildRequires:  python%{python3_pkgversion}-pytest-flake8
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15
BuildRequires:  python%{python3_pkgversion}-six
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Functools like those found in stdlib

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        jaraco-functools documentation

BuildRequires:  python%{python3_pkgversion}-jaraco-packaging >= 3.2
BuildRequires:  python%{python3_pkgversion}-rst-linker >= 1.9
BuildRequires:  python%{python3_pkgversion}-sphinx

%description -n python-%{pypi_name}-doc
Documentation for jaraco-functools
%endif

%prep
%autosetup -n jaraco.functools-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info
# rename package with a -
sed -i 's/%{srcname}/%{pypi_name}/' setup.cfg
# rename jaraco dependencies to use a -
sed -i 's/^\tjaraco\./	jaraco-/' setup.cfg

%build
%py3_build

%if %{with docs}
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-%{python3_version} docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
# disabled for right now, need a newer version of pytest-flake8
# https://src.fedoraproject.org/rpms/python-pytest-flake8/pull-request/2
# AttributeError: 'Application' object has no attribute 'make_notifier'
# LANG=C.utf-8 %%{__python3} -m pytest --ignore=build

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/jaraco/functools*
%{python3_sitelib}/jaraco/__pycache__/functools*
%{python3_sitelib}/jaraco_functools-%{version}-py?.?.egg-info
# These excludes are provided by python%%{python3_pkgversion}-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Dan Radez <dradez@redhat.com> - 2.0-1
- Initial package.
