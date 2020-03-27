%define  debug_package %{nil}
%define _prefix /opt/awx
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user awx
%define service_group awx
%define service_homedir /var/lib/awx
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

%global awx_mainversion 9.3.0
%global awx_subversion %{nil}

Summary: Ansible AWX
Name: ansible-awx
Version: %{awx_mainversion}%{awx_subversion}
Release: 0%{?dist}
Source0: awx-%{version}.tar.gz
Source1: settings.py.dist
%if 0%{?el7}
Source2: awx-cbreceiver.service
Source3: awx-dispatcher.service
Source5: awx-channels-worker.service
Source6: awx-daphne.service
Source7: awx-web.service
%endif
Source8: nginx.conf.example
Source9: awx-create-venv
Source10: awx-rpm-logo.svg
Source11: awx.service
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

%if 0%{?rhel}
BuildRequires: epel-rpm-macros
%endif

BuildRequires: git
BuildRequires: libcurl-devel
BuildRequires: libffi-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: libxslt-devel
BuildRequires: openldap-devel
BuildRequires: postgresql-server >= 10
BuildRequires: postgresql-server-devel >= 10
BuildRequires: xmlsec1-devel
BuildRequires: xmlsec1-openssl-devel

# "via" options
BuildRequires: python%{python3_pkgversion}-adal
BuildRequires: python%{python3_pkgversion}-amqp
BuildRequires: python%{python3_pkgversion}-asgiref
BuildRequires: python%{python3_pkgversion}-attrs
BuildRequires: python%{python3_pkgversion}-autobahn
BuildRequires: python%{python3_pkgversion}-automat
BuildRequires: python%{python3_pkgversion}-azure-common
BuildRequires: python%{python3_pkgversion}-azure-keyvault
BuildRequires: python%{python3_pkgversion}-azure-nspkg
BuildRequires: python%{python3_pkgversion}-cachetools
BuildRequires: python%{python3_pkgversion}-certifi
BuildRequires: python%{python3_pkgversion}-cffi
BuildRequires: python%{python3_pkgversion}-constantly
BuildRequires: python%{python3_pkgversion}-cryptography
BuildRequires: python%{python3_pkgversion}-daphne
BuildRequires: python%{python3_pkgversion}-dateutil
BuildRequires: python%{python3_pkgversion}-defusedxml
BuildRequires: python%{python3_pkgversion}-dictdiffer
BuildRequires: python%{python3_pkgversion}-docutils
BuildRequires: python%{python3_pkgversion}-future
BuildRequires: python%{python3_pkgversion}-gitdb
BuildRequires: python%{python3_pkgversion}-google-auth
BuildRequires: python%{python3_pkgversion}-hyperlink
BuildRequires: python%{python3_pkgversion}-idna
BuildRequires: python%{python3_pkgversion}-importlib_metadata
BuildRequires: python%{python3_pkgversion}-importlib_resources
BuildRequires: python%{python3_pkgversion}-incremental
BuildRequires: python%{python3_pkgversion}-inflect
BuildRequires: python%{python3_pkgversion}-irc
BuildRequires: python%{python3_pkgversion}-isodate
BuildRequires: python%{python3_pkgversion}-jaraco-classes
BuildRequires: python%{python3_pkgversion}-jaraco-collections
BuildRequires: python%{python3_pkgversion}-jaraco-functools
BuildRequires: python%{python3_pkgversion}-jaraco-itertools
BuildRequires: python%{python3_pkgversion}-jaraco-logging
BuildRequires: python%{python3_pkgversion}-jaraco-stream
BuildRequires: python%{python3_pkgversion}-jaraco-text
BuildRequires: python%{python3_pkgversion}-jsonpickle
BuildRequires: python%{python3_pkgversion}-jsonschema
BuildRequires: python%{python3_pkgversion}-kombu
BuildRequires: python%{python3_pkgversion}-kubernetes
BuildRequires: python%{python3_pkgversion}-markupsafe
BuildRequires: python%{python3_pkgversion}-msrest
BuildRequires: python%{python3_pkgversion}-msrestazure
BuildRequires: python%{python3_pkgversion}-pexpect
BuildRequires: python%{python3_pkgversion}-psutil
BuildRequires: python%{python3_pkgversion}-ptyprocess
BuildRequires: python%{python3_pkgversion}-pyasn1
BuildRequires: python%{python3_pkgversion}-pyasn1-modules
# Renamed from PyYAML for RHEL
BuildRequires: python%{python3_pkgversion}-pyyaml
BuildRequires: python%{python3_pkgversion}-openid
BuildRequires: python%{python3_pkgversion}-pytz
BuildRequires: python%{python3_pkgversion}-requests
BuildRequires: python%{python3_pkgversion}-requests-oauthlib
BuildRequires: python%{python3_pkgversion}-six >= 1.13.0
BuildRequires: python%{python3_pkgversion}-smmap
BuildRequires: python%{python3_pkgversion}-social-auth-core
BuildRequires: python%{python3_pkgversion}-tempora
BuildRequires: python%{python3_pkgversion}-twilio
BuildRequires: python%{python3_pkgversion}-twisted >= 19.1.0
BuildRequires: python%{python3_pkgversion}-txaio
BuildRequires: python%{python3_pkgversion}-urllib3
BuildRequires: python%{python3_pkgversion}-vine
BuildRequires: python%{python3_pkgversion}-websocket-client
BuildRequires: python%{python3_pkgversion}-xmlsec
BuildRequires: python%{python3_pkgversion}-zipp >= 0.6.0
BuildRequires: python%{python3_pkgversion}-zope-interface >= 4.7.1

