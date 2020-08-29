# Created by pyp2rpm-3.3.4
%global pypi_name pre-commit

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        0%{?dist}
Summary:        A framework for managing and maintaining multi-language pre-commit hooks

License:        MIT
URL:            https://github.com/pre-commit/pre-commit
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/pre_commit-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
[![Build Status]( [![Azure DevOps coverage]( pre-commitA framework for managing
and maintaining multi-language pre-commit hooks.For more information see:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aspy.yaml)
Requires:       python3dist(cfgv) >= 2
Requires:       python3dist(identify) >= 1
Requires:       python3dist(importlib-metadata)
Requires:       python3dist(importlib-resources)
Requires:       python3dist(nodeenv) >= 0.11.1
Requires:       python3dist(pyyaml)
Requires:       python3dist(setuptools)
Requires:       python3dist(toml)
# Loosen up, backporting ivrtualenv to RHEL 8 runs indo modular dependencies
#Requires:       python3dist(virtualenv) >= 15.2
Requires:       python3dist(virtualenv)
%description -n python3-%{pypi_name}
[![Build Status]( [![Azure DevOps coverage]( pre-commitA framework for managing
and maintaining multi-language pre-commit hooks.For more information see:


%prep
%autosetup -n pre_commit-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if 0%{?rhel}
grep -rl 'virtualenv>=' . | while read name; do
    echo Roll back virtualenv requirement on for RHEL in: $name
    sed -i.bak 's/virtualenv>=.*/virtualenv/g' $name
done
%endif

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/pre-commit
%{_bindir}/pre-commit-validate-config
%{_bindir}/pre-commit-validate-manifest
%{python3_sitelib}/pre_commit
%{python3_sitelib}/pre_commit-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Aug 24 2020 Koji Builder <koji@dummy.lan> - 2.0.0-1
- Initial package.
