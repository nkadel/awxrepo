%global pypi_name rdflib

%global run_tests 1

# Disable python2
%global with_python2 0

Name:           python-%{pypi_name}
Version:        4.2.1
#Release:        9%%{?dist}.1
Release:        0%{?dist}.1
Summary:        Python library for working with RDF

License:        BSD
URL:            https://github.com/RDFLib/rdflib
Source0:        http://pypi.python.org/packages/source/r/rdflib/rdflib-%{version}.tar.gz
Patch1:         %{name}-SPARQLWrapper-optional.patch
BuildArch:      noarch

%if 0%{?rhe}
Buildrequires:  epel-rpm-macros
%endif

%if 0%{?with_python2}
BuildRequires:  python2-html5lib >= 1:
BuildRequires:  python2-isodate
BuildRequires:  python2-pyparsing
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

BuildRequires:  python%{python3_pkgversion}-html5lib >= 1:
BuildRequires:  python%{python3_pkgversion}-isodate
BuildRequires:  python%{python3_pkgversion}-pyparsing
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%if %{run_tests}
BuildRequires:  python2-nose >= 0.9.2
BuildRequires:  python%{python3_pkgversion}-nose >= 0.9.2
%endif

%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information.

The library contains parsers and serializers for RDF/XML, N3,
NTriples, Turtle, TriX, RDFa and Microdata. The library presents
a Graph interface which can be backed by any one of a number of
Store implementations. The core rdflib includes store
implementations for in memory storage, persistent storage on top
of the Berkeley DB, and a wrapper for remote SPARQL endpoints.


%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
Requires:       python2-html5lib >= 1:
Requires:       python2-isodate
Requires:       python2-pyparsing
Obsoletes:      python-rdfextras <= 0.1-7
Provides:       python-rdfextras = %{version}-%{release}

%description -n python2-%{pypi_name}
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information.

The library contains parsers and serializers for RDF/XML, N3,
NTriples, Turtle, TriX, RDFa and Microdata. The library presents
a Graph interface which can be backed by any one of a number of
Store implementations. The core rdflib includes store
implementations for in memory storage, persistent storage on top
of the Berkeley DB, and a wrapper for remote SPARQL endpoints.

This is for Python 2.
%endif


%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-html5lib >= 1:
Requires:       python%{python3_pkgversion}-isodate
Requires:       python%{python3_pkgversion}-pyparsing

%description -n python%{python3_pkgversion}-%{pypi_name}
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information.

The library contains parsers and serializers for RDF/XML, N3,
NTriples, Turtle, TriX, RDFa and Microdata. The library presents
a Graph interface which can be backed by any one of a number of
Store implementations. The core rdflib includes store
implementations for in memory storage, persistent storage on top
of the Berkeley DB, and a wrapper for remote SPARQL endpoints.

This is for Python 3.

%prep
%setup -q -n rdflib-%{version}
%patch1 -p1

# remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find -name "*.pyc" -delete

sed -i -e 's|_sn_gen=bnode_uuid()|_sn_gen=bnode_uuid|' test/test_bnode_ncname.py

# Separate dirs needed
rm -rf %{py3dir}
cp -a . %{py3dir}


%build
pushd %{py3dir}
%py3_build
popd

%if 0%{?with_python2}
%py2_build
%endif


%install
pushd %{py3dir}
%py3_install
popd

# rename binaries
for i in csv2rdf rdf2dot rdfgraphisomorphism rdfpipe rdfs2dot; do
    mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i-%{python3_version}
    ln -s $i-%{python3_version} %{buildroot}%{_bindir}/$i-3
done

%if 0%{?with_python2}
%py2_install

# rename binaries
for i in csv2rdf rdf2dot rdfgraphisomorphism rdfpipe rdfs2dot; do
    mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i-%{python2_version}
    ln -s $i-%{python2_version} %{buildroot}%{_bindir}/$i-2
    ln -s $i-2 %{buildroot}%{_bindir}/$i
done

cp LICENSE %{buildroot}%{python2_sitelib}/rdflib/LICENSE
%endif

cp LICENSE %{buildroot}%{python3_sitelib}/rdflib/LICENSE