BuildRequires: python%{python3_pkgversion}-GitPython
BuildRequires: python%{python3_pkgversion}-ansible-runner
BuildRequires: python%{python3_pkgversion}-build
BuildRequires: python%{python3_pkgversion}-celery
BuildRequires: python%{python3_pkgversion}-channels
BuildRequires: python%{python3_pkgversion}-chardet
BuildRequires: python%{python3_pkgversion}-devel
# Named as lower case "django" in RHEL
BuildRequires: python%{python3_pkgversion}-django
BuildRequires: python%{python3_pkgversion}-django-auth-ldap
BuildRequires: python%{python3_pkgversion}-django-cors-headers
BuildRequires: python%{python3_pkgversion}-django-crum
BuildRequires: python%{python3_pkgversion}-django-extensions
# Renamed with django prefix
BuildRequires: python%{python3_pkgversion}-django-jsonbfield
BuildRequires: python%{python3_pkgversion}-django-jsonfield
BuildRequires: python%{python3_pkgversion}-django-oauth-toolkit
BuildRequires: python%{python3_pkgversion}-django-pglocks
BuildRequires: python%{python3_pkgversion}-django-polymorphic
BuildRequires: python%{python3_pkgversion}-django-solo
BuildRequires: python%{python3_pkgversion}-django-taggit
BuildRequires: python%{python3_pkgversion}-djangorestframework
BuildRequires: python%{python3_pkgversion}-djangorestframework-yaml
BuildRequires: python%{python3_pkgversion}-jinja2
BuildRequires: python%{python3_pkgversion}-ldap
BuildRequires: python%{python3_pkgversion}-more-itertools
BuildRequires: python%{python3_pkgversion}-oauthlib
BuildRequires: python%{python3_pkgversion}-pip
BuildRequires: python%{python3_pkgversion}-psycopg2
BuildRequires: python%{python3_pkgversion}-pygerduty
BuildRequires: python%{python3_pkgversion}-pygments
# Renamed from PyJWT for RHEL
BuildRequires: python%{python3_pkgversion}-pyjwt >= 1.7.1
BuildRequires: python%{python3_pkgversion}-pyparsing
BuildRequires: python%{python3_pkgversion}-pytest-runner >= 1.4.4
BuildRequires: python%{python3_pkgversion}-python-logstash
BuildRequires: python%{python3_pkgversion}-requests-futures
BuildRequires: python%{python3_pkgversion}-slackclient
BuildRequires: python%{python3_pkgversion}-social-auth-app-django
BuildRequires: python%{python3_pkgversion}-sqlparse

