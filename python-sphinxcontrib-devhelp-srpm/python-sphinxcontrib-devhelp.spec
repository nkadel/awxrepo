# Created by pyp2rpm-3.3.4
%global pypi_name sphinxcontrib-devhelp

# when bootstrapping sphinx, we cannot run tests yet
%bcond_without check

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        0%{?dist}
Summary:        sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document

License:        BSD
URL:            http://sphinx-doc.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils-stubs)
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(mypy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%if %{with check}
BuildRequires:  python3dist(sphinx) >= 1:2
BuildRequires:  python3dist(sphinx)
%endif

%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(docutils-stubs)
Requires:       python3dist(flake8)
Requires:       python3dist(mypy)
Requires:       python3dist(pytest)
%description -n python3-%{pypi_name}
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp document.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%if %{with check}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_devhelp-%{version}-py%{python3_version}.egg-info
# Why are these being generated???
%{python3_sitelib}/sphinxcontrib_devhelp-%{version}-py%{python3_version}-nspkg.pth

%changelog
* Sun Aug 23 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 1.0.2-1
- Initial package.
