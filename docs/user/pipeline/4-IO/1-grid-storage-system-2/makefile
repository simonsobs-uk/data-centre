submit:
	condor_submit gfal.ini

tail:
	tail -F gfal.log gfal.out gfal.err

clean:
	rm -f *.log *.out *.err

cert: ac.pem
ac.pem:
	voms-proxy-init --voms souk.ac.uk --valid 168:0
	rm -f ac.pem
	ln -s "/tmp/x509up_u$$UID" ac.pem
