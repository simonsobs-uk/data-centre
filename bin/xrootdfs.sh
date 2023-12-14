#!/usr/bin/env bash

# modified from https://github.com/xrootd/xrootd/blob/master/src/XrdFfs/xrootdfs.template
 
# chkconfig: 345 99 10
# chkconfig(sun): S3 99 K0 10 
# description: start and stop XrootdFS

MOUNT_POINT1="$HOME/souk.ac.uk"

start() {
    mkdir -p "$MOUNT_POINT1"
    # export XrdSecPROTOCOL=gsi
    # export X509_USER_PROXY="/tmp/x509up_u$$UID"
    # export XrdSecGSICREATEPROXY=0

    # we need to load the fuse kernel module
    /sbin/modprobe fuse
    ulimit -c unlimited
    cd /tmp

    # Please repeat the following lines for each additional mount point.

    # XROOTDFS_RDRURL is a ROOT URL to tell XrootdFS which base path should be mounted.
    XROOTDFS_RDRURL='root://bohr3226.tier2.hep.manchester.ac.uk:1094//dpm/tier2.hep.manchester.ac.uk/home/souk.ac.uk/'

    # After XrootdFS starts but before it takes any user request, XrootdFS will try to switch its effective 
    # user ID to XROOTDFS_USER if it is defined.
    # export XROOTDFS_USER='daemon'
    # export XROOTDFS_USER="$USER"

    # if you are ready to use 'sss' security module. See README for detail
    # export XROOTDFS_SECMOD='sss'

    # XROOTDFS_CNSURL
    # XROOTDFS_FASTLS
    # XROOTDFS_OFSFWD
    # XROOTDFS_NO_ALLOW_OTHER

    # xrootdfs "$MOUNT_POINT1" -o allow_other,fsname=xrootdfs,max_write=131072,attr_timeout=10,entry_timeout=10
    xrootdfs "$MOUNT_POINT1" -o rdr="$XROOTDFS_RDRURL" 
    # undefine them so that the next mount point won't be affected by the setting for the previous mount point.
    # unset XROOTDFS_RDRURL
    # unset XROOTDFS_USER
    # unset XROOTDFS_SECMOD
}
stop() {
    # repeat the following lines for each additional mount point
    # umount $MOUNT_POINT1
    fusermount -u "$MOUNT_POINT1"
}

case "$1" in
start)
    start
    ;;

stop)
    stop
    ;;

restart)
    stop
    sleep 5
    start
    ;;

*)
    echo "Usage: $0 {start|stop|restart}"
    exit 1
esac
