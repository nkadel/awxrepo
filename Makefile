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

EPELPKGS+=http-parser-srpm
EPELPKGS+=meson-srpm

# Confusing sources for build module
#EPELPKGS+=python-build-srpm

# uncertain requirements
#EPELPKGS+=python-pkgconfig-srpm
#EPELPKGS+=python-pytest-xdist-srpm

# python3 only update modules for version sensitive python-six
EPELPKGS+=python3-six-srpm

EPELPKGS+=python-adal-srpm
EPELPKGS+=python-async-generator-srpm
EPELPKGS+=python-attrs-srpm
EPELPKGS+=python-azure-common-srpm
EPELPKGS+=python-azure-core-srpm
EPELPKGS+=python-azure-keyvault-keys-srpm
EPELPKGS+=python-azure-keyvault-secrets-srpm
EPELPKGS+=python-azure-keyvault-srpm
EPELPKGS+=python-azure-nspkg-srpm
EPELPKGS+=python-channels-srpm
EPELPKGS+=python-colorama-srpm
EPELPKGS+=python-commonmark-srpm
EPELPKGS+=python-contextlib2-srpm
EPELPKGS+=python-contextvars-srpm
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
EPELPKGS+=python-django-split_settings-srpm
EPELPKGS+=python-django-taggit-srpm
EPELPKGS+=python-djangorestframework-srpm
EPELPKGS+=python-djangorestframework-yaml-srpm
EPELPKGS+=python-docutils-srpm
EPELPKGS+=python-docutils-stubs-srpm
EPELPKGS+=python-func_timeout-srpm
EPELPKGS+=python-funcsigs-srpm
EPELPKGS+=python-idna-ssl-srpm
EPELPKGS+=python-immutables-srpm
EPELPKGS+=python-inflect-srpm
EPELPKGS+=python-irc-srpm
EPELPKGS+=python-jaraco-collections-srpm
EPELPKGS+=python-jaraco-logging-srpm
EPELPKGS+=python-jaraco-packaging-srpm
EPELPKGS+=python-jaraco-text-srpm
EPELPKGS+=python-kombu-srpm
EPELPKGS+=python-lockfile-srpm
EPELPKGS+=python-more-itertools-srpm
EPELPKGS+=python-msrestazure-srpm
EPELPKGS+=python-mypy-extensions-srpm
EPELPKGS+=python-oauth2_provider-srpm
EPELPKGS+=python-path-srpm
EPELPKGS+=python-process-tests-srpm
EPELPKGS+=python-ptyprocess-srpm
EPELPKGS+=python-pyasn1-srpm
EPELPKGS+=python-pycares-srpm
EPELPKGS+=python-pyenchant-srpm
EPELPKGS+=python-pygerduty-srpm
EPELPKGS+=python-pyjwt-srpm
EPELPKGS+=python-pyrsistent-srpm
EPELPKGS+=python-pytest-aiohttp-srpm
EPELPKGS+=python-python-logstash-srpm
EPELPKGS+=python-python-mimeparse-srpm
EPELPKGS+=python-python3-openid-srpm
EPELPKGS+=python-python3-saml-srpm
EPELPKGS+=python-recommonmark-srpm
#EPELPKGS+=python-repoze-sphinx-autointerface-srpm
EPELPKGS+=python-requests-futures-srpm
EPELPKGS+=python-rst-linker-srpm
EPELPKGS+=python-setuptools_git-srpm
EPELPKGS+=python-setuptools_scm-srpm
EPELPKGS+=python-simplejson-srpm
EPELPKGS+=python-smmap-srpm
EPELPKGS+=python-social-auth-app-django-srpm
EPELPKGS+=python-sortedcontainers-srpm
EPELPKGS+=python-sphinx-rst-builder-srpm
EPELPKGS+=python-sphinx-tabs-srpm
EPELPKGS+=python-termcolor-srpm
EPELPKGS+=python-typing-extensions-srpm
EPELPKGS+=python-typing-srpm
EPELPKGS+=python-vine-srpm
EPELPKGS+=python-websocket_client-srpm
EPELPKGS+=python-xmlsec-srpm

# Depends on mypy-extensions
AWXPKGS+=python-mypy-srpm

## Depends on mypy, docutils-stubs
#AWXPKGS+=python-sphinxcontrib-applehelp-srpm
#AWXPKGS+=python-sphinxcontrib-devhelp-srpm
#
#AWXPKGS+=python-sphinxcontrib-htmlhelp-srpm
#AWXPKGS+=python-sphinxcontrib-jsmath-srpm
#AWXPKGS+=python-sphinxcontrib-qthelp-srpm
#AWXPKGS+=python-sphinxcontrib-serializinghtml-srpm
#
# Depends on importlib-metadata, pyenchant
AWXPKGS+=python-sphinxcontrib-spelling-srpm

## Depends on sphinxcontrib-*
#AWXPKGS+=python-sphinx-srpm

# Depends on sphinxcontrib-spelling, sphinx-rst-builder, sphinx-tabs
AWXPKGS+=python-coverage-srpm

# Depends on repoze-sphinx-autointerface, coverage
AWXPKGS+=python-zope-interface-srpm

# Depends on sure
AWXPKGS+=python-httpretty-srpm

# Depends on chardet
AWXPKGS+=python-feedparser-srpm

# Depends on contextlib2, setuptools_git, termcolor
AWXPKGS+=python-pytest-shutil-srpm

# Depends on setuptools_git
AWXPKGS+=python-pytest-fixture-config-srpm

# Depends on path and contextlib2 and
AWXPKGS+=python-pytest-virtualenv-srpm

# bootstrup updated setuptools, depends on python2-futures,
# virtualenv, mock, pytest-fixture-config
AWXPKGS+=python-setuptools-srpm

