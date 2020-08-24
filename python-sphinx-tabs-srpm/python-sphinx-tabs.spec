# Created by pyp2rpm-3.3.4
%global pypi_name sphinx-tabs

Name:           python-%{pypi_name}
Version:        1.2.1
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Tabbed views for Sphinx

License:        MIT
URL:            https://github.com/executablebooks/sphinx-tabs
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 sphinx-tabs[![Github-CI][github-ci]][github-link] [![Coverage Status][codecov-
badge]][codecov-link] [![PyPI][pypi-badge]][pypi-link]Create tabbed content in
[Sphinx documentation]() when building HTML.For example, see the [Raw] code of
[docs/index.rst](docs/index.rst) which generates the following:A live demo can
be found here: <>![Tabs](/images/tabs.gif) Installationbash pip install
sphinx-...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(coverage)
Requires:       python3dist(lxml)
#Requires:       python3dist(pre-commit) = 2.6
Requires:       python3dist(pre-commit) = 2.0.0
Requires:       python3dist(pygments)
Requires:       (python3dist(pytest) >= 3.6 with python3dist(pytest) < 4)
Requires:       python3dist(pytest-cov)
Requires:       (python3dist(sphinx) >= 2 with python3dist(sphinx) < 4)
Requires:       python3dist(sphinx-testing)
%description -n python3-%{pypi_name}
 sphinx-tabs[![Github-CI][github-ci]][github-link] [![Coverage Status][codecov-
badge]][codecov-link] [![PyPI][pypi-badge]][pypi-link]Create tabbed content in
[Sphinx documentation]() when building HTML.For example, see the [Raw] code of
[docs/index.rst](docs/index.rst) which generates the following:A live demo can
be found here: <>![Tabs](/images/tabs.gif) Installationbash pip install
sphinx-...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE sphinx_tabs/semantic-ui-2.4.1/LICENSE.md
%doc README.md
%{python3_sitelib}/sphinx_tabs
%{python3_sitelib}/sphinx_tabs-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 24 2020 Koji Builder <koji@dummy.lan> - 1.2.1-1
- Initial package.
