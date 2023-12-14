submit:
	condor_submit mpi.ini

tail:
	tail -F mpi.log mpi.out mpi.err

clean:
	rm -f *.log *.out *.err *.txt
	find . -name '*.csv' \! -name 'header.csv' -delete
