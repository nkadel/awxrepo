#
# Makefile - build wrapper for awx
#
#	git clone RHEL 6 SRPM building tools from
#	https://github.com/nkadel/[package] into designated
#	AWXPKGS below
#
#	Set up local

#REPOBASE=http://localhost
REPOBASE=file://$(PWD)

# Dependency metapackage
#EPELPKGS+=PyYAML-srpm

EPELPKGS+=Cython-srpm
EPELPKGS+=http-parser-srpm
EPELPKGS+=meson-srpm

# RHEL name funkiness for python-pyflakes
EPELPKGS+=pyflakes-srpm

# RHEL packages do not currently "provide"  python2- dependendcies
EPELPKGS+=python2-lockfile-srpm
EPELPKGS+=python2-sphinx-srpm

# python3 only update modules for version sensitive python-six
EPELPKGS+=python3-six-srpm
# python3 named package from EPEL 8 backported to EPEL 7
EPELPKGS+=python3-chardet-srpm

EPELPKGS+=python-adal-srpm
EPELPKGS+=python-amqp-srpm
EPELPKGS+=python-async-generator-srpm
EPELPKGS+=python-atomicwrites-srpm
EPELPKGS+=python-azure-common-srpm
EPELPKGS+=python-azure-core-srpm
EPELPKGS+=python-azure-keyvault-keys-srpm
EPELPKGS+=python-azure-keyvault-secrets-srpm
EPELPKGS+=python-azure-keyvault-srpm
EPELPKGS+=python-azure-nspkg-srpm
EPELPKGS+=python-billiard-srpm
EPELPKGS+=python-build-srpm
EPELPKGS+=python-celery-srpm
EPELPKGS+=python-channels-srpm
EPELPKGS+=python-colorama-srpm
EPELPKGS+=python-commonmark-srpm
EPELPKGS+=python-contextlib2-srpm
EPELPKGS+=python-contextvars-srpm
EPELPKGS+=python-coverage-srpm
EPELPKGS+=python-curio-srpm
EPELPKGS+=python-daphne-srpm
EPELPKGS+=python-demjson-srpm
EPELPKGS+=python-django-auth-ldap-srpm
EPELPKGS+=python-django-cors-headers-srpm
EPELPKGS+=python-django-crum-srpm
EPELPKGS+=python-django-extensions-srpm
EPELPKGS+=python-django-jsonbfield-srpm
EPELPKGS+=python-django-oauth-toolkit-srpm
EPELPKGS+=python-django-pglocks-srpm
EPELPKGS+=python-django-polymorphic-srpm
EPELPKGS+=python-django-solo-srpm
EPELPKGS+=python-django-taggit-srpm
EPELPKGS+=python-djangorestframework-srpm
EPELPKGS+=python-djangorestframework-yaml-srpm
EPELPKGS+=python-docutils-srpm
EPELPKGS+=python-entrypoints-srpm
EPELPKGS+=python-extras-srpm
EPELPKGS+=python-func_timeout-srpm
EPELPKGS+=python-futures-srpm
EPELPKGS+=python-gitdb-srpm
EPELPKGS+=python-idna-ssl-srpm
EPELPKGS+=python-immutables-srpm
EPELPKGS+=python-inflect-srpm
EPELPKGS+=python-irc-srpm
EPELPKGS+=python-isodate-srpm
EPELPKGS+=python-jaraco-collections-srpm
EPELPKGS+=python-jaraco-logging-srpm
EPELPKGS+=python-jaraco-packaging-srpm
EPELPKGS+=python-jaraco-text-srpm
EPELPKGS+=python-kombu-srpm
EPELPKGS+=python-lockfile-srpm
EPELPKGS+=python-memcached-srpm
EPELPKGS+=python-more-itertools-srpm
EPELPKGS+=python-msrestazure-srpm
EPELPKGS+=python-path-srpm
EPELPKGS+=python-process-tests-srpm
EPELPKGS+=python-ptyprocess-srpm
EPELPKGS+=python-py-srpm
EPELPKGS+=python-pyasn1-srpm
EPELPKGS+=python-pycares-srpm
EPELPKGS+=python-pygerduty-srpm
EPELPKGS+=python-pyjwt-srpm
EPELPKGS+=python-pyrsistent-srpm
EPELPKGS+=python-pytest-aiohttp-srpm
EPELPKGS+=python-pytest-param-srpm
EPELPKGS+=python-python-logstash-srpm
EPELPKGS+=python-python-mimeparse-srpm
EPELPKGS+=python-python3-openid-srpm
EPELPKGS+=python-recommonmark-srpm
EPELPKGS+=python-requests-futures-srpm
EPELPKGS+=python-rst-linker-srpm
EPELPKGS+=python-selenium-srpm
EPELPKGS+=python-setuptools_git-srpm
EPELPKGS+=python-setuptools_scm-srpm
EPELPKGS+=python-simplejson-srpm
EPELPKGS+=python-smmap-srpm
EPELPKGS+=python-social-auth-app-django-srpm
EPELPKGS+=python-sortedcontainers-srpm
EPELPKGS+=python-sqlparse-srpm
EPELPKGS+=python-sure-srpm
EPELPKGS+=python-termcolor-srpm
EPELPKGS+=python-typing-extensions-srpm
EPELPKGS+=python-typing-srpm
EPELPKGS+=python-unittest2-srpm
EPELPKGS+=python-vine-srpm
EPELPKGS+=python-websocket_client-srpm
EPELPKGS+=python-xmlsec-srpm
EPELPKGS+=python-zope-interface-srpm