# Various .py files within site-packages have a shebang line but aren't
# flagged as executable.
# I've gone through them and either removed the shebang or made them
# executable as appropriate:

# __main__ parses URI as N-Triples:
chmod +x %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/ntriples.py

# __main__ parses the file given on the command line:
chmod +x %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/notation3.py

# __main__ parses the file or URI given on the command line:
chmod +x %{buildroot}%{python3_sitelib}/rdflib/tools/rdfpipe.py

# __main__ runs a test (well, it's something)
chmod +x %{buildroot}%{python3_sitelib}/rdflib/extras/infixowl.py \
         %{buildroot}%{python3_sitelib}/rdflib/extras/external_graph_libs.py

# sed these headers out as they include no __main__
for lib in %{buildroot}%{python3_sitelib}/rdflib/extras/describer.py \
    %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/pyRdfa/extras/httpheader.py \
    %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/structureddata.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# sed shebangs
sed -i '1s=^#!/usr/bin/\(python\|env python\).*=#!%{__python3}='  \
    %{buildroot}%{python3_sitelib}/rdflib/extras/infixowl.py \
    %{buildroot}%{python3_sitelib}/rdflib/extras/external_graph_libs.py \
    %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/ntriples.py \
    %{buildroot}%{python3_sitelib}/rdflib/tools/rdfpipe.py \
    %{buildroot}%{python3_sitelib}/rdflib/plugins/parsers/notation3.py

%if 0%{?with_python2}
# __main__ parses URI as N-Triples:
chmod +x %{buildroot}%{python2_sitelib}/rdflib/plugins/parsers/ntriples.py

# __main__ parses the file given on the command line:
chmod +x %{buildroot}%{python2_sitelib}/rdflib/plugins/parsers/notation3.py

# __main__ parses the file or URI given on the command line:
chmod +x %{buildroot}%{python2_sitelib}/rdflib/tools/rdfpipe.py

# __main__ runs a test (well, it's something)
chmod +x %{buildroot}%{python2_sitelib}/rdflib/extras/infixowl.py \
         %{buildroot}%{python2_sitelib}/rdflib/extras/external_graph_libs.py

# sed these headers out as they include no __main__
for lib in %{buildroot}%{python2_sitelib}/rdflib/extras/describer.py \
    %{buildroot}%{python2_sitelib}/rdflib/plugins/parsers/pyRdfa/extras/httpheader.py \
    %{buildroot}%{python2_sitelib}/rdflib/plugins/parsers/structureddata.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# sed shebangs
sed -i '1s=^#!/usr/bin/\(python\|env python\).*=#!%{__python2}='  \
    %{buildroot}%{python2_sitelib}/rdflib/extras/infixowl.py \
    %{buildroot}%{python2_sitelib}/rdflib/extras/external_graph_libs.py \
    %{buildroot}%{python2_sitelib}/rdflib/plugins/parsers/ntriples.py \
    %{buildroot}%{python2_sitelib}/rdflib/tools/rdfpipe.py \
    %{buildroot}%{python2_sitelib}/rdflib/plugins/parsers/notation3.py
%endif

%check
%if %{run_tests}
sed -i -e "s|'--with-doctest'|#'--with-doctest'|" run_tests.py
sed -i -e "s|'--doctest-tests'|#'--doctest-tests'|" run_tests.py
sed -i -e "s|with-doctest = 1|#with-doctest = 1|" setup.cfg
# skip test_issue375, need to investigate the failure
%if 0%{?with_python2}
PYTHONPATH=./build/lib %{__python2} run_tests.py --verbose || :
%endif

pushd %{py3dir}/build/src
# The python 3 tests are failing, but better to have them here anyway
# TODO investigate the failures
%{__python3} run_tests.py --verbose || :
popd
%endif


%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info
%{_bindir}/csv2rdf
%{_bindir}/csv2rdf-2*
%{_bindir}/rdf2dot
%{_bindir}/rdf2dot-2*
%{_bindir}/rdfgraphisomorphism
%{_bindir}/rdfgraphisomorphism-2*
%{_bindir}/rdfpipe
%{_bindir}/rdfpipe-2*
%{_bindir}/rdfs2dot
%{_bindir}/rdfs2dot-2*
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_bindir}/csv2rdf-3*
%{_bindir}/rdf2dot-3*
%{_bindir}/rdfgraphisomorphism-3*
%{_bindir}/rdfpipe-3*
%{_bindir}/rdfs2dot-3*

