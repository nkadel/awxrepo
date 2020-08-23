%global pypi_name python3-openid

Name:           python-%{pypi_name}
Version:        3.1.0
#Release:        5%%{?dist}
Release:        0%{?dist}
Summary:        Python 3 port of the python-openid library
License:        ASL 2.0
URL:            https://github.com/necaris/%{pypi_name}
Source0:        %pypi_source

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
This started out as a fork of the Python OpenID library,
with changes to make it Python 3 compatible.
It's now a port of that library,
including cleanups and updates to the code in general.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Python 3 port of the python-openid library

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-django
BuildRequires:  python%{python3_pkgversion}-psycopg2
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-defusedxml

Requires:       python%{python3_pkgversion}-defusedxml

# Deal with loony tunes inconstent Fedora discard of python- prefix
Provides:       python3-openid = %{version}-%{release}
Obsoletes:      python3-openid <= %{version}
Conflicts:	python3-openid


%description -n python%{python3_pkgversion}-%{pypi_name}
This started out as a fork of the Python OpenID library,
with changes to make it Python 3 compatible.
It's now a port of that library,
including cleanups and updates to the code in general.

%prep
%setup -q -n %{pypi_name}-%{version}

# replace env python shebangs with env python3
grep -Erl '^#!/usr/bin/env python$' | xargs \
sed -i -r '1 s|^#!/usr/bin/env python$|#!%{__python3}|g'

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f

%check
%{__python3} -m unittest openid.test.test_suite

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc LICENSE NEWS.md
%dir %{python3_sitelib}/openid
%{python3_sitelib}/openid/*.py
%dir %{python3_sitelib}/openid/__pycache__
%{python3_sitelib}/openid/__pycache__/*.py[co]
%dir %{python3_sitelib}/openid/consumer
%{python3_sitelib}/openid/consumer/*.py
%dir %{python3_sitelib}/openid/consumer/__pycache__
%{python3_sitelib}/openid/consumer/__pycache__/*.py[co]
%dir %{python3_sitelib}/openid/extensions
%{python3_sitelib}/openid/extensions/*.py
%dir %{python3_sitelib}/openid/extensions/__pycache__
%{python3_sitelib}/openid/extensions/__pycache__/*.py[co]
%dir %{python3_sitelib}/openid/extensions/draft
%{python3_sitelib}/openid/extensions/draft/*.py
%dir %{python3_sitelib}/openid/extensions/draft/__pycache__
%{python3_sitelib}/openid/extensions/draft/__pycache__/*.py[co]
%dir %{python3_sitelib}/openid/server
%{python3_sitelib}/openid/server/*.py
%dir %{python3_sitelib}/openid/server/__pycache__
%{python3_sitelib}/openid/server/__pycache__/*.py[co]
%dir %{python3_sitelib}/openid/store
%{python3_sitelib}/openid/store/*.py
%dir %{python3_sitelib}/openid/store/__pycache__
%{python3_sitelib}/openid/store/__pycache__/*.py[co]
%dir %{python3_sitelib}/openid/yadis
%{python3_sitelib}/openid/yadis/*.py
%dir %{python3_sitelib}/openid/yadis/__pycache__
%{python3_sitelib}/openid/yadis/__pycache__/*.py[co]
%{python3_sitelib}/python3_openid-%{version}-py3.*.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-2
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.0-1
- Update to 3.1.0, fix FTBFS (#1556287)
- Use nonenv shebangs

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Jakub Dorňák <jakub.dornak@misli.cz> - 3.0.10-1
- Update to version 3.0.10

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.9-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.9-2
- Require python3-defusedxml

* Thu Nov 19 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.9-1
- Update to version 3.0.9

* Fri Nov 13 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.6-1
- Update to version 3.0.6

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.5-1
- Update to version 3.0.5

* Wed Jun 17 2015 Jakub Dorňák <jdornak@redhat.com> - 3.0.2-4
- use BytesIO to write the response (instead of StringIO)
    Resolves: 1232809

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Nov 29 2013 Jakub Dorňák <jdornak@redhat.com> - 3.0.2-1
- Initial package
