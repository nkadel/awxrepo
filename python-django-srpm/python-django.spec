%{?python_enable_dependency_generator}
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%global         pypi_name Django
%global         pkg_name django


# Tests requiring Internet connections are disabled by default
# pass --with internet to run them (e.g. when doing a local rebuild
# for sanity checks before committing)
%bcond_with internet

Name:           python-django

#Version:        2.2.9
Version:        2.2.6
#Release:        1%%{?dist}
Release:        0%{?dist}
Summary:        A high-level Python Web framework

License:        BSD
URL:            http://www.djangoproject.com/
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

# skip tests requiring network connectivity
Patch000: Django-2.0-skip-net-tests.patch

BuildArch:      noarch

%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif

%description
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.

%package bash-completion
Summary:        bash completion files for Django
BuildRequires:  bash-completion

%description bash-completion
This package contains the bash completion files form Django high-level
Python Web framework.

%package -n python%{python3_pkgversion}-django-doc
Summary:        Documentation for Django
Requires:       python%{python3_pkgversion}-django = %{version}-%{release}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-psycopg2
# Funky RHEL renumbering
BuildRequires:  %{_bindir}/sphinx-build-3

%description -n python%{python3_pkgversion}-django-doc
This package contains the documentation for the Django high-level
Python Web framework.

%package -n python%{python3_pkgversion}-django
Summary:        A high-level Python Web framework
%{?python_provide:%python_provide python%{python3_pkgversion}-django}

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     (%{name}-bash-completion = %{version}-%{release} if bash)
%endif

#Requires:       sqlite >= 3.8.3
Requires:       sqlite
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-bcrypt
# test requirements
#BuildRequires: python%%{python3_pkgversion}-py-bcrypt
BuildRequires:  python%{python3_pkgversion}-docutils
BuildRequires:  python%{python3_pkgversion}-jinja2
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-pillow
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-pytz
BuildRequires:  python%{python3_pkgversion}-selenium
BuildRequires:  python%{python3_pkgversion}-sqlparse
BuildRequires:  python%{python3_pkgversion}-memcached
# Funky RHEL renumbering
BuildRequires:  %{_bindir}/sphinx-build-3

Provides: bundled(jquery) = 2.2.3
Provides: bundled(xregexp) = 2.0.0

# /usr/bin/django-admin moved from the python2 package
Conflicts:   python2-django < 2
Conflicts:   python-django < 2