# Depends on isodate and xmsec for RHEL 7
AWXPKGS+=python-python3-saml-srpm

# Depends on coverage for python2 on RHEL 7
AWXPKGS+=python-hypothesis-srpm

# Depends on sure
AWXPKGS+=python-httpretty-srpm

# Depends on chardet
AWXPKGS+=python-feedparser-srpm

# Depends on unittest2 for RHEL 7
AWXPKGS+=python-funcsigs-srpm

# Depends on contextlib2 and setuptools_git and termcolor
AWXPKGS+=python-pytest-shutil-srpm

# Depends on setuptools_git
AWXPKGS+=python-pytest-fixture-config-srpm

# Depends on path and contextlib2 and
AWXPKGS+=python-pytest-virtualenv-srpm

# bootstrup updated setuptools, depends on python2-futures,
# virtualenv, mock, pytest-fixture-config
AWXPKGS+=python-setuptools-srpm

# python3 only update for pytest modules of misnmed source package
# Depends on more-itertools and upstream pluggy 0.6, not local updated version
AWXPKGS+=pytest-srpm

# Updated pytest for 3.6.x dependencies
# Depends on more-itertools and atomicwrites and colorama and funcsigs
AWXPKGS+=pytest-3.6.x-srpm

# Depends on more-itertools
AWXPKGS+=python-outcome-srpm

# Depends on jaraco-packaging
AWXPKGS+=python-pytest-black-multiply-srpm

# Depends on process-tests and pytest-xdist
AWXPKGS+=python-pytest-cov-srpm

# Depends on simplejson and feedparser and demjson
AWXPKGS+=python-jsonpickle-srpm

# Depends on setuptools_scm
AWXPKGS+=python-importlib_resources-srpm

# Depnds on python3-saml and python3-openid
AWXPKGS+=python-social-auth-core-srpm

# Depends on pycares
AWXPKGS+=python-aiodns-srpm

# Depends on curio and contextvars
AWXPKGS+=python-sniffio-srpm

# Depends on hypothesis
AWXPKGS+=python-attrs-srpm

# Depends on pytest
AWXPKGS+=python-sqlparse-srpm

# Depends on http-parser and Cython and yarl and async-timeout
AWXPKGS+=python-aiohttp-srpm

# Depends on pytest and Cython and multidict and more-itertools
AWXPKGS+=python-yarl-srpm

# Depends on aiohttp and pyttest-aiohttp
AWXPKGS+=python-async-timeout-srpm

# Depends on aiohttp, which Requires yarl and async-timeout
AWXPKGS+=python-black-srpm

# Depends on aiodns and aiohttp and black
AWXPKGS+=python-slackclient-srpm