Requires: bubblewrap
Requires: curl
Requires: git
Requires: libcurl-devel
Requires: libffi-devel
Requires: libtool-ltdl-devel
Requires: libxslt-devel
Requires: openldap-devel
Requires: postgresql-devel >= 10
Requires: sshpass
Requires: subversion
Requires: xmlsec1-devel
Requires: xmlsec1-openssl-devel

Requires: python%{python3_pkgversion}-PyHamcrest
Requires: python%{python3_pkgversion}-PyYAML
Requires: python%{python3_pkgversion}-adal
Requires: python%{python3_pkgversion}-ansible-runner
Requires: python%{python3_pkgversion}-attrs
Requires: python%{python3_pkgversion}-autobahn
Requires: python%{python3_pkgversion}-azure-common
Requires: python%{python3_pkgversion}-azure-keyvault
Requires: python%{python3_pkgversion}-azure-nspkg
Requires: python%{python3_pkgversion}-build
Requires: python%{python3_pkgversion}-celery
Requires: python%{python3_pkgversion}-certifi
Requires: python%{python3_pkgversion}-cffi
Requires: python%{python3_pkgversion}-channels
Requires: python%{python3_pkgversion}-chardet
Requires: python%{python3_pkgversion}-constantly
Requires: python%{python3_pkgversion}-cryptography
Requires: python%{python3_pkgversion}-daphne
Requires: python%{python3_pkgversion}-dateutil
Requires: python%{python3_pkgversion}-devel
# Named as lower case "django" in RHEL
Requires: python%{python3_pkgversion}-django
Requires: python%{python3_pkgversion}-django-auth-ldap
Requires: python%{python3_pkgversion}-django-cors-headers
Requires: python%{python3_pkgversion}-django-crum
Requires: python%{python3_pkgversion}-django-extensions
Requires: python%{python3_pkgversion}-django-jsonfield
# Renamed with django prefix
Requires: python%{python3_pkgversion}-django-jsonbfield
Requires: python%{python3_pkgversion}-django-oauth-toolkit
Requires: python%{python3_pkgversion}-django-pglocks
Requires: python%{python3_pkgversion}-django-polymorphic
Requires: python%{python3_pkgversion}-django-solo
Requires: python%{python3_pkgversion}-django-taggit
Requires: python%{python3_pkgversion}-djangorestframework
Requires: python%{python3_pkgversion}-djangorestframework-yaml
Requires: python%{python3_pkgversion}-gitdb
Requires: python%{python3_pkgversion}-GitPython
Requires: python%{python3_pkgversion}-google-auth
Requires: python%{python3_pkgversion}-idna
Requires: python%{python3_pkgversion}-importlib_metadata
Requires: python%{python3_pkgversion}-incremental
Requires: python%{python3_pkgversion}-inflect
Requires: python%{python3_pkgversion}-irc
Requires: python%{python3_pkgversion}-isodate
Requires: python%{python3_pkgversion}-jaraco-classes
Requires: python%{python3_pkgversion}-jaraco-collections
Requires: python%{python3_pkgversion}-jaraco-functools
Requires: python%{python3_pkgversion}-jaraco-itertools
Requires: python%{python3_pkgversion}-jaraco-logging
Requires: python%{python3_pkgversion}-jaraco-stream
Requires: python%{python3_pkgversion}-jaraco-text
Requires: python%{python3_pkgversion}-jinja2
Requires: python%{python3_pkgversion}-jsonschema
Requires: python%{python3_pkgversion}-kombu
Requires: python%{python3_pkgversion}-kubernetes
Requires: python%{python3_pkgversion}-ldap
Requires: python%{python3_pkgversion}-markupsafe
Requires: python%{python3_pkgversion}-more-itertools
Requires: python%{python3_pkgversion}-msrest
Requires: python%{python3_pkgversion}-msrestazure
Requires: python%{python3_pkgversion}-oauthlib
Requires: python%{python3_pkgversion}-openid
Requires: python%{python3_pkgversion}-pexpect
Requires: python%{python3_pkgversion}-pip
Requires: python%{python3_pkgversion}-psutil
Requires: python%{python3_pkgversion}-psycopg2
Requires: python%{python3_pkgversion}-ptyprocess
Requires: python%{python3_pkgversion}-pyasn1
Requires: python%{python3_pkgversion}-pyasn1-modules
Requires: python%{python3_pkgversion}-pygerduty
Requires: python%{python3_pkgversion}-pygments
# Renamed from PyJWT for RHEL
Requires: python%{python3_pkgversion}-pyjwt >= 1.7.1
Requires: python%{python3_pkgversion}-pyparsing
Requires: python%{python3_pkgversion}-python-logstash
Requires: python%{python3_pkgversion}-pytz
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-requests-futures
Requires: python%{python3_pkgversion}-requests-oauthlib
Requires: python%{python3_pkgversion}-runtime
Requires: python%{python3_pkgversion}-six >= 1.13.0
Requires: python%{python3_pkgversion}-slackclient
Requires: python%{python3_pkgversion}-smmap
Requires: python%{python3_pkgversion}-social-auth-app-django
Requires: python%{python3_pkgversion}-social-auth-core
Requires: python%{python3_pkgversion}-tempora
Requires: python%{python3_pkgversion}-twilio
Requires: python%{python3_pkgversion}-twisted >= 19.1.0
Requires: python%{python3_pkgversion}-txaio
Requires: python%{python3_pkgversion}-urllib3
Requires: python%{python3_pkgversion}-websocket_client
Requires: python%{python3_pkgversion}-wheel >= 0.33.6
Requires: python%{python3_pkgversion}-zipp >= 0.6.0
Requires: python%{python3_pkgversion}-zope-interface >= 4.7.1

