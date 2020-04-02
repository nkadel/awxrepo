# Created by pyp2rpm-3.3.3
%global pypi_name pytest-checkdocs
%global mod_name pytest_checkdocs

Name:           python-%{pypi_name}
Version:        1.2.3
Release:        1%{?dist}
Summary:        check the README when running tests

License:        None
URL:            https://github.com/jaraco/pytest-checkdocs
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python%{python3_pkgversion}-devel
# Ignore this, it is unnecessary and confusing
#BuildConflicts: python3dist(pytest) = 3.7.3
# Dependencies get weird with 0.15, which has modular python3-docutils
BuildRequires:  python3dist(docutils) >= 0.15
BuildRequires:  python3dist(importlib-metadata) >= 0.21
#BuildRequires:  python3dist(jaraco.packaging) >= 3.2
BuildRequires:  python3dist(jaraco-packaging) >= 3.2
BuildRequires:  python3dist(more-itertools)
BuildRequires:  python3dist(pytest) >= 3.5
# Comment out to allow circular building
#BuildRequires:  python3dist(pytest-black-multipy)
#BuildRequires:  python3dist(pytest-checkdocs)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-flake8)
#BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(rst-linker) >= 1.9
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15.0
BuildRequires:  python3dist(sphinx)

%description
A pytest plugin that checks the long description of the project to ensure it
renders properly.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

#Conflicts:      python3dist(pytest) = 3.7.3
# Dependencies get weird with 0.15
Requires:       python3dist(docutils) >= 0.15
Requires:       python3dist(importlib-metadata) >= 0.21
#Requires:       python3dist(jaraco.packaging) >= 3.2
Requires:       python3dist(jaraco-packaging) >= 3.2
Requires:       python3dist(more-itertools)
Requires:       python3dist(pytest) >= 3.5
Requires:       python3dist(pytest-black-multipy)
#Requires:       python3dist(pytest-checkdocs)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-flake8)
#Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(rst-linker) >= 1.9
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)

%description -n python%{python3_pkgversion}-%{pypi_name}
A pytest plugin that checks the long description of the project to ensure it
renders properly.

%package -n python-%{pypi_name}-doc
Summary:        pytest-checkdocs documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest-checkdocs

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# Skip this test, it breaks on docutils dependencies
#%check
#%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_checkdocs.py
#%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pytest_checkdocs-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Mar 31 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 1.2.3-1
- Initial package.
