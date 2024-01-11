default:
	./gen_arch_info_classad.py arch_info.template -p hostnames.txt
check:
	./check_arch_info_done.py | sort
submit:
	for universe in vanilla parallel; do \
		cd $$universe; \
		find . -maxdepth 1 -name '*.ini' -exec condor_submit {} \; ; \
		cd ..; \
	done
clean:
	find . \( \
		-name '*.log' -o \
		-name '*.out' -o \
		-name '*.err' -o \
		-name '*.yml' -o \
		-name '*.ini' \
	\) -delete
