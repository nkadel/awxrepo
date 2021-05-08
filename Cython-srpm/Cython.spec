# python2X and python3X are built form the same module, so we need a conditional
# for python[23] bits the state of the conditional is not important in the spec,
# it is set in modulemd
%bcond_without python2
%bcond_without python3

%global srcname Cython
%global upname cython

Name:           Cython
Version:        0.28.1
#Release:        7%%{?dist}
Release:        0%{?dist}
Summary:        Language for writing Python extension modules

License:        ASL 2.0
URL:            http://www.cython.org
Source:         https://github.com/cython/cython/archive/%{version}/%{srcname}-%{version}.tar.gz

# Replace GCC's attribute optimize("Os") by the better supported and similar (cold).
# We essentially disable again strict aliasing which makes some compiler warnings
# go away on python2.
# Fixed upstream: https://github.com/cython/cython/commit/9ddac7152091eac62830fea4f38b4d7f9edb6a86
Patch0:         replace-gcc-attribute-os-with-cold.patch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

BuildRequires:  gcc

%global _description \
This is a development version of Pyrex, a language\
for writing Python extension modules.

%description %{_description}

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
Obsoletes:      Cython < 0.28.1-5
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools


%description -n python2-%{srcname} %{_description}

Python 2 version.

%endif

%if %{with python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

Python 3 version.

%endif

%prep
%autosetup -n %{upname}-%{version} -p1

%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}

%install
# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if %{with python3}
%py3_install
for bin in cython cythonize cygdb; do
  mv %{buildroot}%{_bindir}/${bin} %{buildroot}%{_bindir}/${bin}3
done
rm -rf %{buildroot}%{python3_sitelib}/setuptools/tests
%endif

%if %{with python2}
%py2_install
for bin in cython cythonize cygdb; do
  mv %{buildroot}%{_bindir}/${bin} %{buildroot}%{_bindir}/${bin}-%{python2_version}
  ln -s ${bin}-%{python2_version} $RPM_BUILD_ROOT%{_bindir}/${bin}-2
done
rm -rf %{buildroot}%{python2_sitelib}/setuptools/tests
%endif

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE.txt
%doc *.txt Demos Doc Tools
%{_bindir}/cython-2
%{_bindir}/cygdb-2
%{_bindir}/cythonize-2
%{_bindir}/cython-%{python2_version}
%{_bindir}/cygdb-%{python2_version}
%{_bindir}/cythonize-%{python2_version}
%{python2_sitearch}/%{srcname}-*.egg-info/
%{python2_sitearch}/%{srcname}/
%{python2_sitearch}/pyximport/
%{python2_sitearch}/%{upname}.py*
%endif

%if %{with python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc *.txt Demos Doc Tools
%{_bindir}/cython3
%{_bindir}/cythonize3
%{_bindir}/cygdb3
%{python3_sitearch}/%{srcname}-*.egg-info/
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/pyximport/
%{python3_sitearch}/%{upname}.py
%{python3_sitearch}/__pycache__/%{upname}.*
%endif

%changelog
* Wed Apr 03 2019 Tomas Orsava <torsava@redhat.com> - 0.28.1-7
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Wed Dec 12 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.28.1-6
- Replace GCC's attribute optimize("Os") by the better supported and similar (cold).
- Resolves: rhbz#1658621

* Tue Oct 09 2018 Lumír Balhar <lbalhar@redhat.com> - 0.28.1-5
- Remove unversioned provides
- Resolves: rhbz#1628242

* Wed Aug 08 2018 Lumír Balhar <lbalhar@redhat.com> - 0.28.1-4
- Remove unversioned binaries from python2 subpackage
- Resolves: rhbz#1613343

* Wed Aug 01 2018 Lumír Balhar <lbalhar@redhat.com> - 0.28.1-3
- First version for python27 module
