# Created by pyp2rpm-3.3.4
%global pypi_name coverage

Name:           python-%{pypi_name}
Version:        5.0.3
Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Code coverage measurement for Python

License:        Apache 2.0
URL:            https://github.com/nedbat/coveragepy
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toml)
BuildRequires:  python3dist(sphinx)

# Added manually
BuildRequires:  python3dist(sphinxcontrib-spelling)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-rst-builder)
BuildRequires:  python3dist(sphinx-tabs)
# Embedded requirement, added here manually
BuildRequires:  python3dist(pre-commit) = 2.0.0

%description
Coverage.py is a Python 3 module that measures code coverage during Python
execution. It uses the code analysis tools and tracing hooks provided in the 
Python standard library to determine which lines are executable, and which 
have been executed.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
Requires:       python3dist(toml)

%description -n python3-%{pypi_name}
Coverage.py is a Python 3 module that measures code coverage during Python
execution. It uses the code analysis tools and tracing hooks provided in the 
Python standard library to determine which lines are executable, and which 
have been executed.

%package -n python-%{pypi_name}-doc
Summary:        coverage documentation

%description -n python-%{pypi_name}-doc
Documentation for coverage

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc ci/README.txt tests/gold/README.rst README.rst
%{_bindir}/coverage
%{_bindir}/coverage-3.6
%{_bindir}/coverage3
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Sun Aug 23 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 5.0.3-1
- Initial package.