# python3 only update for pytest modules of misnmed source package
# Depends on more-itertools, upstream pluggy 0.6, not local updated version
AWXPKGS+=pytest-srpm

# Updated pytest for 3.6.x dependencies
# Depends on more-itertools, atomicwrites, colorama, funcsigs
AWXPKGS+=pytest-3.6.x-srpm

# Depends on more-itertools
AWXPKGS+=python-outcome-srpm

# Depends on jaraco-packaging
AWXPKGS+=python-pytest-black-multiply-srpm

# Depends on process-tests, pytest-xdist
AWXPKGS+=python-pytest-cov-srpm

# Depends on setuptools_scm
AWXPKGS+=python-importlib_resources-srpm

# Depnds on python3-saml, python3-openid
AWXPKGS+=python-social-auth-core-srpm

# Depends on pycares
AWXPKGS+=python-aiodns-srpm

# Depends on curio, contextvars
AWXPKGS+=python-sniffio-srpm

# Depends on pytest, Cython, multidict, more-itertools
AWXPKGS+=python-yarl-srpm

# Depends on aiohttp, pyttest-aiohttp
AWXPKGS+=python-async-timeout-srpm

# Depends on aiohttp, which Requires yarl, async-timeout
AWXPKGS+=python-black-srpm

# Depends on aiodns, aiohttp, black
AWXPKGS+=python-slackclient-srpm

# Depends on pyjwt
AWXPKGS+=python-twilio-srpm

# Depends on pytest, entrypoints
AWXPKGS+=python-pytest-flake8-srpm

# Depends on jaraco-packaging, setuptools_scm
AWXPKGS+=python-jaraco-itertools-srpm

# Depends on zipp
AWXPKGS+=python-importlib-metadata-srpm

# Depends on sphinxcontrib-*
AWXPKGS+=python-sphinx-srpm

# Depends on pytest-black, pytest = 3.5.0
AWXPKGS+=python-pytest-black-srpm

# Depends on pytest, importlib-metadata, jaraco-packaging ane
# pytest-black-multiply, pytest-checkdocs, pytest-cov and
# pytest-flake8, rst-linker, setuptools_scm, pytest-black

# Disable temporarily
AWXPKGS+=python-pytest-checkdocs-srpm

# Depends on black-multiply, checkdocs
AWXPKGS+=python-jaraco-stream-srpm

# Depends on importlib-metadata
AWXPKGS+=python-pluggy-srpm

# Depends on ptyprocess, pluggy
AWXPKGS+=python-pexpect-srpm

# Depends on pytest, pytest-flake8, setuptools_scm, more-itertools
AWXPKGS+=python-jaraco-classes-srpm

# Depends on jaraco-packaging, jaraco-classes, pytest-flske8
AWXPKGS+=python-jaraco-functools-srpm

AWXPKGS+=python-fixtures-srpm
AWXPKGS+=python-testscenario-srpm

# Depends on pytest-flake8, jaraco-functools
AWXPKGS+=python-tempora-srpm

# Depends on django-extensions, coverage
AWXPKGS+=python-django-formtools-srpm

# Depends on pytest, and pytest-asyncio, async-timeout
AWXPKGS+=python-asgiref-srpm

# Depends on django, django-formtools
AWXPKGS+=python-django-jsonfield-srpm

AWXPKGS+=python-service-identity-srpm

# Depends on pytest, service-dentity
AWXPKGS+=python-trustme-srpm

# Depends on attrs, pytest, pytest-asyncio, more-itertools, 
AWXPKGS+=python-outcome-srpm

# Depends on trustme, outcome
AWXPKGS+=python-trio-srpm

# Depends on aiodns, httpretty, pytest, recommonmark, trio
AWXPKGS+=python-msrest-srpm

AWXPKGS+=ansible-awx-srpm

REPOS+=awxrepo/el/8
#REPOS+=awxrepo/fedora/32

REPODIRS := $(patsubst %,%/x86_64/repodata,$(REPOS)) $(patsubst %,%/SRPMS/repodata,$(REPOS))

CFGS+=awxrepo-8-x86_64.cfg
#CFGS+=awxrepo-f32-x86_64.cfg

# Link from /etc/mock
MOCKCFGS+=epel-8-x86_64.cfg
#MOCKCFGS+=fedora-32-x86_64.cfg

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
#awx:: epel
awx:: $(AWXPKGS)

.PHONY: cfg
cfg:: cfgs

.PHONY: cfgs
cfgs: $(CFGS) $(MOCKCFGS)

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
	@echo 'metadata_expire=1' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo "best=0" >> $@
	@echo '"""' >> $@

#awxrepo-f32-x86_64.cfg: /etc/mock/fedora-32-x86_64.cfg
#	@echo Generating $@ from $?
#	@cat $? > $@
#	@sed -i 's/fedora-32-x86_64/awxrepo-f32-x86_64/g' $@
#	@echo >> $@
#	@echo "Disabling 'best=' for $@"
#	@sed -i '/^best=/d' $@
#	@echo "best=0" >> $@
#	@echo >> $@
#	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
#	@echo '[awxrepo]' >> $@
#	@echo 'name=awxrepo' >> $@
#	@echo 'enabled=1' >> $@
#	@echo 'baseurl=$(REPOBASE)/awxrepo/fedora/32/x86_64/' >> $@
#	@echo 'failovermethod=priority' >> $@
#	@echo 'skip_if_unavailable=False' >> $@
#	@echo 'metadata_expire=1' >> $@
#	@echo 'gpgcheck=0' >> $@
#	@echo '#cost=2000' >> $@
#	@echo "best=0" >> $@
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
