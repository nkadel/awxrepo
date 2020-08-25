%bcond_without tests

%bcond_without doc

%global srcname pip
%global python_wheelname %{srcname}-%{version}-py2.py3-none-any.whl
%global python_wheeldir %{_datadir}/python-wheels

%if %{with doc}
%global pypa_theme_commit_hash d2e63fbfc62af3b7050f619b2f5bb8658985b931
%endif

%global bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)

Name:           python-%{srcname}
# When updating, update the bundled libraries versions below!
# You can use vendor_meta.sh in the dist git repo
Version:        19.3.1
#Release:        2%%{?dist}
Release:        0%{?dist}
Summary:        A tool for installing and managing Python packages

# We bundle a lot of libraries with pip, which itself is under MIT license.
# Here is the list of the libraries with corresponding licenses:

# appdirs: MIT
# certifi: MPLv2.0
# chardet: LGPLv2
# colorama: BSD
# CacheControl: ASL 2.0
# contextlib2: Python
# distlib: Python
# distro: ASL 2.0
# html5lib: MIT
# idna: BSD
# ipaddress: Python
# msgpack: ASL 2.0
# packaging: ASL 2.0 or BSD
# pep517: MIT
# progress: ISC
# pyparsing: MIT
# pytoml: MIT
# requests: ASL 2.0
# retrying: ASL 2.0
# setuptools: MIT
# six: MIT
# urllib3: MIT
# webencodings: BSD

License:        MIT and Python and ASL 2.0 and BSD and ISC and LGPLv2 and MPLv2.0 and (ASL 2.0 or BSD)
URL:            http://www.pip-installer.org
Source0:        %pypi_source

BuildArch:      noarch

%if %{with tests}
# Version control systems
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/brz
BuildRequires:  /usr/bin/svn

BuildRequires:  python-setuptools-wheel
BuildRequires:  python-wheel-wheel
%endif

# to get tests:
# git clone https://github.com/pypa/pip && cd pip
# VERSION=   # define the version you want
# git checkout $VERSION && tar -czvf ../pip-$VERSION-tests.tar.gz tests/
%if %{with tests}
Source1:        pip-%{version}-tests.tar.gz
%endif

# Themes required to build the docs.
%if %{with doc}
Source2:        https://github.com/pypa/pypa-docs-theme/archive/%{pypa_theme_commit_hash}.tar.gz
Source3:        https://github.com/python/python-docs-theme/archive/2018.2.tar.gz
%endif

# Downstream only patch
# Emit a warning to the user if pip install is run with root privileges
# Issue upstream: https://github.com/pypa/pip/issues/4288
Patch1:         emit-a-warning-when-running-with-root-privileges.patch

# Add path to the doc themes to conf.py
Patch2:         html_theme_path.patch

# Prevent removing of the system packages installed under /usr/lib
# when pip install -U is executed.
# https://bugzilla.redhat.com/show_bug.cgi?id=1550368#c24
Patch3:         remove-existing-dist-only-if-path-conflicts.patch

# Use the system level root certificate instead of the one bundled in certifi
# https://bugzilla.redhat.com/show_bug.cgi?id=1655253
Patch4:         dummy-certifi.patch

%if %{with tests}
# Mark tests that need the Internet as network tests so we can skip them
# https://github.com/pypa/pip/pull/7359
Patch5:         network-tests.patch
%endif

# Dark magic to make pip 19.3+ support the old private API of main()
# This is needed to be able to use pip 19.3+ in ensurepip of older Pythons
# without patching all the Pythons
# A proper fix is discussed in:
#   https://discuss.python.org/t/can-we-finally-add-a-minimal-api-to-pip/2833/3
#   https://github.com/pypa/pip/pull/7061
#   https://github.com/python/cpython/pull/16782
Patch6:         callable-main.patch