Requires(pre): /usr/sbin/useradd, /usr/bin/getent
%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx-%{awx_mainversion}

%install
# Setup build environment
#pip-%{python3_pkgversion} install --root=$RPM_BUILD_ROOT .
%{py3_install}

# Collect django static
cat > _awx_rpmbuild_collectstatic_settings.py <<EOF
from awx.settings.defaults import *
DEFAULTS_SNAPSHOT = {}
STATIC_ROOT = "static/"
LOG_AGGREGATOR_AUDIT = False
EOF

export DJANGO_SETTINGS_MODULE="_awx_rpmbuild_collectstatic_settings"
export PYTHONPATH="$PYTHONPATH:."
%{__install} -d -m 755 static/

%{python3} "$RPM_BUILD_ROOT%{_bindir}/awx-manage collectstatic --noinput --clear"

# Cleanup
unset PYTHONPATH
unset DJANGO_SETTINGS_MODULE

%{__install} -d %{buildroot}%{service_homedir}
%{__install} -d %{buildroot}%{service_logdir}
%{__install} -d %{buildroot}%{_prefix}/bin
%{__install} -d %{buildroot}%{service_configdir}
%{__install} -d %{buildroot}/var/lib/awx/
echo %{aws_mainversion} > %{buildroot}%{service_homedir}/.tower_version

%{__install} %{_sourcedir}/settings.py.dist %{buildroot}%{service_configdir}/settings.py
%{__mv} static %{buildroot}%{_prefix}/static

%if 0%{?el7}
# Install systemd configuration
%{__install} -d %{buildroot}%{_unitdir}
for service in awx-cbreceiver awx-dispatcher awx-channels-worker awx-daphne awx-web awx; do
    %{__install} %{_sourcedir}/${service}.service %{buildroot}%{_unitdir}/
