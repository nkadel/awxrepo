#
# Makefile - build wrapper for Awx RPMs
#

#REOBASEE=http://localhost
REPOBASE=file://$(PWD)

REPOS+=awxrepo/el/8
REPOS+=awxrepo/el/9
REPOS+=awxrepo/el/10
REPOS+=awxrepo/fedora/40
REPOS+=awxrepo/amazon/2023

REPODIRS := $(patsubst %,%/x86_64/repodata,$(REPOS)) $(patsubst %,%/SRPMS/repodata,$(REPOS))

CFGS+=awxrepo-8-x86_64.cfg
CFGS+=awxrepo-9-x86_64.cfg
CFGS+=awxrepo-10-x86_64.cfg
CFGS+=awxrepo-f40-x86_64.cfg
# Amazon 2 023config
CFGS+=awxrepo-amz2023-x86_64.cfg

# /etc/mock version lacks python modules
MOCKCFGS+=centos-stream+epel-8-x86_64.cfg
MOCKCFGS+=centos-stream+epel-9-x86_64.cfg
MOCKCFGS+=centos-stream+epel-10-x86_64.cfg
MOCKCFGS+=fedora-40-x86_64.cfg
MOCKCFGS+=amazonlinux-2023-x86_64.cfg

EPELPKGS+=awx-srpm

# AWX builds on Fedora 40 without more dependencies
#AWXREPOPKGS+=awx-srpm

all:: install

install:: $(CFGS)
install:: $(MOCKCFGS)
install:: $(REPODIRS)
install:: $(EPELPKGS)
install:: $(AWXREPOPKGS)

# Actually put all the modules in the local repo
.PHONY: install clean getsrc build srpm src.rpm
install clean getsrc build srpm src.rpm::
	@for name in $(AWXREPOPKGS); do \
	     (cd $$name && $(MAKE) $(MFLAGS) $@); \
	done  

# Git submodule checkout operation
# For more recent versions of git, use "git checkout --recurse-submodules"
#*-srpm::
#	@[ -d $@/.git ] || \
#	     git submodule update --init $@

# Dependencies of libraries on other libraries for compilation

# Actually build in directories
.PHONY: $(AWXREPOPKGS)
$(AWXREPOPKGS)::
	(cd $@ && $(MAKE) $(MLAGS) install)

repodirs: $(REPOS) $(REPODIRS)
repos: $(REPOS) $(REPODIRS)
$(REPOS):
	install -d -m 755 $@

.PHONY: $(REPODIRS)
$(REPODIRS): $(REPOS)
	@install -d -m 755 `dirname $@`
	/usr/bin/createrepo_c -q `dirname $@`

.PHONY: cfg
cfg:: cfgs

.PHONY: cfgs
cfgs:: $(CFGS)
cfgs:: $(MOCKCFGS)

$(MOCKCFGS)::
	@echo Generating $@ from $?
	@echo "include('/etc/mock/$@')" | tee $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@

# packages-microsoft-com-prod added for /bin/pwsh
awxrepo-8-x86_64.cfg: ./centos-stream+epel-8-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@
	@echo "config_opts['root'] = 'awxrepo-{{ releasever }}-{{ target_arch }}'" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[awxrepo]' | tee -a $@
	@echo 'name=awxrepo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/el/8/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '' | tee -a $@
	@echo '[packages-microsoft-com-prod]' | tee -a $@
	@echo 'name=packages-microsoft-com-prod' | tee -a $@
	@echo 'baseurl=https://packages.microsoft.com/rhel/8/prod/' | tee -a $@
	@echo 'enabled=0' | tee -a $@
	@echo 'gpgcheck=1' | tee -a $@
	@echo 'gpgkey=https://packages.microsoft.com/keys/microsoft.asc' | tee -a $@
	@echo '"""' | tee -a $@

