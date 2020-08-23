%global with_python3 1
%global with_python2 0

%{!?_licensedir: %global license %%doc}

%global pypi_name contextlib2

Name:           python-%{pypi_name}
Version:        0.5.5
#Release:        9%{?dist}
Release:        0%{?dist}
Summary:        Backports and enhancements for the contextlib module

License:        Python
URL:            https://pypi.io/project/contextlib2
Source0:        %pypi_source

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%if 0%{?with_python2}
BuildRequires:  python2-devel
# needed for check: assertRaisesRegex in unittest.TestCase
BuildRequires:  python2-unittest2
%endif

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
%endif

%if 0%{?el6}
Patch0:         contextlib2-skip-tests-on-el6.patch
%endif

%global _description\
contextlib2 is a backport of the standard library's contextlib module to\
earlier Python versions.\
\
It also serves as a real world proving ground for possible future\
enhancements to the standard library version.

%description %_description

%if 0%{?with_python2}
%package -n python2-contextlib2
Summary: %summary
%{?python_provide:%python_provide python2-contextlib2}

%description -n python2-contextlib2 %_description
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-contextlib2
Summary:        Backports and enhancements for the contextlib module

%description -n python%{python3_pkgversion}-contextlib2
contextlib2 is a backport of the standard library's contextlib module to
earlier Python versions.

It also serves as a real world proving ground for possible future
enhancements to the standard library version.
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
%if 0%{?el6}
%patch0 -p1 -b skip-tests-on-el6
%endif

# Remove bundled egg-info in case it exists
rm -rf %{pypi_name}.egg-info
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%if 0%{?with_python2}
%{__python2} setup.py build
%endif
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd
%endif
%if 0%{?with_python2}
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
%endif

%check
%if 0%{?with_python2}
%{__python2} test_contextlib2.py
%endif
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} test_contextlib2.py
popd
%endif

%if 0%{?with_python2}
%files -n python2-contextlib2
%doc README.rst VERSION.txt NEWS.rst
%license LICENSE.txt
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-contextlib2
%doc README.rst VERSION.txt NEWS.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/__pycache__/%{pypi_name}*
%{python3_sitelib}/%{pypi_name}-%{version}-*
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-7
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.5-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 0.5.5-4
- Cleanup spec file conditionals

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.5-3
- Python 2 binary package renamed to python2-contextlib2
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Sander Hoentjen <sander@hoentjen.eu> - 0.5.5-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.5.4-2
- Rebuild for Python 3.6

* Tue Sep 27 2016 Ralph Bean <rbean@redhat.com> - 0.5.4-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon May 02 2016 Ralph Bean <rbean@redhat.com> - 0.5.3-1
- new version

* Fri Apr 01 2016 Sander Hoentjen <sander@hoentjen.eu> 0.5.1-1
- Update to latest upstream (#1297768)
- add BuildReq for python-unittest2 for tests to pass
- skip some tests on el6 because python-unittest2 is too old there

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- Initial package for Fedora
