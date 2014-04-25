%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio
%define __jar_repack %{nil}

Name: candlepin-deps
Summary: Build dependencies for Candlepin
Group: Internet/Applications
License: Various
Version: 0.2.4
Release: 1%{?dist}
URL: http://fedorahosted.org/candlepin
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: Red Hat, Inc
BuildArch: noarch

%description
Candlepin is an open source entitlement management system.

%prep
%setup -q 

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/candlepin/lib/
cp repo/*.jar $RPM_BUILD_ROOT%{_datadir}/candlepin/lib/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/candlepin/lib/

%changelog
* Fri Apr 25 2014 jesus m. rodriguez <jesusr@redhat.com> 0.2.4-1
- Addition of liquibase-core (wpoteat@redhat.com)
- remove f18 (jesusr@redhat.com)

* Fri Apr 11 2014 jesus m. rodriguez <jesusr@redhat.com> 0.2.3-1
- add hibernate validation api (jesusr@redhat.com)
- remove f17, add f20 (jesusr@redhat.com)

* Thu Feb 06 2014 jesus m. rodriguez <jesusr@redhat.com> 0.2.2-1
- upgrade to jackson 2.3.0 (jesusr@redhat.com)

* Tue Dec 10 2013 jesus m. rodriguez <jesusr@redhat.com> 0.2.1-1
- add hibernate4, version bump candlepin-deps (jesusr@redhat.com)

* Tue Nov 26 2013 jesus m. rodriguez <jesusr@redhat.com> 0.1.6-1
- Revert "bump version to 0.2.0" (jesusr@redhat.com)
- update for logback and slf4j changes. (jesusr@redhat.com)
- remove F16, add F19 builds (jesusr@redhat.com)
- bump version to 0.2.0 (jesusr@redhat.com)
- make releasers consistent with candlepin (jesusr@redhat.com)
- Update for Hibernate 4 (wpoteat@redhat.com)
- added koji configs (jesusr@redhat.com)

* Mon Feb 18 2013 jesus m. rodriguez <jesusr@redhat.com> 0.1.5-1
- add Fedora 18 to the build list (jesusr@redhat.com)
- Bump rhino from 1.7R2 to 1.7R3. (dgoodwin@redhat.com)

* Mon Aug 06 2012 jesus m. rodriguez <jesusr@redhat.com> 0.1.4-1
- allow building in katello koji (jesusr@redhat.com)

* Fri Jul 27 2012 jesus m. rodriguez <jesusr@redhat.com> 0.1.3-1
- add f17 (jesusr@redhat.com)
- removed f15, rhel,f16-i386 and internal tags as they are no longer needed.
  (jesusr@redhat.com)

* Fri Jun 01 2012 Alex Wood <awood@redhat.com> 0.1.2-1
- bump quartz version to 2.1.5 (cduryee@redhat.com)
- removed f15, rhel, and internal tags as they are no longer needed.
  (jesusr@redhat.com)

* Fri May 04 2012 jesus m. rodriguez <jesusr@redhat.com> 0.1.1-1
- upgraded to guice 3.0, resteasy 2.3.1, and others (jesusr@redhat.com)
- adding epel (jesusr@redhat.com)
- dist-git (jesusr@redhat.com)

* Mon Apr 02 2012 jesus m. rodriguez <jesusr@redhat.com> 0.0.24-1
- update jackson and remove qpid deps (jesusr@redhat.com)

* Tue Jan 17 2012 jesus m. rodriguez <jesusr@redhat.com> 0.0.23-1
- config should be releaser not builder (jesusr@redhat.com)

* Tue Jan 17 2012 jesus m. rodriguez <jesusr@redhat.com> 0.0.22-1
- update branch info (jesusr@redhat.com)
- Add tito releasers.conf. (dgoodwin@redhat.com)

* Fri Oct 28 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.21-1
- use upstream bouncycastle for candlepin 0.4.x (jesusr@redhat.com)

* Thu Oct 13 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.20-1
- use right dist-cvs branch (jesusr@redhat.com)

* Tue Oct 11 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.19-1
- upgrade to fedora based bouncycastle 1.46 (jesusr@redhat.com)

* Wed Sep 14 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.18-1
- upgrade to RESTEasy 2.2.1GA (jesusr@redhat.com)

* Fri Jul 15 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.17-1
- revert to standard bouncycastle (jesusr@redhat.com)

* Tue Jun 14 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.16-1
- renamed qpid*.jars, upgraded to postgresql 9 driver.

* Thu May 12 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.15-1
- updating cp-bouncycastle (jesusr@redhat.com)

* Wed May 11 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.14-1
- add new custom bouncycastle (jesusr@redhat.com)

* Thu Feb 24 2011 jesus m. rodriguez <jesusr@redhat.com> 0.0.13-1
- adding rhino 1.7 (jesusr@redhat.com)

* Tue Dec 14 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.12-1
- adding oauth as a dependency (jesusr@redhat.com)

* Wed Nov 10 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.11-1
- adding jldap, and new qpid (jesusr@redhat.com)

* Mon Oct 25 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.10-1
- 646000: adding c3p0 (jesusr@redhat.com)

* Mon Oct 18 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.9-1
- retagging and rebuilding

* Mon Oct 18 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.8-1
- add cvs branches (jesusr@redhat.com)

* Mon Oct 18 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.7-1
- add dist to release (jesusr@redhat.com)
- updated qpid (jesusr@redhat.com)
- used for its Equals and HashCode Builders (jesusr@redhat.com)

* Fri Oct 15 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.6-1
- use only one branch for now (jesusr@redhat.com)

* Fri Oct 15 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.5-1
- retagging for rebuild (jesusr@redhat.com)
- adding a readme (jesusr@redhat.com)

* Thu Sep 30 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.4-1
- rename spec file to match project (jesusr@redhat.com)

* Thu Sep 30 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.3-1
- turn off jar rebuilding (jesusr@redhat.com)
- use the right location for cp (jesusr@redhat.com)
- copy over the jars (jesusr@redhat.com)

* Thu Sep 30 2010 jesus m. rodriguez <jesusr@redhat.com> 0.0.2-1
- new package built with tito