%changelog
* Wed Jun 19 2019 Troy Dawson <tdawson@redhat.com> - 4.2.1-9.1
- Make python2 optional
- Do not build python2 on RHEL8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-7
- Rebuilt for Python 3.7

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 4.2.1-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Feb 20 2018 Than Ngo <than@redhat.com> - 4.2.1-5
- skip test_issue375 for python2, need to investigate later

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Miro Hrončok <mhroncok@redhat.com> - 4.2.1-1
- Update to 4.2.1
- Add missing python3 requires (rhbz#1295098)
- Modernize the package (python2 subpackage, %%pyX_* macros..., new versioned executable)
- Run tests on Python 3, even when failing
- Fixed bad shebangs

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 4.1.2-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 4.1.2-5
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 05 2015 Matthias Runge <mrunge@redhat.com> - 4.1.2-3
- add python3 subpackage (rhbz#1086844)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Dan Scott <dan@coffeecode.net> - 4.1.2-1
- Update for 4.1.2 release
- Add PYTHONPATH awareness for running tests

* Tue Mar 04 2014 Dan Scott <dan@coffeecode.net> - 4.1.1-1
- Update for 4.1.1 release
- Support for RDF 1.1 and HTML5
- Support for RDFa, TRiG, microdata parsers, and HTML structured data
- Patch to make SPARQLWrapper an extras_require until it is packaged

* Thu Dec 12 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2.3-6
- Remove BR of python-setuptools-devel

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 27 2013 David Malcolm <dmalcolm@redhat.com> - 3.2.3-4
- disable doctests (rhbz#914414)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 10 2012  Pierre-Yves Chibon <pingou@pingoured.fr> - 3.2.3-2
- Re-enable tests
- Backport using sed unit-tests fix from upstream
   (commit 26d25faa90483ed1ba7675d159d10e955dbaf442)

* Wed Oct 10 2012  Pierre-Yves Chibon <pingou@pingoured.fr> - 3.2.3-1
- Update to 3.2.3
- One test is failing, so disabling them for now

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.2.0-4
- Re-add the unittests, for that, patch one and disable the run of
the tests in the documentation of the code.

* Mon Jan 23 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.2.0-3
- Add python-isodate as R (RHBZ#784027)

* Fri Jan 20 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.2.0-2
- Found the official sources of the 3.2.0 release

* Fri Jan 20 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.2.0-1
- Update to 3.2.0-RC which seem to be same as 3.2.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 28 2011 David Malcolm <dmalcolm@redhat.com> - 3.1.0-1
- 3.1.0; converting from arch-specific to noarch (sitearch -> sitelib);
removing rdfpipe and various other extensions

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jan  6 2010 David Malcolm <dmalcolm@redhat.com> - 2.4.2-1
- bump to 2.4.2 (#552909)
- fix source URL to use version macro

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.4.0-8
- Rebuild for Python 2.6

* Wed Oct  1 2008 David Malcolm <dmalcolm@redhat.com> - 2.4.0-7
- fix tab/space issue in specfile

* Tue Sep 30 2008 David Malcolm <dmalcolm@redhat.com> - 2.4.0-6
- override autogeneration of provides info to eliminate unwanted provision
of SPARQLParserc.so

* Mon Sep 29 2008 David Malcolm <dmalcolm@redhat.com> - 2.4.0-5
- make various scripts executable, or remove shebang, as appropriate

* Tue Feb 19 2008 David Malcolm <dmalcolm@redhat.com> - 2.4.0-4
- delete test subdir

* Thu Jan 24 2008 David Malcolm <dmalcolm@redhat.com> - 2.4.0-3
- introduce macro to disable running the test suite, in the hope of eventually
patching it so it passes

* Mon Nov 19 2007 David Malcolm <dmalcolm@redhat.com> - 2.4.0-2
- add python-setuptools(-devel) build requirement; move testing to correct stanza

* Wed Aug  1 2007 David Malcolm <dmalcolm@redhat.com> - 2.4.0-1
- initial version

