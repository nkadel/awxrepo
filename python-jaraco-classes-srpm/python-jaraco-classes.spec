# Created by pyp2rpm-3.3.2
%global pkg_name jaraco-classes
%global pypi_name jaraco.classes
# waiting on jaraco-packaging and rst-linker to build docs
%bcond_with doc

Name:           python-%{pkg_name}
Version:        2.0
Release:        3%{?dist}
Summary:        Utility functions for Python class constructs

License:        MIT
URL:            https://github.com/jaraco/jaraco.classes
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros

%description
Utility functions for Python class constructs.

%package -n python3-%{pkg_name}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-jaraco
Requires:       python%{python3_pkgversion}dist(six)

BuildConflicts: python%{python3_pkgversion}dist(pytest) = 3.7.3
BuildRequires:  python3-devel
BuildRequires:  python%{python3_pkgversion}dist(pytest) >= 3.5
BuildRequires:  python%{python3_pkgversion}dist(pytest-flake8)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm) >= 1.15

%{?python_provide:%python_provide python3-%{pkg_name}}

%description -n python3-%{pkg_name}
Utility functions for Python class constructs.

%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        jaraco-classes documentation

BuildRequires:  python%{python3_pkgversion}dist(pytest-checkdocs)
BuildRequires:  python%{python3_pkgversion}dist(sphinx)
BuildRequires:  python%{python3_pkgversion}dist(jaraco-packaging) >= 3.2
BuildRequires:  python%{python3_pkgversion}dist(rst-linker) >= 1.9

%description -n python-%{pkg_name}-doc
Documentation for jaraco-classes
%endif

%prep
%autosetup -n jaraco.classes-%{version}
# Remove bundled egg-info
rm -rf %{pkg_name}.egg-info
# rename package to use a -
sed -i 's/%{pypi_name}/%{pkg_name}/' setup.cfg
# disable flake8 in the tests, need a newer version of pytest-flake8
# https://src.fedoraproject.org/rpms/python-pytest-flake8/pull-request/2
# AttributeError: 'Application' object has no attribute 'make_notifier'
sed -i 's/ --flake8//' pytest.ini

%build
%py3_build
%if %{with docs}
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
# These excludes are provided by python3-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*
%{python3_sitelib}/jaraco
%{python3_sitelib}/jaraco_classes-%{version}-py?.?.egg-info

%if %{with docs}
%files -n python-%{pkg_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Dan Radez <dradez@redhat.com> - 2.0-2
- fixed egg info

* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 2.0-1
- Initial package.