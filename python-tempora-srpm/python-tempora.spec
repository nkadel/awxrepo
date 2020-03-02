# Created by pyp2rpm-3.3.2
%global pypi_name tempora
%bcond_with docs

Name:           python-%{pypi_name}
Version:        1.14.1
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        Objects and routines pertaining to date and time (tempora)

License:        MIT
URL:            https://github.com/jaraco/tempora
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Objects and routines pertaining to date and time (tempora).

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-jaraco-functools >= 1.20
BuildRequires:  python%{python3_pkgversion}-pytz
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15
BuildRequires:  python%{python3_pkgversion}-six
# testing Reqs
BuildConflicts: python%{python3_pkgversion}-pytest = 3.7.3
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.5
BuildRequires:  python%{python3_pkgversion}-pytest-flake8
#BuildRequires:  python%%{python3_pkgversion}-pytest-sugar >= 0.9.1

%description -n python%{python3_pkgversion}-%{pypi_name}
Objects and routines pertaining to date and time (tempora).

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        tempora documentation

BuildRequires:  python%{python3_pkgversion}-sphinx)
BuildRequires:  python%{python3_pkgversion}-jaraco-packaging >= 3.2
BuildRequires:  python%{python3_pkgversion}-rst-linker >= 1.9

%description -n python-%{pypi_name}-doc
Documentation for tempora
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# fix jaraco deps in setup so they don't get improperly generated
sed -i 's/jaraco.functools/jaraco-functools/' setup.cfg
# disable flake8 in the tests, need a newer version of pytest-flake8
# https://src.fedoraproject.org/rpms/python-pytest-flake8/pull-request/2
# AttributeError: 'Application' object has no attribute 'make_notifier'
sed -i 's/ --flake8//' pytest.ini

%build
%py3_build
%if %{with docs}
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
# disabled for right now, need a newer version of pytest-flake8
# https://src.fedoraproject.org/rpms/python-pytest-flake8/pull-request/2
# AttributeError: 'Application' object has no attribute 'make_notifier'
LANG=C.utf-8 %{__python3} -m pytest --ignore=build

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/calc-prorate
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 22 2019 Dan Radez <dradez@redhat.com> - 1.14.1-2
- fix setup.py reqs so the RPM reqs get generated properly
* Tue Apr 02 2019 Dan Radez <dradez@redhat.com> - 1.14.1-1
- Initial package.
