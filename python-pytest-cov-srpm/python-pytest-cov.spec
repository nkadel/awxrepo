%global srcname pytest-cov

Name:           python-%{srcname}
Version:        2.7.1
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        Pytest plugin for coverage reporting

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/pytest-dev/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Py.test plugin for coverage reporting with support for both centralised and
distributed testing, including subprocesses and multiprocessing for Python.


%package -n python2-%{srcname}
Summary:        Pytest plugin for coverage reporting
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# For tests
#  Not packaged: python2-fields
#BuildRequires:  python2-pytest >= 3.6
#BuildRequires:  python2-coverage >= 4.4
#BuildRequires:  python2-fields
#BuildRequires:  python2-process-tests
#BuildRequires:  python2-six
#BuildRequires:  python2-virtualenv
#BuildRequires:  python2-pytest-xdist
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Py.test plugin for coverage reporting with support for both centralised and
distributed testing, including subprocesses and multiprocessing for Python 2.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Pytest plugin for coverage reporting
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.6
BuildRequires:  python%{python3_pkgversion}-coverage >= 4.4
# For tests
BuildRequires:  python%{python3_pkgversion}-fields
BuildRequires:  python%{python3_pkgversion}-process-tests
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-virtualenv
BuildRequires:  python%{python3_pkgversion}-pytest-xdist
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Py.test plugin for coverage reporting with support for both centralised and
distributed testing, including subprocesses and multiprocessing for Python 3.


%prep
%setup -q -n %{srcname}-%{version}
rm -rf *.egg-info


%build
%py2_build
%py3_build


%install
%py3_install
%py2_install


%check
# Python 2 tests have unpackaged dependencies
# test_dist_missing_data needs internet
# test_central_subprocess/dist_subprocess https://github.com/pytest-dev/pytest-cov/issues/90
# test_subprocess_with_path_aliasing and test_dist_combine_racecondition tries to match strings and fails, mostly version mismatch
# test_multiprocessing_pool{,_terminate, _close} cause deadlock on Python 3.8 - https://github.com/pytest-dev/pytest-cov/issues/295
# To read a custom pth-file we need to add that path to site-dir, needed for tests at RPM build time                                   
echo "import site;site.addsitedir(\"$(pwd)/src\")" > tests/sitecustomize.py        
export PYTHONPATH="$(pwd)"/tests                                                
py.test-%{python3_version} -vv \
    -k "not test_dist_missing_data and not test_subprocess_with_path_aliasing and not test_dist_combine_racecondition and not central_subprocess and not dist_subprocess \
        and not test_multiprocessing_pool and not test_multiprocessing_pool_terminate and not test_multiprocessing_pool_close"


%files -n python2-%{srcname}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst README.rst
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst README.rst
%{python3_sitelib}/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Lumír Balhar <lbalhar@redhat.com> - 2.7.1-2
- Skip three tests (multiprocessing_pool) to fix FTBFS with Python 3.8

* Sun May  5 2019 Orion Poplawski <orion@nwra.com> - 2.7.1-1
- Update to 2.7.1

* Thu Apr 04 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6.1-1
- Update to 2.6.1 for pytest 4 compatibility

* Tue Feb 12 2019 Orion Poplawski <orion@nwra.com> - 2.6.0-3
- Build with pytest-xdist

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 2.6.0-1
- Update to 2.6.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 2.5.1-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 9 2017 Orion Poplawski <orion@cora.nwra.com> - 2.5.1-3
- Ship python2-pytest-cov

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 12 2017 Orion Poplawski <orion@cora.nwra.com> - 2.5.1-1
- Update to 2.5.1

* Wed May 10 2017 Orion Poplawski <orion@cora.nwra.com> - 2.5.0-1
- Update to 2.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 2.4.0-2
- Rebuild for Python 3.6

* Mon Oct 10 2016 Orion Poplawski <orion@cora.nwra.com> - 2.4.0-1
- Update to 2.4.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 7 2016 Orion Poplawski <orion@cora.nwra.com> - 2.3.0-1
- Update to 2.3.0

* Mon May 23 2016 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-1
- Ignore failing tests

* Sat Feb 13 2016 Orion Poplawski <orion@cora.nwra.com> - 2.2.1-1
- Update to 2.2.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 2.2.0-2
- Rebuilt for Python3.5 rebuild
- Skip tests for a python3 rebuild as it seems to be env failure

* Mon Oct 5 2015 Orion Poplawski <orion@cora.nwra.com> - 2.2.0-1
- Update to 2.2.0

* Mon Sep 14 2015 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-2
- Modernize spec
- Run tests properly, skipping xdist tests for now

* Mon Sep 14 2015 Tomas Tomecek <ttomecek@redhat.com> - 2.1.0-1
- upstream release 2.1.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 1.6-2
- Rebuild for Python 3.4

* Tue Feb 25 2014 Orion Poplawski <orion@cora.nwra.com> - 1.6-1
- Initial package
