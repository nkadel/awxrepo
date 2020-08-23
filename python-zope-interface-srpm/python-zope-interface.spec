# Created by pyp2rpm-3.3.4
%global srcname zope.interface
%global pypi_name zope-interface

Name:           python-%{pypi_name}
Version:        5.0.0
Release:        0%{?dist}
Summary:        Interfaces for Python

License:        ZPL 2.1
URL:            https://github.com/zopefoundation/zope.interface
Source0:        %{pypi_source}

BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage) >= 5.0.3
BuildRequires:  python3dist(coverage) >= 5.0.3
BuildRequires:  python3dist(coverage) >= 5.0.3
BuildRequires:  python3dist(repoze.sphinx.autointerface)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(zope.event)
BuildRequires:  python3dist(zope.event)
BuildRequires:  python3dist(zope.event)
BuildRequires:  python3dist(zope.testing)
BuildRequires:  python3dist(zope.testing)
BuildRequires:  python3dist(zope.testing)
BuildRequires:  python3dist(sphinx)

%description
 zope.interface :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(coverage) >= 5.0.3
Requires:       python3dist(coverage) >= 5.0.3
Requires:       python3dist(repoze.sphinx.autointerface)
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)
Requires:       python3dist(zope.event)
Requires:       python3dist(zope.event)
Requires:       python3dist(zope.testing)
Requires:       python3dist(zope.testing)
%description -n python3-%{pypi_name}
 zope.interface :target:

%package -n python-%{pypi_name}-doc
Summary:        zope.interface documentation
%description -n python-%{pypi_name}-doc
Documentation for zope.interface

%prep
%autosetup -n %{pkg_name}-%{version}
# Remove bundled egg-info
rm -rf %{pkg_name}.egg-info

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
%license LICENSE.txt
%doc README.rst docs/README.rst docs/README.ru.rst
%{python3_sitearch}/zope
%{python3_sitearch}/%{pkg_name}-%{version}-py%{python3_version}-*.pth
%{python3_sitearch}/%{pkg_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Sun Aug 23 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 5.0.0-1
- Initial package.