# Removed when F28 was rawhide, keep this till F30:
Obsoletes:   python-django-devserver < 0.8.0-8
Obsoletes:   python2-django-devserver < 0.8.0-8
Obsoletes:   python-django-extra-form-fields < 0.0.1-16
Obsoletes:   python2-django-extra-form-fields < 0.0.1-16
Obsoletes:   python-django-profiles < 0.2-16
Obsoletes:   python2-django-profiles < 0.2-16
Obsoletes:   python-django-model-utils < 3.1.1-3
Obsoletes:   python2-django-model-utils < 3.1.1-3
Obsoletes:   python3-django-model-utils < 3.1.1-3
Obsoletes:   python%{python3_pkgversion}-django-model-utils < 3.1.1-3
Obsoletes:   python-django-netjsongraph < 0.2.2-5
Obsoletes:   python2-django-netjsongraph < 0.2.2-5
Obsoletes:   python3-django-netjsongraph < 0.2.2-5
Obsoletes:   python3=django-netjsongraph < 0.2.2-5
Obsoletes:   python%{python3_pkgversion}-django-netjsongraph < 0.2.2-5
Obsoletes:   python-django-dynamite < 0.4.1-16
Obsoletes:   python2-django-dynamite < 0.4.1-16
Obsoletes:   python-django-flash < 1.8-18
Obsoletes:   python2-django-flash < 1.8-18
Obsoletes:   python-django-followit < 0.0.3-16
Obsoletes:   python2-django-followit < 0.0.3-16
Obsoletes:   python-django-socialregistration < 0.5.10-11
Obsoletes:   python2-django-socialregistration < 0.5.10-11
Obsoletes:   python-django-staticfiles < 1.2.1-13
Obsoletes:   python2-django-staticfiles < 1.2.1-13
Obsoletes:   python-django-sekizai-doc < 0.8.1-12
Obsoletes:   python-django-sekizai < 0.8.1-12
Obsoletes:   python2-django-sekizai < 0.8.1-12
Obsoletes:   python3-django-sekizai-doc < 0.8.1-12
Obsoletes:   python3-django-sekizai < 0.8.1-12
Obsoletes:   python%{python3_pkgversion}-django-sekizai-doc < 0.8.1-12
Obsoletes:   python%{python3_pkgversion}-django-sekizai < 0.8.1-12
Obsoletes:   python-django-south < 1.0.2-3
Obsoletes:   python2-django-south < 1.0.2-3
Obsoletes:   python3-django-south < 1.0.2-3
Obsoletes:   python%{python3_pkgversion}-django-south < 1.0.2-3
Obsoletes:   python-django-pgjson < 0.3.1-7
Obsoletes:   python2-django-pgjson < 0.3.1-7
Obsoletes:   python3-django-pgjson < 0.3.1-7
Obsoletes:   python%{python3_pkgversion}-django-pgjson < 0.3.1-7
Obsoletes:   python-django-ckeditor < 5.3.0-4
Obsoletes:   python2-django-ckeditor < 5.3.0-4
Obsoletes:   python3-django-ckeditor < 5.3.0-4
Obsoletes:   python%{python3_pkgversion}-django-ckeditor < 5.3.0-4
Obsoletes:   python-django-extensions < 1.7.3-6
Obsoletes:   python2-django-extensions < 1.7.3-6
Obsoletes:   python3-django-extensions < 1.7.3-6
Obsoletes:   python%{python3_pkgversion}-django-extensions < 1.7.3-6
Obsoletes:   python-django-extensions-doc < 1.7.3-6
Obsoletes:   python-django-helpdesk < 0.2.1-3
Obsoletes:   python2-django-helpdesk < 0.2.1-3
Obsoletes:   python3-django-helpdesk < 0.2.1-3
Obsoletes:   python%{python3_pkgversion}-django-helpdesk < 0.2.1-3
Obsoletes:   python-django-openid-auth < 0.14-4
Obsoletes:   python2-django-openid-auth < 0.14-4
Obsoletes:   python3-django-openid-auth < 0.14-4
Obsoletes:   python%{python3_pkgversion}-django-openid-auth < 0.14-4
Obsoletes:   python-django-pylibmc < 0.6.1-6
Obsoletes:   python2-django-pylibmc < 0.6.1-6
Obsoletes:   python3-django-pylibmc < 0.6.1-6
Obsoletes:   python%{python3_pkgversion}-django-pylibmc < 0.6.1-6
Obsoletes:   python-django-select2 < 5.8.10-4
Obsoletes:   python2-django-select2 < 5.8.10-4
Obsoletes:   python3-django-select2 < 5.8.10-4
Obsoletes:   python%{python3_pkgversion}-django-select2 < 5.8.10-4
Obsoletes:   python-django-setuptest < 0.2.1-6
Obsoletes:   python2-django-setuptest < 0.2.1-6
Obsoletes:   python3-django-setuptest < 0.2.1-6
Obsoletes:   python%{python3_pkgversion}-django-setuptest < 0.2.1-6
Obsoletes:   python-django-federated-login < 1.0.0-16
Obsoletes:   python2-django-federated-login < 1.0.0-16
Obsoletes:   python3-django-federated-login < 1.0.0-16
Obsoletes:   python%{python3_pkgversion}-django-federated-login < 1.0.0-16


%description -n python%{python3_pkgversion}-django
Django is a high-level Python Web framework that encourages rapid
development and a clean, pragmatic design. It focuses on automating as
much as possible and adhering to the DRY (Don't Repeat Yourself)
principle.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# hard-code python3 in django-admin
pushd django
for file in bin/django-admin.py conf/project_template/manage.py-tpl ; do
    sed -i "s/\/env python/\/python3/" $file ;
done
popd
%build
%py3_build


%install
%py3_install

# Manually invoke the python byte compile macro for each path that needs byte
# compilation.
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}

%find_lang django
%find_lang djangojs
# append djangojs.lang to django.lang
cat djangojs.lang >> django.lang


# build documentation
export SPHINXBUILD=sphinx-build-3
# Enable docs only on fedora
%if 0%{?fedora}
(cd docs && mkdir djangohtml && mkdir -p _build/{doctrees,html} && make html)
%endif
cp -ar docs ..

