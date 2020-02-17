%global pypi_name pluggy

Name:           python-pluggy
Version:        0.6.0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        The plugin manager stripped of pytest specific details

License:        MIT
URL:            https://github.com/pytest-dev/pluggy
Source0:        https://github.com/pytest-dev/%{pypi_name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz


%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
The plugin manager stripped of pytest specific details.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:  The plugin manager stripped of pytest specific details.

%description -n python%{python3_pkgversion}-%{pypi_name}
The plugin manager stripped of pytest specific details.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} -m pytest testing


%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%doc README.rst
%license LICENSE


%changelog
* Fri Jul 13 2018 Petr Viktorin <pviktori@redhat.com> - 0.6.0-3
- Remove the Python 2 subpackage
  https://bugzilla.redhat.com/show_bug.cgi?id=1590435

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Matthias Runge <mrunge@redhat.com> - 0.6.0-1
- update to 0.6.0
- requirement renames to meet python2 names

* Tue Jan 23 2018 Karsten Hopp <karsten@redhat.com> - 0.3.1-10
- fix conditional

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.1-9
- Python 2 binary package renamed to python2-pluggy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Matthias Runge <mrunge@redhat.com> - 0.3.1-3
- make tests pass again on Python 3.5

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 21 2015 Matthias Runge <mrunge@redhat.com> - 0.3.1-1
- update to 0.3.1

* Tue Aug 25 2015 Matthias Runge <mrunge@redhat.com> - 0.3.0-3
- fix python3 builds

* Fri Aug 21 2015 Matthias Runge <mrunge@redhat.com> - 0.3.0-2
- add python2_sitelib macros and BR to setuptools (rhbz#1254484)

* Fri Aug 14 2015 Matthias Runge <mrunge@redhat.com> - 0.3.0-1
- version based on the inital proposal of Adam Young
