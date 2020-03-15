%global srcname social-auth-core
%global desc Python Social Auth is an easy to setup social \
authentication/registration mechanism with support for several frameworks and \
auth providers. This is the core component of the python-social-auth ecosystem, \
it implements the common interface to define new authentication backends to \
third parties services, implement integrations with web frameworks and storage \
solutions. \

Name:           python-%{srcname}
Version:        1.7.0
#Release:        6%%{?dist}
Release:        0%{?dist}
Summary:        The core component of the python-social-auth ecosystem

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/python-social-auth/social-core/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         Unpin-the-test-requirements-and-use-unittest2-for-Py.patch

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python2-devel
BuildRequires:  python%{python3_pkgversion}-devel

%description
%{desc}


%package -n python%{python3_pkgversion}-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
BuildRequires: python%{python3_pkgversion}-cryptography
BuildRequires: python%{python3_pkgversion}-defusedxml
BuildRequires: python%{python3_pkgversion}-httpretty
BuildRequires: python%{python3_pkgversion}-nose
BuildRequires: python%{python3_pkgversion}-oauthlib
BuildRequires: python%{python3_pkgversion}-pyjwt
BuildRequires: python%{python3_pkgversion}-python3-openid
BuildRequires: python%{python3_pkgversion}-python3-saml
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-requests-oauthlib
BuildRequires: python%{python3_pkgversion}-six
BuildRequires: python%{python3_pkgversion}-unittest2
Requires: python%{python3_pkgversion}-cryptography
Requires: python%{python3_pkgversion}-defusedxml
Requires: python%{python3_pkgversion}-oauthlib
Requires: python%{python3_pkgversion}-pyjwt
Requires: python%{python3_pkgversion}-python3-openid
Requires: python%{python3_pkgversion}-python3-saml
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-requests-oauthlib
Requires: python%{python3_pkgversion}-six


%description -n python%{python3_pkgversion}-%{srcname}
%{desc}


%prep
%autosetup -p1 -n social-core-%{version}
rm -f requirements-openidconnect.txt
touch requirements-openidconnect.txt
rm -f social_core/tests/requirements-base.txt
touch social_core/tests/requirements-base.txt

sed -i -e 's|defusedxml>=0.5.0rc1|defusedxml>=0.5.0|' requirements-python3.txt

%build
%py3_build


%install
%py3_install


%check
%__python3 setup.py test


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md CHANGELOG.md
%{python3_sitelib}/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Kevin Fenzi <kevin@scrye.com> - 1.7.0-5
- Change the defusedxml requirement to not have rc1, which confused the python auto dep script.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.7.0-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.7.0-1
- Initial package.
