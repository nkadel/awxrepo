#
# spec file for package python-immutables
#
# Copyright (c) 2020 Nico Kadel-Garcia.
#

%global with_python3 1
%global with_python2 0

%global pypi_name immutables

# Common SRPM package
Name:           python-%{pypi_name}
Version:        0.11
Release:        0%{?dist}
Url:            https://github.com/MagicStack/immutables
Summary:        Immutable Collections
License:        Apache-2.0
Group:          Development/Languages/Python
# Stop using py2pack macros, use local macros published by Fedora
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

%if 0%{?rhel}
Buildrequires: epel-rpm-macros
%endif

%description
immutables
==========

An immutable mapping type for Python.

The underlying datastructure is a Hash Array Mapped Trie (HAMT)
used in Clojure, Scala, Haskell, and other functional languages.
This implementation is used in CPython 3.7 in the ``contextvars``
module (see PEP 550 and PEP 567 for more details).

Immutable mappings based on HAMT have O(log N) performance for both
``set()`` and ``get()`` operations, which is essentially O(1) for
relatively small mappings.

%if %{with_python2}
%package -n python2-%{pypi_name}
Version:        0.11
Release:        0%{?dist}
Url:            https://github.com/MagicStack/immutables
Summary:        Immutable Collections
License:        Apache-2.0

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
immutables
==========

An immutable mapping type for Python.

The underlying datastructure is a Hash Array Mapped Trie (HAMT)
used in Clojure, Scala, Haskell, and other functional languages.
This implementation is used in CPython 3.7 in the ``contextvars``
module (see PEP 550 and PEP 567 for more details).

Immutable mappings based on HAMT have O(log N) performance for both
``set()`` and ``get()`` operations, which is essentially O(1) for
relatively small mappings.

%endif # with_python2

%if %{with_python3}
%package -n python%{python3_pkgversion}-%{pypi_name}
Version:        0.11
Release:        0%{?dist}
Url:            https://github.com/MagicStack/immutables
Summary:        Immutable Collections
License:        Apache-2.0

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
immutables
==========

An immutable mapping type for Python.

The underlying datastructure is a Hash Array Mapped Trie (HAMT)
used in Clojure, Scala, Haskell, and other functional languages.
This implementation is used in CPython 3.7 in the ``contextvars``
module (see PEP 550 and PEP 567 for more details).

Immutable mappings based on HAMT have O(log N) performance for both
``set()`` and ``get()`` operations, which is essentially O(1) for
relatively small mappings.

%endif # with_python3

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with_python2}
%py2_build
%endif # with_python2

%if %{with_python3}
%py3_build
%endif # with_python3

%install
%if %{with_python2}
%py2_install
%endif # with_python2

%if %{with_python3}
%py3_install
%endif # with_python3

%clean
rm -rf %{buildroot}

%if %{with_python2}
%files -n python2-%{pypi_name}
%defattr(-,root,root,-)
%{python2_sitearch}/*
%endif # with_python2

%if %{with_python3}
%files -n python%{python3_pkgversion}-%{pypi_name}
%defattr(-,root,root,-)
%{python3_sitearch}/*
%endif # with_python3

%changelog
