PORT ?= 8099
DOC_DEP = $(shell find docs -type f \( -name '*.md' -o -name '*.rst' \)) $(shell find src -type f -name '*.py')

# documentation ################################################################

.PHONY: all doc epub
all: doc epub
doc: dist/docs/.sentinel
epub: dist/docs.epub

dist/docs/.sentinel: $(DOC_DEP)
	sphinx-build -E -b dirhtml docs $(@D)
	touch $@
dist/docs.epub: $(DOC_DEP)
	sphinx-build -E -b epub docs $@

.PHONY: serve
serve: doc
	sphinx-autobuild \
		-E -b dirhtml \
		--port $(PORT) \
		--open-browser \
		--delay 0 \
		docs dist/docs

################################################################################

.PHONY: clean
clean:
	rm -rf dist

print-%:
	$(info $* = $($*))
