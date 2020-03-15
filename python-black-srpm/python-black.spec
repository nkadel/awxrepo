# Created by pyp2rpm-3.2.2
%global pypi_name black

Name:           python-%{pypi_name}
Version:        19.3b0
#Release:        3%%{?dist}
Release:        0%{?dist}
Summary:        The uncompromising code formatter

License:        MIT
URL:            https://github.com/ambv/black
Source0:        https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        black.1
Source2:        blackd.1
BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-aiohttp
BuildRequires:  python%{python3_pkgversion}-appdirs
BuildRequires:  python%{python3_pkgversion}-attrs >= 17.4.0
BuildRequires:  python%{python3_pkgversion}-click >= 6.5
BuildRequires:  python%{python3_pkgversion}-toml >= 0.9.4


%description
Black is the uncompromising Python code formatter. By using it, you agree to
cease control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting.
You will save time and mental energy for more important matters.

%package -n     %{pypi_name}
Summary:        %{summary}

Requires:       python%{python3_pkgversion}-aiohttp
Requires:       python%{python3_pkgversion}-appdirs
Requires:       python%{python3_pkgversion}-attrs >= 17.4.0
Requires:       python%{python3_pkgversion}-click >= 6.5
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-toml >= 0.9.4

# Package was renamed when Fedora 31 was rawhide
# Don't remove this before Fedora 33
Provides:       python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}
Obsoletes:      python%{python3_pkgversion}-%{pypi_name} < 19.3b0-2

%description -n %{pypi_name}
Black is the uncompromising Python code formatter. By using it, you agree to
cease control over minutiae of hand-formatting. In return, Black gives you
speed, determinism, and freedom from pycodestyle nagging about formatting.
You will save time and mental energy for more important matters.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
cp %{buildroot}/%{_bindir}/black %{buildroot}/%{_bindir}/black-%{python3_version}
cp %{buildroot}/%{_bindir}/blackd %{buildroot}/%{_bindir}/blackd-%{python3_version}
# ln -s {_bindir}/black-{python3_version} {buildroot}/{_bindir}/black-3

install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/black.1
install -D -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/blackd.1

%check
export PIP_INDEX_URL=http://host.invalid./
export PIP_NO_DEPS=yes
%{__python3} setup.py test

%files -n %{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/black
%{_bindir}/black-%{python3_version}
%{_mandir}/man1/black.1*
%{_bindir}/blackd
%{_bindir}/blackd-%{python3_version}
%{_mandir}/man1/blackd.1*

%{python3_sitelib}/__pycache__/black*
%{python3_sitelib}/black*.py
%{python3_sitelib}/blib2to3
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.3b0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Miro Hrončok <mhroncok@redhat.com> - 19.3b0-2
- Rename the binary package to black, rhbz#1692117

* Thu Mar 21 2019 Christian Heimes <cheimes@redhat.com> - 19.3b0-1
- New upstream release 19.3b0, rhbz#1688957

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.9b0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 27 2018 Christian Heimes <cheimes@redhat.com> - 18.9b0-1
- New upstream version 18.9b0
- Include blackd daemon

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.6b4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 18.6b4-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Christian Heimes <cheimes@redhat.com> - 18.6b4-1
- New upstream release 18.6b4, rhbz#1593485
- Remove workaround for missing empty_pyproject.toml

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 18.6b2-3
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Christian Heimes <cheimes@redhat.com> - 18.6b2-2
- Add new build and runtime dependency python3-toml
- Don't download external packages in tests
- Create missing empty_pyproject.toml for tests

* Sat Jun 09 2018 Christian Heimes <cheimes@redhat.com> - 18.6b2-1
- New upstream release 18.6b2, rhbz#1589399

* Wed Jun 06 2018 Christian Heimes <cheimes@redhat.com> - 18.6b1-1
- New upstream release 18.6b1

* Tue May 29 2018 Christian Heimes <cheimes@redhat.com> - 18.5b1-1
- New upstream release 18.5b0, rhbz#1579822

* Fri May 04 2018 Christian Heimes <cheimes@redhat.com> - 18.4a4-2
- Add man page
- Ignore false spelling warnings

* Wed May 02 2018 Christian Heimes <cheimes@redhat.com> - 18.4a4-1
- Initial package.
