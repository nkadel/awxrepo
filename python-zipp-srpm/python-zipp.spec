%global pypi_name zipp

Name:           python-%{pypi_name}
Version:        3.0.0
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        MIT
URL:            https://github.com/jaraco/zipp
Source0:        %{pypi_source}
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm >= 1.15.0
# For testing
BuildRequires:  python%{python3_pkgversion}-func_timeout
BuildRequires:  python%{python3_pkgversion}-inflect
BuildRequires:  python%{python3_pkgversion}-jaraco-itertools
BuildRequires:  python%{python3_pkgversion}-more-itertools
BuildRequires:  python%{python3_pkgversion}-toml

%description -n python%{python3_pkgversion}-%{pypi_name}
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%if 0%{?fedora}
%{__python3} setup.py test
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}.*
#%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Mon Feb 24 2020 Nico Kadel-Garcia <nkadel@gmail.com> - 3.0.0-0
- Update to 3.0.0, with dependencies

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-1
- Initial package
