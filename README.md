# Candlepin Deps
This project contains the java dependencies for project candlepin,
used to build the candlepin rpm.

http://www.candlepinproject.org

# Refresh the Jars
```shell
$ cd ~/path/to/candlepin
$ bin/createcpdeps.sh /path/to/candlepin-deps/
$ cd /path/to/candlepin-deps

# now check to see what changed
git status
git add/rm as required
git commit
```

# Building an RPM
candlepin-deps uses tito for building the rpm. 

http://github.com/dgoodwin/tito