# install man pages (for the main executable only)
mkdir -p %{buildroot}%{_mandir}/man1/
cp -p docs/man/* %{buildroot}%{_mandir}/man1/

# install bash completion script
bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
mkdir -p %{buildroot}$bashcompdir
install -m 0644 -p extras/django_bash_completion \
  %{buildroot}$bashcompdir/django-admin.py

for file in django-admin django-admin-3 django-admin-%{python3_version} python%{python3_pkgversion}-django-admin manage.py ; do
   ln -s django-admin.py %{buildroot}$bashcompdir/$file
done

# Add backward compatible links to %%{_bindir}
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-3
ln -s ./django-admin %{buildroot}%{_bindir}/django-admin-%{python3_version}
ln -s ./django-admin %{buildroot}%{_bindir}/python%{python3_pkgversion}-django-admin

# remove .po files
find $RPM_BUILD_ROOT -name "*.po" | xargs rm -f

# Only do tests on fedora
%if 0%{?fedora}
%check
cd %{_builddir}/%{pypi_name}-%{version}
export PYTHONPATH=$(pwd)
cd tests

%{__python3} runtests.py --settings=test_sqlite --verbosity=2 --parallel 1
%endif

%files bash-completion
%{_datadir}/bash-completion

%if 0%{?fedora}
%files -n python%{python3_pkgversion}-django-doc
%doc docs/_build/html/*
%endif

%files -n python%{python3_pkgversion}-django -f django.lang
%doc AUTHORS README.rst
%license LICENSE
%{_bindir}/django-admin.py
%{_bindir}/django-admin
%{_bindir}/django-admin-3
%{_bindir}/django-admin-%{python3_version}
%{_bindir}/python%{python3_pkgversion}-django-admin
%{_mandir}/man1/django-admin.1*
%attr(0755,root,root) %{python3_sitelib}/django/bin/django-admin.py*
# Include everything but the locale data ...
%dir %{python3_sitelib}/django
%dir %{python3_sitelib}/django/bin
%{python3_sitelib}/django/apps
%{python3_sitelib}/django/db/
%{python3_sitelib}/django/*.py*
%{python3_sitelib}/django/utils/
%{python3_sitelib}/django/dispatch/
%{python3_sitelib}/django/template/
%{python3_sitelib}/django/urls/
%{python3_sitelib}/django/views/
%dir %{python3_sitelib}/django/conf/
%dir %{python3_sitelib}/django/conf/locale/
%dir %{python3_sitelib}/django/conf/locale/??/
%dir %{python3_sitelib}/django/conf/locale/??_*/
%dir %{python3_sitelib}/django/conf/locale/*/LC_MESSAGES
%dir %{python3_sitelib}/django/contrib/
%{python3_sitelib}/django/contrib/*.py*
%dir %{python3_sitelib}/django/contrib/admin/
%dir %{python3_sitelib}/django/contrib/admin/locale
%dir %{python3_sitelib}/django/contrib/admin/locale/??/
%dir %{python3_sitelib}/django/contrib/admin/locale/??_*/
%dir %{python3_sitelib}/django/contrib/admin/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/admin/*.py*
%{python3_sitelib}/django/contrib/admin/migrations
%{python3_sitelib}/django/contrib/admin/views/
%{python3_sitelib}/django/contrib/admin/static/
%{python3_sitelib}/django/contrib/admin/templatetags/
%{python3_sitelib}/django/contrib/admin/templates/
%dir %{python3_sitelib}/django/contrib/admindocs/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/??/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/??_*/
%dir %{python3_sitelib}/django/contrib/admindocs/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/admindocs/*.py*
%{python3_sitelib}/django/contrib/admindocs/templates/
%dir %{python3_sitelib}/django/contrib/auth/
%dir %{python3_sitelib}/django/contrib/auth/locale/
%dir %{python3_sitelib}/django/contrib/auth/locale/??/
%dir %{python3_sitelib}/django/contrib/auth/locale/??_*/
%dir %{python3_sitelib}/django/contrib/auth/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/auth/*.py*
%{python3_sitelib}/django/contrib/auth/common-passwords.txt.gz
%{python3_sitelib}/django/contrib/auth/handlers/
%{python3_sitelib}/django/contrib/auth/management/
%{python3_sitelib}/django/contrib/auth/migrations/
%{python3_sitelib}/django/contrib/auth/templates/
%dir %{python3_sitelib}/django/contrib/contenttypes/
%dir %{python3_sitelib}/django/contrib/contenttypes/locale
%dir %{python3_sitelib}/django/contrib/contenttypes/locale/??/
%dir %{python3_sitelib}/django/contrib/contenttypes/locale/??_*/
%dir %{python3_sitelib}/django/contrib/contenttypes/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/contenttypes/*.py*
%{python3_sitelib}/django/contrib/contenttypes/__pycache__
%{python3_sitelib}/django/contrib/contenttypes/management/
%{python3_sitelib}/django/contrib/contenttypes/migrations/
%dir %{python3_sitelib}/django/contrib/flatpages/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/??/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/??_*/
%dir %{python3_sitelib}/django/contrib/flatpages/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/flatpages/*.py*
%{python3_sitelib}/django/contrib/flatpages/migrations
%{python3_sitelib}/django/contrib/flatpages/templatetags
%dir %{python3_sitelib}/django/contrib/gis/
%dir %{python3_sitelib}/django/contrib/gis/locale/
%dir %{python3_sitelib}/django/contrib/gis/locale/??/
%dir %{python3_sitelib}/django/contrib/gis/locale/??_*/
%dir %{python3_sitelib}/django/contrib/gis/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/gis/*.py*
%{python3_sitelib}/django/contrib/gis/geoip2/
%{python3_sitelib}/django/contrib/gis/serializers/
%{python3_sitelib}/django/contrib/gis/static/
%dir %{python3_sitelib}/django/contrib/humanize/
%dir %{python3_sitelib}/django/contrib/humanize/locale/
%dir %{python3_sitelib}/django/contrib/humanize/locale/??/
%dir %{python3_sitelib}/django/contrib/humanize/locale/??_*/
%dir %{python3_sitelib}/django/contrib/humanize/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/humanize/templatetags/
%{python3_sitelib}/django/contrib/humanize/*.py*
%dir %{python3_sitelib}/django/contrib/messages/
%{python3_sitelib}/django/contrib/messages/*.py*
%dir %{python3_sitelib}/django/contrib/postgres
%{python3_sitelib}/django/contrib/postgres/*.py*
%{python3_sitelib}/django/contrib/postgres/aggregates
%{python3_sitelib}/django/contrib/postgres/jinja2
%{python3_sitelib}/django/contrib/postgres/fields
%{python3_sitelib}/django/contrib/postgres/forms
%{python3_sitelib}/django/contrib/postgres/templates
%{python3_sitelib}/django/contrib/postgres/__pycache__
%dir %{python3_sitelib}/django/contrib/redirects
%dir %{python3_sitelib}/django/contrib/redirects/locale
%dir %{python3_sitelib}/django/contrib/redirects/locale/??/
%dir %{python3_sitelib}/django/contrib/redirects/locale/??_*/
%dir %{python3_sitelib}/django/contrib/redirects/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/redirects/*.py*
%{python3_sitelib}/django/contrib/redirects/migrations
%dir %{python3_sitelib}/django/contrib/sessions/
%dir %{python3_sitelib}/django/contrib/sessions/locale/
%dir %{python3_sitelib}/django/contrib/sessions/locale/??/
%dir %{python3_sitelib}/django/contrib/sessions/locale/??_*/
%dir %{python3_sitelib}/django/contrib/sessions/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/sessions/management/
%{python3_sitelib}/django/contrib/sessions/migrations/
%{python3_sitelib}/django/contrib/sessions/*.py*
%{python3_sitelib}/django/contrib/sitemaps/
%dir %{python3_sitelib}/django/contrib/sites/
%dir %{python3_sitelib}/django/contrib/sites/locale/
%dir %{python3_sitelib}/django/contrib/sites/locale/??/
%dir %{python3_sitelib}/django/contrib/sites/locale/??_*/
%dir %{python3_sitelib}/django/contrib/sites/locale/*/LC_MESSAGES
%{python3_sitelib}/django/contrib/sites/*.py*
%{python3_sitelib}/django/contrib/sites/migrations
%{python3_sitelib}/django/contrib/staticfiles/
%{python3_sitelib}/django/contrib/syndication/
%{python3_sitelib}/django/contrib/gis/admin/
%{python3_sitelib}/django/contrib/gis/db/
%{python3_sitelib}/django/contrib/gis/forms/
%{python3_sitelib}/django/contrib/gis/gdal/
%{python3_sitelib}/django/contrib/gis/geos/
%{python3_sitelib}/django/contrib/gis/management/
%{python3_sitelib}/django/contrib/gis/sitemaps/
%{python3_sitelib}/django/contrib/gis/templates/
%{python3_sitelib}/django/contrib/gis/utils/
%{python3_sitelib}/django/contrib/messages/storage/
%{python3_sitelib}/django/contrib/sessions/backends/
%{python3_sitelib}/django/forms/
%{python3_sitelib}/django/templatetags/
%{python3_sitelib}/django/core/
%{python3_sitelib}/django/http/
%{python3_sitelib}/django/middleware/
%{python3_sitelib}/django/test/
%{python3_sitelib}/django/conf/*.py*
%{python3_sitelib}/django/conf/project_template/
%{python3_sitelib}/django/conf/app_template/
%{python3_sitelib}/django/conf/urls/
%{python3_sitelib}/django/conf/locale/*/*.py*
%{python3_sitelib}/django/conf/locale/*.py*
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/django/__pycache__
%{python3_sitelib}/django/bin/__pycache__
%{python3_sitelib}/django/conf/__pycache__
%{python3_sitelib}/django/conf/locale/*/__pycache__
%{python3_sitelib}/django/contrib/__pycache__
%{python3_sitelib}/django/contrib/admin/__pycache__
%{python3_sitelib}/django/contrib/admindocs/__pycache__
%{python3_sitelib}/django/contrib/auth/__pycache__
%{python3_sitelib}/django/contrib/flatpages/__pycache__
%{python3_sitelib}/django/contrib/gis/__pycache__
%{python3_sitelib}/django/contrib/humanize/__pycache__
%{python3_sitelib}/django/contrib/messages/__pycache__
%{python3_sitelib}/django/contrib/redirects/__pycache__
%{python3_sitelib}/django/contrib/sessions/__pycache__
%{python3_sitelib}/django/contrib/sites/__pycache__


