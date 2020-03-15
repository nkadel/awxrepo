%global pypi_name python3-saml

Name:           %{pypi_name}
Version:        1.6.0
#Release:        2%{?dist}
Release:        0%{?dist}
Summary:        Add SAML support to your Python software using this library

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/onelogin/python3-saml/archive/v%{version}/%{pypi_name}-v%{version}.tar.gz

BuildArch: noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
This toolkit lets you turn your Python application into a SP
(Service Provider) that can be connected to an IdP (Identity Provider).


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Add SAML support to your Python software using this library

BuildRequires:  python%{python3_pkgversion}=devel
BuildRequires: %{py3_dist freezegun isodate xmlsec defusedxml}
Requires: %{py3_dist isodate xmlsec defusedxml}

# Replace badly named python3-saml package
Provides:   python3-saml
Conflicts:  python3-saml
Obsoletes:  python3-saml >= %{version}-%{release}

%description -n python%{python3_pkgversion}-%{pypi_name}
This toolkit lets you turn your Python application into a SP
(Service Provider) that can be connected to an IdP (Identity Provider).


%prep
%autosetup -p1


%build
# This is already relaxed upstream, just not in a release yet.
sed -i -e 's|defusedxml==0.5.0|defusedxml>=0.5.0|' setup.py
%py3_build


%install
%py3_install


%check
%__python3 setup.py test


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Kevin Fenzi <kevin@scrye.com> - 1.6.0-1
- Update to 1.6.0.
- Relax defusedxml requirement. Fixes bug #1723432

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.3.0-1
- Initial package.
