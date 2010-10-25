%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio
%define __jar_repack %{nil}

Name: candlepin-deps
Summary: Build dependencies for Candlepin
Group: Internet/Applications
License: Various
Version: 0.0.10
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

