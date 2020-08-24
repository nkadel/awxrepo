%global pypi_name xmlsec

Name:           python-%{pypi_name}
Version:        1.3.3
#Release:        6%%{?dist}
Release:        0
Summary:        Python bindings for the XML Security Library

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source

%if -%{?rhel}
buildrequires:  epel-rpm-macros
%endif

BuildRequires:  gcc
BuildRequires:  libxml2-devel >= 2.9.1
BuildRequires:  xmlsec1-devel >= 1.2.18
BuildRequires:  libtool-ltdl-devel
BuildRequires:  python%{python3_pkgversion}-devel


%description
%{summary}.


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires: python%{python3_pkgversion}-lxml
BuildRequires: python%{python3_pkgversion}-pkgconfig
BuildRequires: python%{python3_pkgversion}-pytest
Requires: libxml2 >= 2.9.1
Requires: xmlsec1 >= 1.2.18
Requires: xmlsec1-openssl
Requires: python%{python3_pkgversion}-lxml
Requires: python%{python3_pkgversion}-pkgconfig


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}.


%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf *.egg-info


%build
%py3_build


%install
%py3_install


# Tests aren't available


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/xmlsec*.so
%{python3_sitearch}/xmlsec-%{version}-*.egg-info


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.3.3-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Thu Jan 25 2018 Jeremy Cline <jeremy@jcline.org> - 1.3.3-1
- Initial package.
