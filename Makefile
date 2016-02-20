PLATFORM = $(shell uname)
TRAVIS_REPO_SLUG = gutomaia/gutomaia.github.com
GH_TOKEN ?= secret

BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/site/output
GITHUB_PAGES_BRANCH=master

PYTHON_MODULES=site

OK=\033[32m[OK]\033[39m
FAIL=\033[31m[FAIL]\033[39m
CHECK=@if [ $$? -eq 0 ]; then echo "${OK}"; else echo "${FAIL}" ; fi

WGET = wget -q 

default: python.mk
	@$(MAKE) -C . build

ifeq "true" "${shell test -f python.mk && echo true}"
include python.mk
endif

python.mk:
	@${WGET} https://raw.githubusercontent.com/gutomaia/makery/master/python.mk && \
		touch $@

clean: python_clean

purge: python_purge
	@rm python.mk
	@rm -rf .tox

publish:
	${VIRTUALENV} $(MAKE) -C site publish

build: python_build ${REQUIREMENTS} publish

github: build
	${VIRTUALENV} ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	@git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git master > /dev/null
