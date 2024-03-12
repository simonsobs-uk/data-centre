VANILLA_YML = $(shell find vanilla -name '*.yml')
PARALLEL_YML = $(shell find parallel -name '*.yml')

.PHONY: default
default: hostnames.txt
hostnames.txt:
	./gen_arch_info_classad.py arch_info.template -p hostnames.txt

.PHONY: check diff submit clean
check:
	./check_arch_info_done.py | sort
diff:
	while IFS= read -r line; do \
		file1=vanilla/arch_info_$$line.yml; \
		file2=parallel/arch_info_$$line.yml; \
		if [ -f $$file1 ] && [ -f $$file2 ]; then \
			difft $$file1 $$file2; \
		fi; \
	done < "hostnames.txt"

submit:
	for universe in vanilla parallel; do \
		cd $$universe; \
		find . -maxdepth 1 -name '*.ini' -exec condor_submit {} \; ; \
		cd ..; \
	done
clean:
	rm -rf vanilla parallel hostnames.txt parallel.csv system-simplified.csv system-simplified.html system-simplified.md system.csv vanilla.csv
	find . \( \
		-name '*.log' -o \
		-name '*.out' -o \
		-name '*.err' -o \
		-name '*.yml' -o \
		-name '*.ini' \
	\) -delete

.PHONY: analysis
analysis: vanilla.csv parallel.csv system.csv system-simplified.csv system-simplified.html system-simplified.md
vanilla.csv: $(VANILLA_YML)
	find vanilla -name '*.yml' -exec ../../src/souk/system/arch_info.py collect-arch-info -o $@ {} +
parallel.csv: $(PARALLEL_YML)
	find parallel -name '*.yml' -exec ../../src/souk/system/arch_info.py collect-arch-info -o $@ {} +
system.csv: $(VANILLA_YML) $(PARALLEL_YML)
	./arch_info_analysis.py $@
system-simplified.csv: $(VANILLA_YML) $(PARALLEL_YML)
	./arch_info_analysis.py $@ -s
system-simplified.html: $(VANILLA_YML) $(PARALLEL_YML)
	./arch_info_analysis.py $@ -s
system-simplified.md: system-simplified.html
	pandoc -t gfm -o $@ $<
