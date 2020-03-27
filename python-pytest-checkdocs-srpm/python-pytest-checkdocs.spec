# Created by pyp2rpm-3.3.3
%global pypi_name pytest-checkdocs

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
BuildConflicts: pytnon%{python3_pkgversion}-pytest = 3.7.3
BuildRequires:  pytnon%{python3_pkgversion}-docutils >= 0.15
BuildRequires:  pytnon%{python3_pkgversion}-importlib-metadata >= 0.21
BuildRequires:  pytnon%{python3_pkgversion}-jaraco-packaging >= 3.2
BuildRequires:  pytnon%{python3_pkgversion}-more-itertools
BuildRequires:  pytnon%{python3_pkgversion}-pytest >= 3.5
BuildRequires:  pytnon%{python3_pkgversion}-pytest-black-multipy
BuildRequires:  pytnon%{python3_pkgversion}-pytest-checkdocs
BuildRequires:  pytnon%{python3_pkgversion}-pytest-cov
BuildRequires:  pytnon%{python3_pkgversion}-pytest-flake8)
BuildRequires:  pytnon%{python3_pkgversion}-rst-linker >= 1.9
BuildRequires:  pytnon%{python3_pkgversion}-setuptools
BuildRequires:  pytnon%{python3_pkgversion}-setuptools-scm >= 1.15.0
BuildRequires:  pytnon%{python3_pkgversion}-sphinx

%description
A pytest plugin that checks the long description of the project to ensure it
renders properly.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Conflicts:      pytnon%{python3_pkgversion}-pytest = 3.7.3
Requires:       pytnon%{python3_pkgversion}-docutils >= 0.15
Requires:       pytnon%{python3_pkgversion}-importlib-metadata >= 0.21
Requires:       pytnon%{python3_pkgversion}-jaraco-packaging >= 3.2
Requires:       pytnon%{python3_pkgversion}-more-itertools
Requires:       pytnon%{python3_pkgversion}-pytest) >= 3.5
Requires:       pytnon%{python3_pkgversion}-pytest-black-multipy
Requires:       pytnon%{python3_pkgversion}-pytest-checkdocs
Requires:       pytnon%{python3_pkgversion}-pytest-cov
Requires:       pytnon%{python3_pkgversion}-pytest-flake8
Requires:       pytnon%{python3_pkgversion}-rst-linker >= 1.9
Requires:       pytnon%{python3_pkgversion}-setuptools)
Requires:       pytnon%{python3_pkgversion}-sphinx)
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
# rename jaraco dependencies to use a -
sed -i 's/^\tjaraco\./	jaraco-/' setup.cfg
# rename rst.linker  dependencies to use a -
sed -i 's/^\trst.linkder/	rst-linker/' setup.cfg

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_checkdocs.py
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/pytest_checkdocs-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Mar 16 2020 Nico Kadel-Garcia <nico.kadel-garcia@cengage.com> - 1.2.3-1
- Initial package.
