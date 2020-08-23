# Created by pyp2rpm-3.3.3
%global pypi_name pytest

Name:           %{pypi_name}
Version:        3.6.4
Release:        0%{?dist}
Summary:        pytest: simple powerful testing with Python

License:        MIT license
URL:            http://pytest.org
Source0:        %pypi_source
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(atomicwrites) >= 1.0
BuildRequires:  python3dist(attrs) >= 17.4.0
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(funcsigs)
BuildRequires:  python3dist(more-itertools) >= 4.0.0
BuildRequires:  python3dist(pluggy) < 0.8
BuildRequires:  python3dist(pluggy) >= 0.5
BuildRequires:  python3dist(py) >= 1.5.0
# Assume bootstrap already occured for docs
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
# Renamed for RHEL naming scheme
#BuildRequires:  python3dist(sphinxcontrib_trio)
BuildRequires:  python3dist(sphinxcontrib-trio)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(six) >= 1.10.0
BuildRequires:  python3dist(sphinx)

%description
 .. image::

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python3dist(atomicwrites) >= 1.0
Requires:       python3dist(attrs) >= 17.4.0
Requires:       python3dist(colorama)
Requires:       python3dist(funcsigs)
Requires:       python3dist(more-itertools) >= 4.0.0
Requires:       python3dist(pluggy) < 0.8
Requires:       python3dist(pluggy) >= 0.5
Requires:       python3dist(py) >= 1.5.0
Requires:       python3dist(setuptools)
Requires:       python3dist(six) >= 1.10.0
%description -n python%{python3_pkgversion}-%{pypi_name}
 .. image::

%package -n python-%{pypi_name}-doc
Summary:        pytest documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/en html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install
mv %{buildroot}%{_bindir}/pytest %{buildroot}%{_bindir}/pytest-%{python3_version}
ln -snf pytest-%{python3_version} %{buildroot}%{_bindir}/pytest-3
mv %{buildroot}%{_bindir}/py.test %{buildroot}%{_bindir}/py.test-%{python3_version}
ln -snf py.test-%{python3_version} %{buildroot}%{_bindir}/py.test-3

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license doc/en/_themes/LICENSE doc/en/license.rst LICENSE
%doc changelog/README.rst README.rst
%{_bindir}/pytest-3
%{_bindir}/pytest-%{python3_version}
%{_bindir}/py.test-3
%{_bindir}/py.test-%{python3_version}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/_pytest
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license doc/en/_themes/LICENSE doc/en/license.rst LICENSE

%changelog
* Tue Mar 31 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 3.6.4-1
- Initial package.
