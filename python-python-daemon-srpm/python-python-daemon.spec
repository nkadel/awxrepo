# Created by pyp2rpm-3.3.4
%global pypi_name python-daemon

Name:           python-%{pypi_name}
Version:        2.2.4
Release:        0%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

License:        Apache-2
URL:            https://pagure.io/python-daemon/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(lockfile) >= 0.10
BuildRequires:  python3dist(mock) >= 1.3
BuildRequires:  python3dist(mock) >= 1.3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(testscenarios) >= 0.4
BuildRequires:  python3dist(testscenarios) >= 0.4
BuildRequires:  python3dist(testtools)
BuildRequires:  python3dist(testtools)
BuildRequires:  python3dist(twine)
BuildRequires:  python3dist(unittest2) >= 0.5.1
BuildRequires:  python3dist(unittest2) >= 0.5.1

%description
This library implements the well-behaved daemon specification of :pep:3143,
“Standard daemon process library”.A well-behaved Unix daemon process is tricky
to get right, but the required steps are much the same for every daemon
program. A DaemonContext instance holds the behaviour and configured process
environment for the program; use the instance as a context manager to enter a
daemon...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(coverage)
Requires:       python3dist(docutils)
Requires:       python3dist(docutils)
Requires:       python3dist(lockfile) >= 0.10
Requires:       python3dist(mock) >= 1.3
Requires:       python3dist(setuptools)
Requires:       python3dist(testscenarios) >= 0.4
Requires:       python3dist(testtools)
Requires:       python3dist(unittest2) >= 0.5.1
%description -n python3-%{pypi_name}
This library implements the well-behaved daemon specification of :pep:3143,
“Standard daemon process library”.A well-behaved Unix daemon process is tricky
to get right, but the required steps are much the same for every daemon
program. A DaemonContext instance holds the behaviour and configured process
environment for the program; use the instance as a context manager to enter a
daemon...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.ASF-2 LICENSE.GPL-3
%{python3_sitelib}/daemon
%{python3_sitelib}/python_daemon-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Aug 22 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 2.2.4-1
- Initial package.