done
%endif

# Create fake python executable
cat > %{buildroot}%{_bindir}/python <<"EOF"
#!/bin/sh
export AWX_SETTINGS_FILE=/etc/tower/settings.py
%{python3} \"$@\""
EOF

# Create Virtualenv folder
%{__install} -d -m755 %{buildroot}/var/lib/awx/venv

# Install docs
%{__install} %{_sourcedir}/nginx.conf.example ./

# Install VENV Script
%{__install} -m755 %{_sourcedir}/awx-create-venv $RPM_BUILD_ROOT%{_bindir}/
sed -i 's|#!/usr/bin/python$|#!%{__python3}|g' "$RPM_BUILD_ROOT%{_bindir}/awx-create-venv"
%{__install} -d -m755 $RPM_BUILD_ROOT%{service_homedir}/venv

%{__install} %{_sourcedir}/awx-rpm-logo.svg $RPM_BUILD_ROOT/opt/awx/static/assets/awx-rpm-logo.svg
%{__mv} $RPM_BUILD_ROOT/opt/awx/static/assets/logo-header.svg $RPM_BUILD_ROOT/opt/awx/static/assets/logo-header.svg.orig
%{__mv} $RPM_BUILD_ROOT/opt/awx/static/assets/logo-login.svg $RPM_BUILD_ROOT/opt/awx/static/assets/logo-login.svg.orig
%{__ln_s} /opt/awx/static/assets/awx-rpm-logo.svg $RPM_BUILD_ROOT/opt/awx/static/assets/logo-header.svg
%{__ln_s} /opt/awx/static/assets/awx-rpm-logo.svg $RPM_BUILD_ROOT/opt/awx/static/assets/logo-login.svg

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%post
%if 0%{?el7}
%systemd_post awx-cbreceiver
%systemd_post awx-dispatcher
%systemd_post awx-channels-worker
%systemd_post awx-daphne
%systemd_post awx-web
%endif
# Create symlink to /var/lib/awx/venv/awx as needed

%preun
%if 0%{?el7}
%systemd_preun awx-cbreceiver
%systemd_preun awx-dispatcher
%systemd_preun awx-channels-worker
%systemd_preun awx-daphne
%systemd_preun awx-web
%endif

%postun
%if 0%{?el7}
%systemd_postun awx-cbreceiver
%systemd_postun awx-dispatcher
%systemd_postun awx-channels-worker
%systemd_postun awx-daphne
%systemd_postun awx-web
%endif

%clean

%files
%defattr(0644, awx, awx, 0755)
%doc nginx.conf.example
%attr(0755, root, root) %{_bindir}/awx-manage
%attr(0755, root, root) %{_bindir}/awx-create-venv
%{_bindir}/awx-create-venv
%{python3_sitelib}/awx
%attr(0755, root, root) %{python3_sitelib}/awx/plugins/*/*.py
%attr(0755, awx, awx) %{_prefix}/static
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
%{service_homedir}/.tower_version
%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config %{service_configdir}/settings.py
%{python3_sitelib}/awx-*.egg-info/
/usr/share/doc/awx/
/opt/awx/bin/python
%{_bindir}/ansible-tower-service
%{_bindir}/ansible-tower-setup
%{_bindir}/awx-python
%{_bindir}/failure-event-handler
/usr/share/awx
/usr/share/sosreport/sos/plugins/tower.py
/var/lib/awx/favicon.ico
/var/lib/awx/wsgi.py

%if 0%{?el7}
%attr(0644, root, root) %{_unitdir}/awx-cbreceiver.service
%attr(0644, root, root) %{_unitdir}/awx-dispatcher.service
%attr(0644, root, root) %{_unitdir}/awx-channels-worker.service
%attr(0644, root, root) %{_unitdir}/awx-daphne.service
%attr(0644, root, root) %{_unitdir}/awx-web.service
%attr(0644, root, root) %{_unitdir}/awx.service
%endif

%changelog
