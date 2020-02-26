%bcond_without check

%global modname service-identity
%global pypi_name service_identity

%bcond_without python3
%bcond_with python2

Name:           python-%{modname}
Version:        18.1.0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        Service identity verification for pyOpenSSL

License:        MIT
URL:            https://github.com/pyca/service_identity
Source0:        %{url}/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%global _description \
Service Identity Verification for pyOpenSSL.\
\
TL;DR: Use this package if you use pyOpenSSL and don’t want to be MITMed.\
\
service_identity aspires to give you all the tools you need for verifying\
whether a certificate is valid for the intended purposes.\
\
In the simplest case, this means host name verification. However,\
service_identity implements RFC 6125 fully and plans to add other\
relevant RFCs too.

%description %{_description}

%if %{with python2}
%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
%if %{with check}
BuildRequires:  python2dist(attrs)
BuildRequires:  python2dist(idna) >= 0.6
BuildRequires:  python2dist(ipaddress)
BuildRequires:  python2dist(pyasn1)
BuildRequires:  python2dist(pyasn1-modules)
#BuildRequires:  python2dist(pyopenssl) >= 0.14
BuildRequires:  python2dist(pyOpenSSL) >= 0.14
BuildRequires:  python2dist(pytest)
%endif
Requires:       python2dist(attrs)
Requires:       python2dist(pyasn1)
Requires:       python2dist(pyasn1-modules)
BuildRequires:  python2dist(pyOpenSSL) >= 0.14
#Requires:       python2dist(pyopenssl) >= 0.14
%if 0%{?fedora}
Recommends:     python2dist(idna) >= 0.6
%endif

%description -n python2-%{modname} %{_description}

Python 2 version.
%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(sphinx)
%if %{with check}
BuildRequires:  python%{python3_pkgversion}dist(attrs)
BuildRequires:  python%{python3_pkgversion}dist(idna) >= 0.6
BuildRequires:  python%{python3_pkgversion}dist(pyasn1)
BuildRequires:  python%{python3_pkgversion}dist(pyasn1-modules)
#BuildRequires:  python%%{python3_pkgversion}dist(pyopenssl) >= 0.14
BuildRequires:  python%{python3_pkgversion}dist(pyOpensSSL) >= 0.14
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif
Requires:       python%{python3_pkgversion}dist(attrs)
Requires:       python%{python3_pkgversion}dist(pyasn1)
Requires:       python%{python3_pkgversion}dist(pyasn1-modules)
#Requires:       python%%{python3_pkgversion}dist(pyopenssl) >= 0.14
Requires:       python%{python3_pkgversion}dist(pyOpenSSL) >= 0.14
%if 0%{?fedora}
Recommends:     python%{python3_pkgversion}dist(idna) >= 0.6
%endif

%description -n python%{python3_pkgversion}-%{modname} %{_description}

Python 3 version.

%package -n python-%{modname}-doc
Summary:        Service-identity documentation

%description -n python-%{modname}-doc
Documentation for service-identity.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install

# generate html docs
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%if %{with check}
%check
%if %{with python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v
%endif
%if %{with python3}
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
%endif
%endif

%if %{with python2}
%files -n python2-%{modname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{pypi_name}-*.egg-info/
%{python2_sitelib}/%{pypi_name}/
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%{python3_sitelib}/%{pypi_name}/

%files -n python-%{modname}-doc
%doc html
%license LICENSE docs/license.rst
%endif

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Miro Hrončok <mhroncok@redhat.com> - 18.1.0-2
- Rebuilt to update automatic Python dependencies

* Wed Apr 10 2019 Robert-André Mauchin <zebob.m@gmail.com> - 18.1.0-1
- Release 18.1.0 (#1454995)
- Fix FTBFS  with pytest 4.3 (#1693822)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Miro Hrončok <mhroncok@redhat.com> - 16.0.0-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 16.0.0-6
- Rebuild for Python 3.6

* Mon Dec 19 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 16.0.0-5
- Modernize spec

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 16.0.0-4
- Enable tests

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 16.0.0-3
- Rebuild for Python 3.6
- Disable python3 tests for now

* Mon Oct 17 2016 Tom Prince <tom.prince@twistedmatrix.com> - 16.0.0-2
- Use python3 to test python3 package.
- Fix dependencies.

* Mon Oct 17 2016 Tom Prince <tom.prince@twistedmatrix.com> - 16.0.0-1
- Update source URL for pypi migration. (#1361604)
- Build new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 14.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 14.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 robyduck@fedoraproject.org - 14.0.0-1
- Build new version

* Sat Jul 12 2014 tom.prince@twistedmatrix.com - 1.0.0-2
- Add python-idna dependency.

* Sat Jul 12 2014 tom.prince@twistedmatrix.com - 1.0.0-1
- Initial package.