# Downstream only patch
# Users might have local installations of pip from using
# `pip install --user --upgrade pip` on older/newer versions.
# If they do that and they run `pip` or  `pip3`, the one from /usr/bin is used.
# However that's the one from this RPM package and the import in there might
# fail (it tries to import from ~/.local, but older or newer pip is there with
# a bit different API).
# We add this patch as a dirty workaround to make /usr/bin/pip* work with
# both pip10+ (from this RPM) and older or newer (19.3+) pip (from whatever).
# A proper fix is to put ~/.local/bin in front of /usr/bin in the PATH,
# however others are against that and we cannot change it for existing
# installs/user homes anyway.
# https://bugzilla.redhat.com/show_bug.cgi?id=1569488
# https://bugzilla.redhat.com/show_bug.cgi?id=1571650
# https://bugzilla.redhat.com/show_bug.cgi?id=1767212
# WARNING: /usr/bin/pip* are entrypoints, this cannot be applied in %%prep!
# %%patch10 doesn't work outside of %%prep, so we add it as a source
Source10:        pip-allow-different-versions.patch

%description
pip is a package management system used to install and manage software packages
written in Python. Many packages can be found in the Python Package Index
(PyPI). pip is a recursive acronym that can stand for either "Pip Installs
Packages" or "Pip Installs Python".



# Virtual provides for the packages bundled by pip.
# You can find the versions in src/pip/_vendor/vendor.txt file.
%global bundled() %{expand:
Provides: bundled(python%{1}dist(appdirs)) = 1.4.3
Provides: bundled(python%{1}dist(CacheControl)) = 0.12.5
Provides: bundled(python%{1}dist(certifi)) = 2019.9.11
Provides: bundled(python%{1}dist(chardet)) = 3.0.4
Provides: bundled(python%{1}dist(colorama)) = 0.4.1
Provides: bundled(python%{1}dist(contextlib2)) = 0.6.0
Provides: bundled(python%{1}dist(distlib)) = 0.2.9.post0
Provides: bundled(python%{1}dist(distro)) = 1.4.0
Provides: bundled(python%{1}dist(html5lib)) = 1.0.1
Provides: bundled(python%{1}dist(idna)) = 2.8
Provides: bundled(python%{1}dist(ipaddress)) = 1.0.22
Provides: bundled(python%{1}dist(msgpack)) = 0.6.2
Provides: bundled(python%{1}dist(packaging)) = 19.2
Provides: bundled(python%{1}dist(pep517)) = 0.7.0
Provides: bundled(python%{1}dist(progress)) = 1.5
Provides: bundled(python%{1}dist(pyparsing)) = 2.4.2
Provides: bundled(python%{1}dist(pytoml)) = 0.1.21
Provides: bundled(python%{1}dist(requests)) = 2.22.0
Provides: bundled(python%{1}dist(retrying)) = 1.3.3
Provides: bundled(python%{1}dist(setuptools)) = 41.4.0
Provides: bundled(python%{1}dist(six)) = 1.12.0
Provides: bundled(python%{1}dist(urllib3)) = 1.25.6
Provides: bundled(python%{1}dist(webencodings)) = 0.5.1
}

# Some manylinux1 wheels need libcrypt.so.1.
# Manylinux1, a common (as of 2019) platform tag for binary wheels, relies
# on a glibc version that included ancient crypto functions, which were
# moved to libxcrypt and then removed in:
#  https://fedoraproject.org/wiki/Changes/FullyRemoveDeprecatedAndUnsafeFunctionsFromLibcrypt
# The manylinux1 standard assumed glibc would keep ABI compatibility,
# but that's only the case if libcrypt.so.1 (libxcrypt-compat) is around.
# This should be solved in the next manylinux standard (but it may be
# a long time until manylinux1 is phased out).
# See: https://github.com/pypa/manylinux/issues/305
# Note that manylinux is only applicable to x86 (both 32 and 64 bits)
%global crypt_compat_recommends() %{expand:
Recommends: (libcrypt.so.1()(64bit) if python%{1}(x86-64))
Recommends: (libcrypt.so.1 if python%{1}(x86-32))
}



