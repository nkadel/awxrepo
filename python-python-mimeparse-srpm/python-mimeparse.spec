%global pypi_name python-mimeparse

Name:           python-%{pypi_name}
Version:        1.6.0
#Release:        5%%{?dist}
Release:        0.1%{?dist}
Summary:        Python module for parsing mime-type names
License:        MIT
URL:            https://github.com/dbtsai/python-mimeparse
Source0:        %pypi_source
BuildArch:      noarch

%description
This module provides basic functions for parsing mime-type names
and matching them against a list of media-ranges.


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
# Handle EPEL snipping leading python- off package name
Provides: python%{python3_pkgversion}-mimeparse = %{version}-%{release}
Obsoletes: python%{python3_pkgversion}-mimeparse <= %{version}-%{release}


%description -n python%{python3_pkgversion}-%{pypi_name}
This module provides basic functions for parsing mime-type names
and matching them against a list of media-ranges.


%prep
%setup -q -n %{pypi_name}-%{version}


%build
%py3_build

%install
%py3_install

%check
%{__python3} -m unittest -v mimeparse_test


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*


%changelog
* Sun Dec 15 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.6.0-0
- Port to RHEL 8
- Rename to python[version]-python-mimeparse

* Fri Mar 08 2019 Troy Dawson <tdawson@redhat.com> - 1.6.0-5
- Rebuilt to change main python from 3.4 to 3.6

* Thu Sep 07 2017 Carl George <carl@george.computer> - 1.6.0-4
- Enable python34 subpackage for EPEL

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 04 2017 Carl George <carl.george@rackspace.com> - 1.6.0-2
- Spec file clean up

* Tue Feb 28 2017 Carl George <carl.george@rackspace.com> - 1.6.0-1
- New upstream https://github.com/dbtsai/python-mimeparse
- Modernize spec file per Python Packaging Guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.1.4-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 02 2015 Jan Kaluza <jkaluza@redhat.com> - 0.1.4-6
- provide python2-mimeparse (#1241680)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 18 2013 Pádraig Brady <P@draigBrady.com> - 0.1.4-1
- Update to release 0.1.4

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Jan Kaluza <jkaluza@redhat.com> - 0.1.3-2
- python3 support disabled
- removed useless spec file directives
- run upstream test

* Wed Nov 02 2011 Jan Kaluza <jkaluza@redhat.com> - 0.1.3-1
- Initial version
