# Created by pyp2rpm-3.3.4
%global pypi_name ansible-runner

Name:           python-%{pypi_name}
Version:        1.4.6
Release:        0%{?dist}
Summary:        A tool and python library to interface with Ansible

License:        Apache
URL:            https://github.com/ansible/ansible-runner
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pexpect) >= 4.5
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(python-daemon)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%description
Ansible Runner [![Documentation]( [![Code of Conduct]( [![Ansible Mailing
lists]( Runner is a tool and python library that helps when interfacing with
Ansible directly or as part of another system whether that be through a
container image interface, as a standalone tool, or as a Python module that can
be imported. The goal is to provide a stable and consistent interface
abstraction to Ansible.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pexpect) >= 4.5
Requires:       python3dist(psutil)
Requires:       python3dist(python-daemon)
Requires:       python3dist(pyyaml)
Requires:       python3dist(setuptools)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
Ansible Runner [![Documentation]( [![Code of Conduct]( [![Ansible Mailing
lists]( Runner is a tool and python library that helps when interfacing with
Ansible directly or as part of another system whether that be through a
container image interface, as a standalone tool, or as a Python module that can
be imported. The goal is to provide a stable and consistent interface
abstraction to Ansible.


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
%license LICENSE.md
%doc README.md
%{_bindir}/ansible-runner
%{python3_sitelib}/ansible_runner
%{python3_sitelib}/test
%{python3_sitelib}/ansible_runner-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Aug 23 2020 Nico KAdel-Garcia <nkadel@gmail.com> - 1.4.6-1
- Initial package.