# Depends on ptyprocess and pluggy
AWXPKGS+=python-pexpect-srpm

# Depndes on unittest2
AWXPKGS+=python-case-srpm

# Depnds on isodate
AWXPKGS+=python-rdflib-srpm

# Depends on pyjwt
AWXPKGS+=python-twilio-srpm

# Depends on memcached
AWXPKGS+=python-django-srpm

# Depends on pytest
AWXPKGS+=python-cryptography-srpm

# Depends on pytest and more-itertools
AWXPKGS+=python-multidict-srpm

# Depends on pytest and entrypoints
AWXPKGS+=python-flake8-srpm
AWXPKGS+=python-pytest-flake8-srpm

# Depends on jaraco-packaging and setuptools_scm
AWXPKGS+=python-jaraco-itertools-srpm

# Depends on jaraco-packaging and setuptools_scm and jaraco-itertools and toml
AWXPKGS+=python-zipp-srpm

# Depends on zipp
AWXPKGS+=python-importlib-metadata-srpm

# Depends on pytest-black and pytest = 3.5.0
AWXPKGS+=python-pytest-black-srpm

# Depends on pytest and importlib-metadata and jaraco-packaging ane
# pytest-black-multiply and pytest-checkdocs and pytest-cov and
# pytest-flake8 and rst-linker and setuptools_scm and pytest-black

# Disable temporarily
AWXPKGS+=python-pytest-checkdocs-srpm

# Depends on black-multiply and checkdocs
AWXPKGS+=python-jaraco-stream-srpm

# Depends on importlib-metadata
AWXPKGS+=python-pluggy-srpm

# Depends on pytest and pytest-flake8 and setuptools_scm and more-itertools
AWXPKGS+=python-jaraco-classes-srpm

# Depends on jaraco-packaging and jaraco-classes and pytest-flske8
AWXPKGS+=python-jaraco-functools-srpm

AWXPKGS+=python-testtools-srpm
AWXPKGS+=python-fixtures-srpm
AWXPKGS+=python-testscenario-srpm
AWXPKGS+=python-daemon-srpm

# Depends on flake8 and pytest-flake8 and jaraco-functools
AWXPKGS+=python-tempora-srpm

# Depends on django-extensions and coverage and flake8
AWXPKGS+=python-django-formtools-srpm

# Depends on coverage and async-generator and hypothesis
AWXPKGS+=python-pytest-asyncio-srpm

# Depends on pytest and and pytest-asyncio and async-timeout
AWXPKGS+=python-asgiref-srpm

# Depends on django and django-formtools
AWXPKGS+=python-django-jsonfield-srpm

AWXPKGS+=python-service-identity-srpm

# Depends on pytest and service-identity
AWXPKGS+=python-ansible-runner-srpm

# Depends on pytest and service-dentity
AWXPKGS+=python-trustme-srpm

# Depends on attrs and pytest and pytest-asyncio and more-itertools and 
AWXPKGS+=python-outcome-srpm

# Depends on trustme and outcome
AWXPKGS+=python-trio-srpm

# Depends on aiodns and httpretty and pytest and recommonmark and trio
AWXPKGS+=python-msrest-srpm

AWXPKGS+=ansible-awx-srpm

REPOS+=awxrepo/el/7
REPOS+=awxrepo/el/8
#REPOS+=awxrepo/fedora/31

REPODIRS := $(patsubst %,%/x86_64/repodata,$(REPOS)) $(patsubst %,%/SRPMS/repodata,$(REPOS))

CFGS+=awxrepo-7-x86_64.cfg
CFGS+=awxrepo-8-x86_64.cfg
#CFGS+=awxrepo-f31-x86_64.cfg

# Link from /etc/mock
MOCKCFGS+=epel-7-x86_64.cfg
MOCKCFGS+=epel-8-x86_64.cfg
#MOCKCFGS+=fedora-31-x86_64.cfg

install:: $(CFGS)
install:: $(MOCKCFGS)
install:: $(REPODIRS)
install:: $(EPELPKGS)
install:: $(AWXPKGS)

.PHONY: all
all:: install