# packages-microsoft-com-prod added for /bin/pwsh
awxrepo-9-x86_64.cfg: centos-stream+epel-9-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@
	@echo "config_opts['root'] = 'awxrepo-{{ releasever }}-{{ target_arch }}'" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[awxrepo]' | tee -a $@
	@echo 'name=awxrepo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/el/9/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '' | tee -a $@
	@echo '[packages-microsoft-com-prod]' | tee -a $@
	@echo 'name=packages-microsoft-com-prod' | tee -a $@
	@echo 'baseurl=https://packages.microsoft.com/rhel/9/prod/' | tee -a $@
	@echo 'enabled=0' | tee -a $@
	@echo 'gpgcheck=1' | tee -a $@
	@echo 'gpgkey=https://packages.microsoft.com/keys/microsoft.asc' | tee -a $@
	@echo '"""' | tee -a $@

# packages-microsoft-com-prod added for /bin/pwsh
awxrepo-10-x86_64.cfg: ./centos-stream+epel-10-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@
	@echo "config_opts['root'] = 'awxrepo-{{ releasever }}-{{ target_arch }}'" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[awxrepo]' | tee -a $@
	@echo 'name=awxrepo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/el/9/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '' | tee -a $@
	@echo '[packages-microsoft-com-prod]' | tee -a $@
	@echo 'name=packages-microsoft-com-prod' | tee -a $@
	@echo 'baseurl=https://packages.microsoft.com/rhel/9/prod/' | tee -a $@
	@echo 'enabled=0' | tee -a $@
	@echo 'gpgcheck=1' | tee -a $@
	@echo 'gpgkey=https://packages.microsoft.com/keys/microsoft.asc' | tee -a $@
	@echo '"""' | tee -a $@

awxrepo-f40-x86_64.cfg: ./fedora-40-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@
	@echo "config_opts['root'] = 'awxrepo-f{{ releasever }}-{{ target_arch }}'" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[awxrepo]' | tee -a $@
	@echo 'name=awxrepo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/fedora/40/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '"""' | tee -a $@

awxrepo-rawhide-x86_64.cfg: ./fedora-rawhide-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@
	@echo "config_opts['root'] = 'awxrepo-rawhide-{{ target_arch }}'" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[awxrepo]' | tee -a $@
	@echo 'name=awxrepo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/fedora/rawhide/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '"""' | tee -a $@

awxrepo-amz2023-x86_64.cfg: ./amazonlinux-2023-x86_64.cfg
	@echo Generating $@ from $?
	@echo "include('$?')" | tee $@
	@echo "config_opts['dnf_vars'] = { 'best': 'False' }" | tee -a $@
	@echo "config_opts['root'] = 'awxrepo-amz2023-{{ target_arch }}'" | tee -a $@
	@echo "config_opts['dnf.conf'] += \"\"\"" | tee -a $@
	@echo '[awxrepo]' | tee -a $@
	@echo 'name=awxrepo' | tee -a $@
	@echo 'enabled=1' | tee -a $@
	@echo 'baseurl=$(REPOBASE)/awxrepo/amazon/2023/x86_64/' | tee -a $@
	@echo 'skip_if_unavailable=False' | tee -a $@
	@echo 'metadata_expire=1s' | tee -a $@
	@echo 'gpgcheck=0' | tee -a $@
	@echo '"""' | tee -a $@

repo: awxrepo.repo
awxrepo.repo:: Makefile awxrepo.repo.in
	if [ -s /etc/fedora-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/fedora/|g" | tee $@; \
	elif [ -s /etc/redhat-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/el/|g" | tee $@; \
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
	@for name in $(AWXREPOPKGS); do \
	    $(MAKE) -C $$name clean; \
	done

distclean: clean
	rm -rf $(REPOS)
	rm -rf awxrepo
	@for name in $(AWXREPOPKGS); do \
	    (cd $$name; git clean -x -d -f); \
	done

maintainer-clean: distclean
	rm -rf $(AWXREPOPKGS)
	@for name in $(AWXREPOPKGS); do \
	    (cd $$name; git clean -x -d -f); \
	done
