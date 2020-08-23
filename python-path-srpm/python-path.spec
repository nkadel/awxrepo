%global with_python3 1
%global with_python2 0

%global pypi_name path

# Disable tests
%bcond_with tests

Name:           python-%{pypi_name}
Version:        5.2
#Release:        17%%{?dist}
Release:        0%{?dist}
Summary:        A python module wrapper for os.path

License:        MIT
URL:            https://pypi.python.org/pypi/path.py
Source0:        %{pypi_source %{pypi_name} %{version} zip}

BuildArch:      noarch

%if 0%{rhel}
BuildRequires:  epel-rpm-macros
%endif

%if %{with_python2}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  %{_bindir}/py.test-%{python3_version}
%endif
%endif

%if %{with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  %{_bindir}/py.test-%{python3_version}
%endif
%endif

%description
path.py implements a path objects as first-class entities,
allowing common operations on files to be invoked on those path objects directly.

See documentation here http://amoffat.github.io/sh/.

%if %{with_python2}
%package    -n python2-%{pypi_name}
Summary:    Python 2 module wrapper for os.path
%{?python_provide:%python_provide python2-%{pypi_name}}
%description -n python2-%{pypi_name}
path.py implements a path objects as first-class entities,
allowing common operations on files to be invoked on those path objects directly.

See documentation here http://amoffat.github.io/sh/.
%endif

%if %{with_python3}
%package    -n python%{python3_pkgversion}-%{pypi_name}
Summary:    Python 3 module wrapper for os.path
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
path.py implements a path objects as first-class entities,
allowing common operations on files to be invoked on those path objects directly.

See documentation here http://amoffat.github.io/sh/.
%endif


%prep
%setup -q -n %{pypi_name}.py-%{version}
sed -i 's/\[pytest\]/\[tool:pytest\]/' setup.cfg

%build
%if %{with_python3}
%py3_build
%endif

%if %{with_python2}
%py2_build
%endif

%if %{with tests}
%check
%if %{with_python2}
pushd build/lib
   LC_ALL=C.UTF-8 py.test-%{python2_version} -v
   popd
%endif

%if %{with_python3}
pushd build/lib
    py.test-%{python3_version} -v
popd
%endif
%endif # with tests

%install
%if %{with_python3}
%py3_install
%endif

%if %{with_python2}
%py2_install
%endif


%if %{with_python2}
%files -n python2-path
%doc CHANGES.rst README.rst
%{python2_sitelib}/path.py
%{python2_sitelib}/path.pyc
%{python2_sitelib}/path.pyo
%{python2_sitelib}/path.py-%{version}-py?.?.egg-info/
%{python2_sitelib}/test_path.py*
%endif

%if %{with_python3}
%files -n python%{python3_pkgversion}-path
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/path.py
%{python3_sitelib}/path.py-%{version}-py?.?.egg-info/
%{python3_sitelib}/test_path.py
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2-15
- Drop explicit locale setting for python3, use C.UTF-8 for python2
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 5.2-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 5.2-11
- Update conditional

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Thomas Spura <tomspur@fedoraproject.org> - 5.2-8
- rename python-* to python2-*
- expand %%files
- use py_build/install macros

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.2-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Orion Poplawski <orion@cora.nwra.com> - 5.2-4
- Fix py.test call for python3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep  3 2014 Thomas Spura <tomspur@fedoraproject.org> - 5.2-2
- enable testsuite

* Wed Sep  3 2014 Thomas Spura <tomspur@fedoraproject.org> - 5.2-1
- update to 5.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Apr 04 2014 Xavier Lamien <laxathom@fedoraproject.org> - 5.1-1
- Upstream release.
- Add python3's subpackage.

* Fri Jul 26 2013 Xavier Lamien <laxathom@fedoraproject.org> - 4.3-1
- Upstream release.

* Wed Apr 10 2013 Xavier Lamien <laxathom@fedoraproject.org> - 3.0.1-2
- Add %%check stage.
- Update BuildRequire.
- Add missing %%docs.

* Wed Apr 10 2013 Xavier Lamien <laxathom@fedoraproject.org> - 3.0.1-1
- Initial RPM release.
