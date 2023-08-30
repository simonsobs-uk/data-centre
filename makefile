SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = dist/docs

# for bump2version, valid options are: major, minor, patch
PART ?= patch

PORT ?= 8099
DOC_DEP = $(shell find docs -type f \( -name '*.md' -o -name '*.rst' \)) $(shell find src -type f -name '*.py')

# documentation ################################################################

.PHONY: all doc epub
all: doc epub pdf
doc: dist/docs/.sentinel
epub: dist/docs/SOUKDataCentre.epub
pdf: dist/docs/latex/soukdatacentre.pdf

dist/docs/.sentinel: $(DOC_DEP)
	@$(SPHINXBUILD) -b dirhtml "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	touch $@
dist/docs/SOUKDataCentre.epub: $(DOC_DEP)
	@$(SPHINXBUILD) -b epub "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
dist/docs/latex/soukdatacentre.pdf: $(DOC_DEP)
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

.PHONY: serve
serve: doc
	sphinx-autobuild \
		-b dirhtml $(SPHINXOPTS) \
		--port $(PORT) \
		--open-browser \
		--delay 0 \
		"$(SOURCEDIR)" "$(BUILDDIR)"

# releasing ####################################################################

.PHONY: bump
bump:
	bump2version $(PART)
	git push --follow-tags

################################################################################

.PHONY: clean
clean:
	rm -rf dist

print-%:
	$(info $* = $($*))
