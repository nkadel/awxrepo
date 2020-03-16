%global with_python3 1

Name:           python-jsonpickle
Version:        1.1
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        A module that allows any object to be serialized into JSON

License:        BSD
URL:            https://pypi.io/project/jsonpickle/
Source0:        https://pypi.io/packages/source/j/jsonpickle/jsonpickle-%{version}.tar.gz

%global _docdir_fmt %{name}

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
This module allows python objects to be serialized to JSON in a similar fashion
to the pickle module.

%package -n python2-jsonpickle
Summary:        A module that allows any object to be serialized into JSON
%{?python_provide:%python_provide python2-jsonpickle}

BuildRequires:  python2-devel
BuildRequires:  python2-simplejson
BuildRequires:  python2-feedparser
BuildRequires:  python2-numpy
BuildRequires:  python2-enum34
BuildRequires:  python2-demjson
Requires:       python2-simplejson

%if 0%{?fedora}
# This doesn't exist in EL7 yet...
BuildRequires:  python2-ujson
%endif

%description -n python2-jsonpickle
This module allows python objects to be serialized to JSON in a similar fashion
to the pickle module.

This is the version for Python 3.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-jsonpickle
Summary:        A module that allows any object to be serialized into JSON
%{?python_provide:%python_provide python%{python3_pkgversion}-jsonpickle}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-simplejson
BuildRequires:  python%{python3_pkgversion}-feedparser
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-bson
# https://bugzilla.redhat.com/show_bug.cgi?id=1238787
# BuildRequires:  python%{python3_pkgversion}-ujson
BuildRequires:  python%{python3_pkgversion}-demjson
Requires:       python%{python3_pkgversion}-simplejson


%description -n python%{python3_pkgversion}-jsonpickle
This module allows python objects to be serialized to JSON in a similar fashion
to the pickle module.

This is the version for Python 3.
%endif

%prep
%setup -q -n jsonpickle-%{version}
rm -r *.egg-info


%build
%{__python2} setup.py build
%if 0%{?with_python3}
%{__python3} setup.py build
%endif


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}
%if 0%{?with_python3}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
%endif


#%%check
#pushd tests
#%%{__python2} ./runtests.py
#%%{__python3} ./runtests.py
#%popd


%files -n python2-jsonpickle
%license COPYING
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-jsonpickle
%license COPYING
%{python3_sitelib}/*
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 1.1-1
- 1.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.4-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-2
- Conditionalize python3 package for EPEL7 compat.

* Thu Mar 30 2017 Ralph Bean <rbean@redhat.com> - 0.9.4-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-2
- Rebuild for Python 3.6

* Fri Dec 09 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.3-1
- 0.9.3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 23 2015 Jon Ciesla <limburgher@gmail.com> - 0.9.2-3
- Disable tests to fix build.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jul  2 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.2-1
- Update to latest version
- Clean up spec file a bit
- Add python3 subpackage (#1233915)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Jon Ciesla <limburgher@gmail.com> - 0.4.0-1
- Latest upstream release, 0.4.0.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jan 23 2010 Ben Boeckel <MathStuf@gmail.com> - 0.3.1-1
- Update to 0.3.1

* Mon Nov 02 2009 Ben Boeckel <MathStuf@gmail.com> - 0.2.0-1
- Initial package