%package -n python%{python3_pkgversion}-%{srcname}
Summary:        A tool for installing and managing Python3 packages

BuildRequires:  python%{python3_pkgversion}-devel
# python3 bootstrap: this is rebuilt before the final build of python3, which
# adds the dependency on python3-rpm-generators, so we require it manually
BuildRequires:  python%{python3_pkgversion}-rpm-generators
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  bash-completion
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pretend
BuildRequires:  python%{python3_pkgversion}-freezegun
BuildRequires:  python%{python3_pkgversion}-scripttest
BuildRequires:  python%{python3_pkgversion}-virtualenv
BuildRequires:  python%{python3_pkgversion}-pyyaml
%endif
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  ca-certificates
Requires:       ca-certificates
Requires:  python%{python3_pkgversion}-setuptools

# Virtual provides for the packages bundled by pip:
%{bundled 3}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Provides:       pip = %{version}-%{release}
Conflicts:      python-pip < %{version}-%{release}

%{crypt_compat_recommends 3}

%description -n python%{python3_pkgversion}-%{srcname}
pip is a package management system used to install and manage software packages
written in Python. Many packages can be found in the Python Package Index
(PyPI). pip is a recursive acronym that can stand for either "Pip Installs
Packages" or "Pip Installs Python".

%if %{with doc}
%package doc
Summary:        A documentation for a tool for installing and managing Python packages

BuildRequires:  python%{python3_pkgversion}-sphinx

%description doc
A documentation for a tool for installing and managing Python packages

%endif

%package wheel
Summary:        The pip wheel
Requires:       ca-certificates

# Virtual provides for the packages bundled by pip:
%{bundled 2}
%{bundled 3}

%{crypt_compat_recommends 2}
%{crypt_compat_recommends 3}

%description wheel
A Python wheel of pip to use with venv.

%prep
%setup -q -n %{srcname}-%{version}
%if %{with tests}
tar -xf %{SOURCE1}
%endif
%if %{with doc}
pushd docs/html
tar -xf %{SOURCE2}
mv pypa-docs-theme-%{pypa_theme_commit_hash} pypa
tar -xf %{SOURCE3}
mv python-docs-theme-2018.2 python-docs-theme
popd
%endif

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if %{with tests}
%patch5 -p1
%endif
%patch6 -p1

