# Created by pyp2rpm-3.3.4
%global pypi_name sphinxcontrib-spelling

Name:           python-%{pypi_name}
Version:        5.3.0
Release:        0%{?dist}
Summary:        Sphinx spelling extension

License:        None
URL:            https://github.com/sphinx-contrib/spelling
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  (python3dist(coverage) >= 4 with (python3dist(coverage) < 4.4 or python3dist(coverage) > 4.4))
BuildRequires:  python3dist(fixtures) >= 3
BuildRequires:  python3dist(flake8) = 3.8.2
BuildRequires:  python3dist(importlib-metadata) >= 1.7
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(pyenchant) >= 3.1.1
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(reno)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx) >= 3
BuildRequires:  python3dist(sphinx)

%description
.. -*- mode: rst -*- sphinxcontrib-spelling This package contains
sphinxcontrb.spelling, a spelling checker for Sphinx-based documentation. It
uses PyEnchant_ to produce a report showing misspelled words.Refer to the main
documentation page < for installation and setup details.License Copyright Doug
Hellmann, All Rights ReservedPermission to use, copy, modify, and distribute
this software and...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(coverage) >= 4 with (python3dist(coverage) < 4.4 or python3dist(coverage) > 4.4))
Requires:       python3dist(fixtures) >= 3
Requires:       python3dist(flake8) = 3.8.2
Requires:       python3dist(importlib-metadata) >= 1.7
Requires:       python3dist(pyenchant) >= 3.1.1
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(reno)
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx) >= 3
%description -n python3-%{pypi_name}
.. -*- mode: rst -*- sphinxcontrib-spelling This package contains
sphinxcontrb.spelling, a spelling checker for Sphinx-based documentation. It
uses PyEnchant_ to produce a report showing misspelled words.Refer to the main
documentation page < for installation and setup details.License Copyright Doug
Hellmann, All Rights ReservedPermission to use, copy, modify, and distribute
this software and...

%package -n python-%{pypi_name}-doc
Summary:        sphinxcontrib-spelling documentation
%description -n python-%{pypi_name}-doc
Documentation for sphinxcontrib-spelling

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

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_spelling-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sun Aug 23 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 5.3.0-1
- Initial package.
