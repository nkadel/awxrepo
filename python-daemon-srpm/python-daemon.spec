
%global pypi_name daemon

%global with_python3 1
%if 0%{?fedora} > 30 || %{?rhel} > 7
%global with_python2 0
%else
%global with_python2 1
%endif

Name:           python-%{pypi_name}
Version:        2.2.3
Release:        1%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

# Some build scripts and test franework are licensed GPLv3+ but htose aren't shipped
License:        ASL2.0
URL:            http://pypi.python.org/pypi/python-daemon/
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz


BuildArch:      noarch
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
%if %{with_python2}
BuildRequires:  python2
BuildRequires:  python2-devel
BuildRequires:  python2-docutils
BuildRequires:  python2-lockfile
BuildRequires:  python2-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-testscenarios
%endif
%if %{with_python3}
BuildRequires:  python%{python3_pkgversion}
BuildRequires:  python%{python3_pkgversion}-devel
Buildrequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-testscenarios
BuildRequires:  python%{python3_pkgversion}-docutils
BuildRequires:  python%{python3_pkgversion}-lockfile
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-testtools
%endif

%global _description\
This library implements the well-behaved daemon specification of PEP 3143,\
"Standard daemon process library".\
\
This is the python2 version of the library.

%description %_description

%if %{with_python2}
%package -n python2-%{pypi_name}
Summary: %summary
Requires:       python2-lockfile
Requires:       python2-docutils
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name} %_description
%endif

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Library to implement a well-behaved Unix daemon process
Requires:       python%{python3_pkgversion}-lockfile
Requires:       python%{python3_pkgversion}-docutils

%description -n python%{python3_pkgversion}-%{pypi_name}
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".

This is the python%{python3_pkgversion} version of the library.
%endif

%prep
%setup -q

%if %{with_python3}
rm -rf %{py3dir}
cp -ar . %{py3dir}
%endif

%build
%if %{with_python2}
%{__python2} setup.py build
%endif

%if %{with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if %{with_python2}
%{__python2} setup.py install --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python2_sitelib}/tests
%endif

%if %{with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python3_sitelib}/tests
popd
%endif


# Test suite requires minimock and lockfile
%check
%if %{with_python2}
PYTHONPATH=$(pwd) %{__python2} -m unittest discover || :
%endif

%if %{with_python3}
pushd %{py3dir}
PYTHONPATH=$(pwd) %{__python3} -m unittest discover || :
%endif

%if %{with_python2}
%files -n python2-%{pypi_name}
%license LICENSE.ASF-2
%{python2_sitelib}/%{pypi_name}/
%{python2_sitelib}/python_%{pypi_name}-%{version}-py%{python2_version}.egg-info/
%endif

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.ASF-2
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/python_%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%endif

%changelog
* Tue Feb 12 2019 Alfredo Moralejo <amoralej@redhat.com> - 2.2.3-1
- Update to 2.2.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-9
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.2-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 17 2017 Kevin Fenzi <kevin@scrye.com> - 2.1.2-6
- Add dep on python2-docutils. Fixes bug #1478196

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.2-5
- Python 2 binary package renamed to python2-daemon
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-2
- Rebuild for Python 3.6

* Wed Nov 09 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.2-1
- Update to 2.1.2. Fixes bug #1389593

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Apr 10 2016 Kevin Fenzi <kevin@scrye.com> - 2.1.1-1
- Update to 2.1.1. Fixes bug #1234933

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.1.0-1
- Update to newer upstream.
- Create a python3 subpackage since upstream supports it
- Note that newer upstream has relicensed to Apache 2.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug  4 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.6-7
- enable tests again as lockfile was fixed

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Kushal Das <kushal@fedoraproject.org> - 1.6-1
- New release of source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.2-1
- add missing BR: python-nose
- also add lockfile as R (bug #513546)
- update to 1.5.2

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.1-2
- add missing BR: minimock and lockfile -> testsuite works again
- remove patch, use sed instead

* Wed Oct 07 2009 Luke Macken <lmacken@redhat.com> - 1.5.1-1
- Update to 1.5.1
- Remove conflicting files (#512760)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Kushal Das <kushal@fedoraproject.org> 1.4.6-1
- Initial release

