# Created by pyp2rpm-3.3.3
%global pypi_name jaraco-stream

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        routines for dealing with data streams

License:        None
URL:            https://github.com/jaraco/jaraco.stream
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/jaraco.stream-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildConflicts: python3dist(pytest) = 3.7.3
BuildRequires:  python3dist(jaraco-packaging) >= 3.2
BuildRequires:  python3dist(more-itertools)
BuildRequires:  python3dist(pytest) >= 3.5
BuildRequires:  python3dist(pytest-black-multipy)
BuildRequires:  python3dist(pytest-checkdocs) >= 1.2.3
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(rst-linker) >= 1.9
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15.0
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx)

%description
 .. .. .. .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Conflicts:      python3dist(pytest) = 3.7.3
Requires:       python3dist(jaraco-packaging) >= 3.2
Requires:       python3dist(more-itertools)
Requires:       python3dist(pytest) >= 3.5
Requires:       python3dist(pytest-black-multipy)
Requires:       python3dist(pytest-checkdocs) >= 1.2.3
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-flake8)
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(sphinx)
%description -n python3-%{pypi_name}
 .. .. .. .. image::

%package -n python-%{pypi_name}-doc
Summary:        jaraco-stream documentation
%description -n python-%{pypi_name}-doc
Documentation for jaraco-stream

%prep
%autosetup -n jaraco.stream-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Use - rather than . in module names
sed -i 's/rst.linker/rst-linker/' setup.cfg

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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/jaraco
%{python3_sitelib}/jaraco_stream-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Mar 16 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 3.0.0-1
- Initial package.
