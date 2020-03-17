# Created by pyp2rpm-3.3.3
%global pypi_name pkgconfig

Name:           python-%{pypi_name}
Version:        1.5.1
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        Interface Python with pkg-config

License:        None
URL:            https://github.com/matze/pkgconfig
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python3dist(setuptools)

%description
pkgconfig is a Python module to interface with the pkg-config command
line tool and supports Python 2.6+ and 3.3+.It can be used to- find all pkg-
config packages :: >>> packages pkgconfig.list_all()- check if a package exists
:: >>> pkgconfig.exists('glib-2.0') True- check if a package meets certain
version requirements :: >>> pkgconfig.installed('glib-2.0', '< 2.26') False-
return...

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
pkgconfig is a Python module to interface with the pkg-config command
line tool and supports Python 2.6+ and 3.3+.It can be used to- find all pkg-
config packages :: >>> packages pkgconfig.list_all()- check if a package exists
:: >>> pkgconfig.exists('glib-2.0') True- check if a package meets certain
version requirements :: >>> pkgconfig.installed('glib-2.0', '< 2.26') False-
return...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Mar 16 2020 Nico Kadel-Garcia <nico.kadel-garcia@cengage.com> - 1.5.1-1
- Initial package.
