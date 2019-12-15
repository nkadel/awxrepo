%global with_python3 1

Name:           python-gitdb
Version:        0.6.4
Release:        4%{?dist}
Summary:        A pure-Python git object database

Group:          Development/Languages
License:        BSD
URL:            http://pypi.python.org/packages/source/g/gitdb/gitdb-%{version}.tar.gz#md5=44e4366b8bdfd306b075c3a52c96ae1a
Source0:        gitdb-%{version}.tar.gz
Requires:       python-smmap

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python2-devel
BuildRequires:  python2-nose
BuildRequires:  python2-setuptools

%description
GitDB allows you to access bare git repositories for reading and writing. It
aims at allowing full access to loose objects as well as packs with performance
and scalability in mind. It operates exclusively on streams, allowing to
operate on large objects with a small memory footprint.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-gitdb
Summary:        Python3 Git Library
Requires:       python%{python3_pkgversion}-smmap
BuildRequires:  python%{python3_pkgversion}-devel
Buildrequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-gitdb
%{description}
%endif

# Filter the private provide
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/gitdb/_perf.so
%filter_setup
}

%prep
%setup -qc -n gitdb-%{version}
mv gitdb-%{version} python2

%if 0%{?with_python3}
cp -a python2 python3
find python3 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find python2 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

pushd python2
cp AUTHORS LICENSE ../
popd

%build
pushd python2
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
popd

%if 0%{?with_python3}
pushd python3
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif

%install
pushd python2
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
chmod 0755 %{buildroot}%{python2_sitearch}/gitdb/_perf.so
popd
%if 0%{?with_python3}
pushd python3
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif

%files
%defattr(-,root,root,-)
%if 0%{?fedora}
%license LICENSE
%else
%doc LICENSE
%endif
%doc AUTHORS
%{python2_sitearch}/gitdb-%{version}-py?.?.egg-info
%{python2_sitearch}/gitdb/

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-gitdb
%license LICENSE
%doc AUTHORS
%{python3_sitearch}/gitdb-%{version}-py?.?.egg-info
%{python3_sitearch}/gitdb/
%endif

%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Dennis Gilmore <dennis@ausil.us> - 0.6.4-1
- update to 0.6.4
- enable python3 support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Jesse Keating <jkeating@redhat.com> - 0.5.4-2
- Require python-smmap

* Mon Jul 18 2011 Jesse Keating <jkeating@redhat.com> - 0.5.4-1
- Upstream release to fix licensing issues
- Use real upstream release instead of git checkout
- No tests shipped in release, remove %check

* Tue Jun 14 2011 Jesse Keating <jkeating@redhat.com> - 0.5.2-3.20110613git17d9d13
- Add a br on python-async

* Mon Jun 13 2011 Jesse Keating <jkeating@redhat.com> - 0.5.2-2.20110613git17d9d13
- Fix perms and add a date to the release field.

* Sat May 28 2011 Jesse Keating <jkeating@redhat.com> - 0.5.2-1.git17d9d13
- Initial package

