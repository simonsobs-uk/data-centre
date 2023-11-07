#!/bin/bash -l

# helpers ##############################################################

COLUMNS=72

print_double_line() {
	eval printf %.0s= '{1..'"${COLUMNS}"\}
	echo
}

print_line() {
	eval printf %.0s- '{1..'"${COLUMNS}"\}
	echo
}

########################################################################

export X509_USER_PROXY=ac.pem
PROJ_DIR='bohr3226.tier2.hep.manchester.ac.uk/dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk'

for PROTOCOL in davs root; do
	print_double_line
	echo "Testing gfal-ls with $PROTOCOL"
	print_line
	gfal-ls -alH --full-time "$PROTOCOL://$PROJ_DIR"

	print_double_line
	echo "Testing gfal-mkdir with $PROTOCOL"
	gfal-mkdir -p "$PROTOCOL://$PROJ_DIR/$USER/testing"
	print_line
	gfal-ls -alH --full-time "$PROTOCOL://$PROJ_DIR/$USER"

	print_double_line
	echo "Testing gfal-rm with $PROTOCOL"
	print_line
	gfal-rm -r "$PROTOCOL://$PROJ_DIR/$USER/testing"

	print_double_line
	echo "Testing gfal-copy with $PROTOCOL"
	echo "hello $PROTOCOL" > "hello-$PROTOCOL.txt"
	gfal-copy -f "hello-$PROTOCOL.txt" "$PROTOCOL://$PROJ_DIR/$USER"
done
