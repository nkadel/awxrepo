%global pypi_name fixtures
%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        12%{?dist}
Summary:        Fixtures, reusable state for writing clean tests and more

License:        ASL 2.0 or BSD
URL:            https://launchpad.net/python-fixtures
Source0:        https://pypi.python.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-pbr >= 0.11

# Requirements
BuildRequires:  python2-mock
BuildRequires:  python2-testtools >= 0.9.22

%global _description\
Fixtures defines a Python contract for reusable state / support logic,\
primarily for unit testing. Helper and adaption logic is included to\
make it easy to write your own fixtures using the fixtures contract.\
Glue code is provided that makes using fixtures that meet the Fixtures\
contract in unit test compatible test cases easy and straight forward.

%description %_description

%package -n python2-%{pypi_name}
Summary: %summary
Requires:       python2-testtools >= 0.9.22
Requires:       python2-six
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name} %_description

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Fixtures, reusable state for writing clean tests and more
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pbr >= 0.11

# Requirements
BuildRequires:  python3-mock
BuildRequires:  python3-testtools >= 0.9.22

Requires:       python3-testtools >= 0.9.22
Requires:       python3-six
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Fixtures defines a Python contract for reusable state / support logic,
primarily for unit testing. Helper and adaption logic is included to
make it easy to write your own fixtures using the fixtures contract.
Glue code is provided that makes using fixtures that meet the Fixtures
contract in unit test compatible test cases easy and straight forward.

%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} -m testtools.run fixtures.test_suite
%if 0%{?with_python3}
%{__python3} -m testtools.run fixtures.test_suite
%endif

%files -n python2-%{pypi_name}
%doc README GOALS NEWS Apache-2.0 BSD COPYING
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README GOALS NEWS Apache-2.0 BSD COPYING
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-10
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.0-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 3.0.0-7
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.0-6
- Python 2 binary package renamed to python2-fixtures
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 21 2016 Matthias Runge <mrunge@redhat.com> - 3.0.0-1
- update to 3.0.0 (rhbz#1281945)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Paul Belanger <pabelanger@redhat.com> 1.4.0-1
- New upstream 1.4.0 release
- Update spec file latest python support
- Fix bogus date warning
- rpmlint warnings

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.14-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Mar 24 2014 Matthias Runge <mrunge@redhat.com> - 0.3.14-1
- update to 0.3.14

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Matthias Runge <mrunge@redhat.com> - 0.3.12-3
- enable python3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 1 2013 Pádraig Brady <P@draigBrady.com> - 0.3.12-1
- Update to 0.3.12

* Fri Nov 16 2012 Pádraig Brady <P@draigBrady.com> - 0.3.9-4
- Update changelog

* Fri Nov 16 2012 Pádraig Brady <P@draigBrady.com> - 0.3.9-3
- Fix License:

* Thu Nov 15 2012 Pádraig Brady <P@draigBrady.com> - 0.3.9-2
- Remove version dependency on python-testtools (assume always >= 0.9.12)
- BuildRequire python2-devel rather than python-devel
- Adjust License:

* Wed Nov 14 2012 Pádraig Brady <P@draigBrady.com> - 0.3.9-1
- Initial package