%changelog
* Wed Feb 26 2020 Nico KAdel-Garcia <nkadel@gmail.com>
- Backport for RHEL
- Switch to "pypi_name" rather than "pkgname"
- Use more robuset Source entry

* Tue Jan 07 2020 Matthias Runge <mrunge@redhat.com> - 2.2.9-1
- fix CVE-2019-19844 (rhbz#1788429)

* Wed Jul 03 2019 Matthias Runge <mrunge@redhat.com> - 2.2.3-1
- fix CVE-2019-12781 Incorrect HTTP detection with reverse-proxy connecting
  via HTTPS (rhbz#1726014)

* Tue Jun 04 2019 Matthias Runge <mrunge@redhat.com> - 2.2.2-1
- fix CVE-2019-12308 AdminURLFieldWidget XSS
  (rhbz#1716763)

* Wed Apr 10 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-1
- Update to 2.2 (rhbz#1674439)

* Wed Feb 20 2019 Matthias Runge <mrunge@redhat.com> - 2.1.7-1
- Fix CVE-2019-6975: Memory exhaustion in django.utils.numberformat.format()
  rhbz#1678264

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.5-2
- Enable python dependency generator

* Mon Jan 07 2019 Matthias Runge <mrunge@redhat.com> - 2.1.5-1
- fix CVE-2019-3498 python-django: Content spoofing via URL path in
  default 404 page (rhbz#1663723)

* Mon Oct 22 2018 Matthias Runge <mrunge@redhat.com> - 2.1.2-1
- fix CVE-2018-16984 Password hash disclosure to “view only” admin users
  (rhbz#1639399)

* Fri Aug 17 2018 Matthias Runge <mrunge@redhat.com> - 2.1-1
- update to 2.1 (rhbz#1611025)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Matthias Runge <mrunge@redhat.com> - 2.0.7-1
- bugfix update to 2.0.7 (rhbz#1597265)

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.6-2
- Rebuilt for Python 3.7

* Mon Jun 04 2018 Matthias Runge <mrunge@redhat.com> - 2.0.6-1
- bugfix update to 2.0.6 (rhbz#1585347)

* Thu May 03 2018 Matthias Runge <mrunge@redhat.com> - 2.0.5-1
- update to 2.0.5 (rhbz#1574123)

* Tue Apr 03 2018 Matthias Runge <mrunge@redhat.com> - 2.0.4-1
- update to 2.0.4 (rhbz#1541188)

* Fri Mar 16 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-4
- Obsolete pythonX-django-ckeditor, pythonX-django-extensions,
  pythonX-django-helpdesk, pythonX-django-openid-auth, pythonX-django-pylibmc,
  pythonX-django-select2, pythonX-django-setuptest,
  pythonX-django-federated-login

* Sun Mar 11 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-3
- Obsolete pythonX-django-pgjson

* Wed Mar 07 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Obsolete pythonX-django-sekizai and pythonX-django-south

* Tue Mar 06 2018 Matthias Runge <mrunge@redhat.com> - 2.0.3-1
- update to 2.0.3, fix CVE-2018-7536 (rhbz#1552178)

* Fri Mar 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Obsolete packages retired from https://pagure.io/fesco/issue/1857

* Fri Mar 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-3
- Obsolete pythonX-django-model-utils and pythonX-django-netjsongraph

* Wed Feb 07 2018 Matthias Runge <mrunge@redhat.com> - 2.0.2-2
- requires python2 while being python3 (rhbz#15424)

* Fri Feb 02 2018 Matthias Runge <mrunge@redhat.com> - 2.0.2-1
- fix CVE-2018-6188

* Tue Jan 16 2018 Matthias Runge <mrunge@redhat.com> - 2.0.1-1
- update to 2.0.1
- remove python2 bits
- enable python3 tests

* Tue Jan 16 2018 Troy Dawson <tdawson@redhat.com> - 1.11.9-2
- Update conditionals

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.9-1
- update to 1.11.9

* Thu Jan 04 2018 Miro Hrončok <mhroncok@redhat.com> - 1.11.8-2
- Obsolete python(2)-django-devserver

* Fri Dec 15 2017 Matthias Runge <mrunge@redhat.com> - 1.11.8-1
- update to 1.11.8

* Wed Sep 06 2017 Matthias Runge <mrunge@redhat.com> - 1.11.5-1
- update to 1.11.5 (rhbz#1488683)

* Wed Aug 02 2017 Matthias Runge <mrunge@redhat.com> - 1.11.4-1
- update to 1.11.4 (rhbz#1477382)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Matthias Runge <mrunge@redhat.com> - 1.11.3-1
- Update to 1.11.3 (rhbz#1467029)

* Thu Jun 15 2017 Matthias Runge <mrunge@redhat.com> - 1.11.2-1
- update to 1.11.2 (rhbz#1448664
- add dependency to pytz (rhbz#1458493)

* Thu Apr 06 2017 Matthias Runge <mrunge@redhat.com> - 1.11-1
- update to 1.11 (rhbz#1410268)

* Tue Feb 28 2017 Matthias Runge <mrunge@redhat.com> - 1.10.5-1
- rebase to 1.10.5, fix FTBFS (rhbz#1424135)
- declare bundled libs (rhbz#1401243)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.10.4-2
- Rebuild for Python 3.6
- Disable python3 tests for now

* Fri Dec 02 2016 Matthias Runge <mrunge@redhat.com> - 1.10.4-1
- update to stable 1.10.4 (rhbz#1400730)

* Wed Nov 02 2016 Matthias Runge <mrunge@redhat.com> - 1.10.3-1
- update to 1.10.3 (rhbz#1390782)
- fix CVE-2016-9013, CVE-2016-9014

* Mon Oct 03 2016 Matthias Runge <mrunge@redhat.com> - 1.10.2-1
- update to 1.10.2 (rhbz#1381019)

* Thu Sep 22 2016 Matthias Runge <mrunge@redhat.com> - 1.10.1-1
- rebase to 1.10.1 (rhbz#1338391)

* Thu Jul 21 2016 Matthias Runge <mrunge@redhat.com> - 1-9.8-1
- fix CVE-2016-6186 (rhbz#1357701)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.7-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 06 2016 Matthias Runge <mrunge@redhat.com> - 1.9.7-1
- bugfix release

* Tue May 31 2016 Nils Philippsen <nils@redhat.com>
- fix source URL

* Sun May  8 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.6-2
- Put the provives/obsoletes in the right spot for new python naming

* Tue May 03 2016 Matthias Runge <mrunge@redhat.com> - 1.9.6-1
- update to 1.9.6 (rhbz#1323374)

* Tue Mar 08 2016 Matthias Runge <mrunge@redhat.com> - 1.9.4-1
- update to 1.9.4 fixing a regression introduced in last
  upstream fix for CVE-2016-2512

* Wed Mar 02 2016 Matthias Runge <mrunge@redhat.com> - 1.9.3-1
- update to 1.9.3, fixing CVE-2016-2512, CVE-2016-2513
  (rhbz#1313500)

* Thu Feb 11 2016 Matthias Runge <mrunge@redhat.com> - 1.9.2-1
- update to 1.9.2 (rhbz#1266062)
- modernize spec file, provide py2, obsolete python-django

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

