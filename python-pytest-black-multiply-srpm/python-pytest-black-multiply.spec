# Created by pyp2rpm-3.3.3
%global pypi_name pytest-black-multipy

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        0%{?dist}
Summary:        Allow '--black' on older Pythons

License:        None
URL:            https://github.com/jaraco/skeleton
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15.0
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(jaraco-packaging) >= 3.2

%description
.. .. .. .. :target:

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Conflicts:      python3dist(pytest) = 3.7.3
Requires:       python3dist(jaraco-packaging) >= 3.2
Requires:       python3dist(pytest) >= 3.5
Requires:       python3dist(pytest-black)
Requires:       python3dist(pytest-checkdocs)
Requires:       python3dist(pytest-flake8)
Requires:       python3dist(rst-linker) >= 1.9
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)
%description -n python%{python3_pkgversion}-%{pypi_name}
.. .. .. .. :target:

%package -n python-%{pypi_name}-doc
Summary:        pytest-black-multipy documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest-black-multipy

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

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_black_multipy
%{python3_sitelib}/pytest_black_multipy-%{version}-py%{python3_version}.egg-info
# These excludes are provided by python3-jaraco
%exclude %{python3_sitelib}/jaraco/__init__*
%exclude %{python3_sitelib}/jaraco/__pycache__/__init__*

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Mar 16 2020 Nico Kadel-Garcia <nico.kadel-garcia@cengage.com> - 1.0.0-1
- Initial package.
