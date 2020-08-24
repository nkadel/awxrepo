# Created by pyp2rpm-3.3.4
%global pypi_name mypy

Name:           python-%{pypi_name}
Version:        0.782
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Optional static typing for Python

License:        MIT License
URL:            http://www.mypy-lang.org/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(mypy-extensions) >= 0.4.3 with python3dist(mypy-extensions) < 0.5)
BuildRequires:  python3dist(psutil) >= 4
BuildRequires:  python3dist(setuptools)
BuildRequires:  (python3dist(typed-ast) >= 1.4 with python3dist(typed-ast) < 1.5)
BuildRequires:  python3dist(typing-extensions) >= 3.7.4
BuildRequires:  python3dist(sphinx)

%description
Mypy -- Optional Static Typing for Python Add type annotations to your Python
programs, and use mypy to type check them. Mypy is essentially a Python linter
on steroids, and it can catch many programming errors by analyzing your
program, without actually having to run it. Mypy has a powerful type system
with features such as type inference, gradual typing, generics and union

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(mypy-extensions) >= 0.4.3 with python3dist(mypy-extensions) < 0.5)
Requires:       python3dist(psutil) >= 4
Requires:       python3dist(setuptools)
Requires:       (python3dist(typed-ast) >= 1.4 with python3dist(typed-ast) < 1.5)
Requires:       python3dist(typing-extensions) >= 3.7.4
%description -n python3-%{pypi_name}
Mypy -- Optional Static Typing for Python Add type annotations to your Python
programs, and use mypy to type check them. Mypy is essentially a Python linter
on steroids, and it can catch many programming errors by analyzing your
program, without actually having to run it. Mypy has a powerful type system
with features such as type inference, gradual typing, generics and union

%package -n python-%{pypi_name}-doc
Summary:        mypy documentation
%description -n python-%{pypi_name}-doc
Documentation for mypy

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# Tests fail on zlib, we do not care
#%check
#%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE mypyc/external/googletest/LICENSE
%doc README.md docs/README.md test-data/packages/modulefinder/readme.txt test-data/samples/readme.txt test-data/unit/README.md
%{_bindir}/dmypy
%{_bindir}/mypy
%{_bindir}/mypyc
%{_bindir}/stubgen
%{_bindir}/stubtest
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/mypyc
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE mypyc/external/googletest/LICENSE

%changelog
* Sun Aug 23 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 0.782-1
- Initial package.