.PHONY: install clean getsrc src.rpm build 
install clean getsrc src.rpm build::
	@for name in $(EPELPKGS) $(AWXPKGS); do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done

# Actually build in directories
.PHONY: $(EPELPKGS) $(AWXPKGS)
$(EPELPKGS) $(AWXPKGS)::
	(cd $@ && $(MAKE) $(MLAGS) install)

repos: $(REPOS) $(REPODIRS)
$(REPOS):
	install -d -m 755 $@

.PHONY: $(REPODIRS)
$(REPODIRS): $(REPOS)
	@install -d -m 755 `dirname $@`
	/usr/bin/createrepo -q `dirname $@`


epelpkgs: epel
.PHONY: epel
epel:: $(EPELPKGS)

# awx pkgs depend on epelpkgs
awxpkgs: awx
.PHONY: awx
#awx:: epel %(AWXPKGS)
awx: $(AWXPKGS)

.PHONY: cfg
cfg:: cfgs

.PHONY: cfgs
cfgs: $(CFGS) $(MOCKCFGS)

awxrepo-7-x86_64.cfg: /etc/mock/epel-7-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-7-x86_64/awxrepo-7-x86_64/g' $@
	@echo >> $@
	@echo "Disabling 'best=' for $@"
	@sed -i '/^best=/d' $@
	@echo "best=0" >> $@
	@echo >> $@
	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
	@echo '[awxrepo]' >> $@
	@echo 'name=awxrepo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/el/7/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=0' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@

awxrepo-8-x86_64.cfg: /etc/mock/epel-8-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-8-x86_64/awxrepo-8-x86_64/g' $@
	@echo >> $@
	@echo "Disabling 'best=' for $@"
	@sed -i '/^best=/d' $@
	@echo "best=0" >> $@
	@echo >> $@
	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
	@echo '[awxrepo]' >> $@
	@echo 'name=awxrepo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/el/8/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=0' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@

#awxrepo-f31-x86_64.cfg: /etc/mock/fedora-31-x86_64.cfg
#	@echo Generating $@ from $?
#	@cat $? > $@
#	@sed -i 's/fedora-31-x86_64/awxrepo-f31-x86_64/g' $@
#	@echo >> $@
#	@echo "Disabling 'best=' for $@"
#	@sed -i '/^best=/d' $@
#	@echo "best=0" >> $@
#	@echo >> $@
#	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
#	@echo '[awxrepo]' >> $@
#	@echo 'name=awxrepo' >> $@
#	@echo 'enabled=1' >> $@
#	@echo 'baseurl=$(REPOBASE)/awxrepo/fedora/31/x86_64/' >> $@
#	@echo 'failovermethod=priority' >> $@
#	@echo 'skip_if_unavailable=False' >> $@
#	@echo 'metadata_expire=0' >> $@
#	@echo 'gpgcheck=0' >> $@
#	@echo '#cost=2000' >> $@
#	@echo '"""' >> $@

$(MOCKCFGS)::
	ln -sf /etc/mock/$@ $@

repo: awxrepo.repo
awxrepo.repo:: Makefile awxrepo.repo.in
	@if [ -s /etc/fedora-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/fedora/|g" > $@; \
	elif [ -s /etc/redhat-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/el/|g" > $@; \
	else \
		echo Error: unknown release, check /etc/*-release; \
		exit 1; \
	fi

awxrepo.repo::
	@cmp -s $@ /etc/yum.repos.d/$@ || \
	    diff -u $@ /etc/yum.repos.d/$@

clean::
	find . -name \*~ -exec rm -f {} \;
	rm -f *.cfg
	rm -f *.out
	@for name in $(EPELPKGS) $(AWXPKGS); do \
	    $(MAKE) -C $$name $@; \
	done

distclean: clean
	rm -rf awxrepo
	@for name in $(EPELPKGS) $(AWXPKGS); do \
	    $(MAKE) -C $$name $@; \
	done

maintainer-clean: distclean
	git clean -x -d -f .
	@for name in $(EPELPKGS) $(AWXPKGS); do \
	    $(MAKE) -C $$name $@; \
	done
