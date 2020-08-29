# Enable Python dependency generation
%{?python_enable_dependency_generator}

# Created by pyp2rpm-3.3.2
%global pypi_name pytest-flake8

%global desc \
%{name} is a plugin for pytest to leverage flake8 to automatically\
and efficiently checking for PEP8 compliance of a project.

Name:           python-%{pypi_name}
Version:        1.0.4
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        Plugin for pytest to check PEP8 compliance with Flake8

License:        BSD
URL:            https://github.com/tholo/pytest-flake8
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-flake8 >= 3.5
BuildRequires:  python%{python3_pkgversion}-pytest >= 3.5
BuildRequires:  python%{python3_pkgversion}-setuptools

%description %{desc}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %{desc}


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_flake8.py
%{python3_sitelib}/pytest_flake8-%{version}-py?.?.egg-info

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Dan Radez <dradez@redhat.com> - 1.0.4-1
- update to 1.0.4

* Wed Feb 27 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Subpackage python2-pytest-flake8 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 11 2018 Neal Gompa <ngompa13@gmail.com> - 1.0.1-1
- Initial package
