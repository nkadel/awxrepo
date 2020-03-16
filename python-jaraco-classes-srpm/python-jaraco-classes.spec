# Created by pyp2rpm-3.3.2
%global pkg_name jaraco-classes
%global pypi_name jaraco.classes
# waiting on jaraco-packaging and rst-linker to build docs
%bcond_with doc

Name:           python-%{pkg_name}
Version:        2.0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        Utility functions for Python class constructs

License:        MIT
URL:            https://github.com/jaraco/jaraco.classes
Source0:        %{pypi_source %{pypi_name}}
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Utility functions for Python class constructs.

%package -n python%{python3_pkgversion}-%{pkg_name}
Summary:        %{summary}
Requires:       python%{python3_pkgversion}-jaraco
Requires:       python%{python3_pkgversion}-six

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15

BuildRequires:  python%{python3_pkgversion}-pytest >= 3.5
BuildRequires:  python%{python3_pkgversion}-pytest-flake8
BuildRequires:  python%{python3_pkgversion}-more-itertools

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkg_name}}

%description -n python%{python3_pkgversion}-%{pkg_name}
Utility functions for Python class constructs.

%if %{with docs}
%package -n python-%{pkg_name}-doc
Summary:        jaraco-classes documentation

BuildRequires:  python%{python3_pkgversion}-pytest-checkdocs
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-jaraco-packaging >= 3.2
BuildRequires:  python%{python3_pkgversion}-rst-linker >= 1.9

%description -n python-%{pkg_name}-doc
Documentation for jaraco-classes
%endif

%prep
%autosetup -n jaraco.classes-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# rename package to use a -
sed -i 's/%{pypi_name}/%{pkg_name}/' setup.cfg
# rename jaraco dependencies to use a -
sed -i 's/^\tjaraco\./	jaraco-/' setup.cfg
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

%files -n python%{python3_pkgversion}-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/jaraco
%{python3_sitelib}/jaraco_classes-%{version}-py?.?.egg-info
# These excludes are provided by python%%{python3_pkgversion}-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*

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