# this goes together with patch4
rm src/pip/_vendor/certifi/*.pem
sed -i '/\.pem$/d' src/pip.egg-info/SOURCES.txt

%if %{with tests}
# tests expect wheels in here
ln -s %{python_wheeldir} tests/data/common_wheels
%endif


%build
%py3_build_wheel

%if %{with doc}
export PYTHONPATH=./src/
# from tox.ini
sphinx-build-3 -b html docs/html docs/build/html
sphinx-build-3 -b man  docs/man  docs/build/man  -c docs/html
rm docs/build/html/.buildinfo
%endif


%install

# The following is similar to %%py3_install_wheel, but we don't have
# /usr/bin/pip yet, so we install using the wheel directly.
# (This is not standard wheel usage, but the pip wheel supports it -- see
#  pip/__main__.py)
%{__python3} dist/%{python_wheelname}/pip install \
    -I 'dist/%{python_wheelname}' \
    --root %{buildroot} \
    --no-deps

%if %{with doc}
pushd docs/build/man
install -d %{buildroot}%{_mandir}/man1
for MAN in *1; do
install -pm0644 $MAN %{buildroot}%{_mandir}/man1/$MAN
install -pm0644 $MAN %{buildroot}%{_mandir}/man1/${MAN/pip/pip3}
done
popd
%endif

# before we ln -s anything, we apply Source10 patch to all pips:
for PIP in %{buildroot}%{_bindir}/pip*; do
  patch -p1 --no-backup-if-mismatch $PIP < %{SOURCE10}
done


mkdir -p %{buildroot}%{bashcompdir}
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    %{buildroot}%{_bindir}/pip completion --bash \
    > %{buildroot}%{bashcompdir}/pip3

# Make bash completion apply to all the 5 symlinks we install
sed -i -e "s/^\\(complete.*\\) pip\$/\\1 pip pip{,-}{3,%{python3_version}}/" \
    -e s/_pip_completion/_pip3_completion/ \
    %{buildroot}%{bashcompdir}/pip3


# Provide symlinks to executables to comply with Fedora guidelines for Python
ln -s ./pip%{python3_version} %{buildroot}%{_bindir}/pip-%{python3_version}
ln -s ./pip-%{python3_version} %{buildroot}%{_bindir}/pip-3


# Make sure the INSTALLER is not pip, otherwise Patch2 won't work
# TODO Maybe we should make all our python packages have this?
echo rpm > %{buildroot}%{python3_sitelib}/pip-%{version}.dist-info/INSTALLER

mkdir -p %{buildroot}%{python_wheeldir}
install -p dist/%{python_wheelname} -t %{buildroot}%{python_wheeldir}


%if %{with tests}
%check
# bash completion tests only work from installed package
# needs unaltered sys.path and we cannot do that in %%check
#     test_pep517_and_build_options
#     test_config_file_venv_option
# TODO investigate failures
#     test_uninstall_non_local_distutils
pytest_k='not completion and
          not test_pep517_and_build_options and
          not test_config_file_venv_option and
          not test_uninstall_non_local_distutils'

mkdir _bin
export PATH="$PWD/_bin:$PATH"

export PYTHONPATH=%{buildroot}%{python3_sitelib}
ln -sf %{buildroot}%{_bindir}/pip3 _bin/pip
%{__python3} -m pytest -m 'not network' -k "$(echo $pytest_k)"
%endif


%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%if %{with doc}
%{_mandir}/man1/pip.*
%{_mandir}/man1/pip-*.*
%{_mandir}/man1/pip3.*
%{_mandir}/man1/pip3-*.*
%endif
%{_bindir}/pip
%{_bindir}/pip3
%{_bindir}/pip-3
%{_bindir}/pip%{python3_version}
%{_bindir}/pip-%{python3_version}
%{python3_sitelib}/pip*
%dir %{bashcompdir}
%{bashcompdir}/pip3

%if %{with doc}
%files doc
%license LICENSE.txt
%doc README.rst
%doc docs/build/html
%endif

%files wheel
%license LICENSE.txt
# we own the dir for simplicity
%dir %{python_wheeldir}/
%{python_wheeldir}/%{python_wheelname}

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Tomas Orsava <torsava@redhat.com> - 19.3.1-1
- Update to 19.3.1 (#1761508)
- Drop upstreamed patch that fixed expected output in test to not break with alpha/beta/rc Python versions

* Wed Oct 30 2019 Miro Hrončok <mhroncok@redhat.com> - 19.2.3-2
- Make /usr/bin/pip(3) work with user-installed pip 19.3+ (#1767212)

* Mon Sep 02 2019 Miro Hrončok <mhroncok@redhat.com> - 19.2.3-1
- Update to 19.2.3 (#1742230)
- Drop patch that should strip path prefixes from RECORD files, the paths are relative

* Wed Aug 21 2019 Petr Viktorin <pviktori@redhat.com> - 19.1.1-8
- Remove python2-pip
- Make pip bootstrap itself, rather than with an extra bootstrap RPM build

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-7
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-6
- Bootstrap for Python 3.8

* Wed Aug 14 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-5
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Petr Viktorin <pviktori@redhat.com> - 19.1.1-3
- Recommend libcrypt.so.1 for manylinux1 compatibility
- Make /usr/bin/pip Python 3

* Mon Jun 10 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-2
- Fix root warning when pip is invoked via python -m pip
- Remove a redundant second WARNING prefix form the abovementioned warning

* Wed May 15 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1.1-1
- Update to 19.1.1 (#1706995)

* Thu Apr 25 2019 Miro Hrončok <mhroncok@redhat.com> - 19.1-1
- Update to 19.1 (#1702525)

* Wed Mar 06 2019 Miro Hrončok <mhroncok@redhat.com> - 19.0.3-1
- Update to 19.0.3 (#1679277)

* Wed Feb 13 2019 Miro Hrončok <mhroncok@redhat.com> - 19.0.2-1
- Update to 19.0.2 (#1668492)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Miro Hrončok <mhroncok@redhat.com> - 18.1-2
- Use the system level root certificate instead of the one bundled in certifi

* Thu Nov 22 2018 Miro Hrončok <mhroncok@redhat.com> - 18.1-1
- Update to 18.1 (#1652089)

* Tue Sep 18 2018 Victor Stinner <vstinner@redhat.com> - 18.0-4
- Prevent removing of the system packages installed under /usr/lib
  when pip install -U is executed. Original patch by Michal Cyprian.
  Resolves: rhbz#1550368.

* Wed Aug 08 2018 Miro Hrončok <mhroncok@redhat.com> - 18.0-3
- Create python-pip-wheel package with the wheel

* Tue Jul 31 2018 Miro Hrončok <mhroncok@redhat.com> - 18.0-2
- Remove redundant "Unicode"" from License

* Mon Jul 23 2018 Marcel Plch <mplch@redhat.com> - 18.0-7
- Update to 18.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.3-5
- Rebuilt for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.3-4
- Bootstrap for Python 3.7

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.3-3
- Bootstrap for Python 3.7

* Fri May 04 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.3-2
- Allow to import pip10's main from pip9's /usr/bin/pip
- Do not show the "new version of pip" warning outside of venv
Resolves: rhbz#1569488
Resolves: rhbz#1571650
Resolves: rhbz#1573755

* Thu Mar 29 2018 Charalampos Stratakis <cstratak@redhat.com> - 9.0.3-1
- Update to 9.0.3

* Wed Feb 21 2018 Lumír Balhar <lbalhar@redhat.com> - 9.0.1-16
- Include built HTML documentation (in the new -doc subpackage) and man page

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 04 2017 Charalampos Stratakis <cstratak@redhat.com> - 9.0.1-14
- Reintroduce the ipaddress module in the python3 subpackage.

* Mon Nov 20 2017 Charalampos Stratakis <cstratak@redhat.com> - 9.0.1-13
- Add virtual provides for the bundled libraries. (rhbz#1096912)

* Tue Aug 29 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-12
- Switch macros to bcond's and make Python 2 optional to facilitate building
  the Python 2 and Python 3 modules

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-10
- Modernized package descriptions
Resolves: rhbz#1452568

* Tue Mar 21 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-9
- Fix typo in the sudo pip warning

* Fri Mar 03 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-8
- Patch 1 update: No sudo pip warning in venv or virtualenv

* Thu Feb 23 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-7
- Patch 1 update: Customize the warning with the proper version of the pip
  command

* Tue Feb 14 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-6
- Added patch 1: Emit a warning when running with root privileges

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Tomas Orsava <torsava@redhat.com> - 9.0.1-4
- Provide symlinks to executables to comply with Fedora guidelines for Python
Resolves: rhbz#1406922

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 9.0.1-3
- Rebuild for Python 3.6 with wheel

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 9.0.1-2
- Rebuild for Python 3.6 without wheel

* Fri Nov 18 2016 Orion Poplawski <orion@cora.nwra.com> - 9.0.1-1
- Update to 9.0.1

* Fri Nov 18 2016 Orion Poplawski <orion@cora.nwra.com> - 8.1.2-5
- Enable EPEL Python 3 builds
- Use new python macros
- Cleanup spec

* Fri Aug 05 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-4
- Updated the test sources

* Fri Aug 05 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-3
- Moved python-pip into the python2-pip subpackage
- Added the python_provide macro

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 17 2016 Tomas Orsava <torsava@redhat.com> - 8.1.2-1
- Update to 8.1.2
- Moved to a new PyPI URL format
- Updated the prefix-stripping patch because of upstream changes in pip/wheel.py

* Mon Feb 22 2016 Slavek Kabrda <bkabrda@redhat.com> - 8.0.2-1
- Update to 8.0.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 7.1.0-3
- Rebuilt for Python3.5 rebuild
- With wheel set to 1

* Tue Oct 13 2015 Robert Kuska <rkuska@redhat.com> - 7.1.0-2
- Rebuilt for Python3.5 rebuild

* Wed Jul 01 2015 Slavek Kabrda <bkabrda@redhat.com> - 7.1.0-1
- Update to 7.1.0

* Tue Jun 30 2015 Ville Skyttä <ville.skytta@iki.fi> - 7.0.3-3
- Install bash completion
- Ship LICENSE.txt as %%license where available

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Matej Stuchlik <mstuchli@redhat.com> - 7.0.3-1
- Update to 7.0.3

* Fri Mar 06 2015 Matej Stuchlik <mstuchli@redhat.com> - 6.0.8-1
- Update to 6.0.8

* Thu Dec 18 2014 Slavek Kabrda <bkabrda@redhat.com> - 1.5.6-5
- Only enable tests on Fedora.

* Mon Dec 01 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-4
- Add tests
- Add patch skipping tests requiring Internet access

* Tue Nov 18 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-3
- Added patch for local dos with predictable temp dictionary names
  (http://seclists.org/oss-sec/2014/q4/655)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.6-1
- Update to 1.5.6

* Fri Apr 25 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-4
- Rebuild as wheel for Python 3.4

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-3
- Disable build_wheel

* Thu Apr 24 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-2
- Rebuild as wheel for Python 3.4

* Mon Apr 07 2014 Matej Stuchlik <mstuchli@redhat.com> - 1.5.4-1
- Updated to 1.5.4

* Mon Oct 14 2013 Tim Flink <tflink@fedoraproject.org> - 1.4.1-1
- Removed patch for CVE 2013-2099 as it has been included in the upstream 1.4.1 release
- Updated version to 1.4.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.1-4
- Fix for CVE 2013-2099

* Thu May 23 2013 Tim Flink <tflink@fedoraproject.org> - 1.3.1-3
- undo python2 executable rename to python-pip. fixes #958377
- fix summary to match upstream

* Mon May 06 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.1-2
- Fix main package Summary, it's for Python 2, not 3 (#877401)

* Fri Apr 26 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.1-1
- Update to 1.3.1, fix for CVE-2013-1888.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-2
- Fixing files for python3-pip

* Thu Oct 04 2012 Tim Flink <tflink@fedoraproject.org> - 1.2.1-1
- Update to upstream 1.2.1
- Change binary from pip-python to python-pip (RHBZ#855495)
- Add alias from python-pip to pip-python, to be removed at a later date

* Tue May 15 2012 Tim Flink <tflink@fedoraproject.org> - 1.1.0-1
- Update to upstream 1.1.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- update to 1.0.2 and added python3 subpackage

* Wed Jun 22 2011 Tim Flink <tflink@fedoraproject.org> - 0.8.3-1
- update to 0.8.3 and project home page

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Luke Macken <lmacken@redhat.com> - 0.8.2-1
- update to 0.8.2 of pip
* Mon Aug 30 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.8-1
- update to 0.8 of pip
* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 7 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.2-1
- update to 0.7.2 of pip
* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.1-1
- update to 0.7.1 of pip
* Fri Jan 1 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1.4
- fix dependency issue
* Fri Dec 18 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-2
- fix spec file 
* Thu Dec 17 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-1
- upgrade to 0.6.1 of pip
* Mon Aug 31 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.4-1
- Initial package

