%define name nagios-plugin-check_linksys
%define version 0.1
%define release 0

Summary: monitoring plugin for Linksys network hardware for Nagios
URL: http://www.nagios.org
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Application/System
Source0: %{name}-%{version}.tar.gz
Requires: nagios-plugins, net-snmp-perl

%description

%prep
rm -rf $RPM_BUILD_DIR/nagios-plugin-check_linksys-0.1
zcat $RPM_SOURCE_DIR/nagios-plugin-check_linksys-0.1.tar.gz | tar -xvf -

%pre

%preun

%install
cp $RPM_SOURCE_DIR/nagios-plugin-check_linksys-0.1/check_linksys.pl /usr/lib/nagios/plugins/

%clean

%files
%defattr(755,root,root)
/usr/lib/nagios/plugins/check_linksys.pl

%changelog
* Mon Aug 04 2008 Birger Schmidt
- First RPM build (0.1)
