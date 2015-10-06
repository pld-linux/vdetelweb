Summary:	Telnet and Web interface for VDE2
Summary(pl.UTF-8):	Telnet oraz interfejs WWW dla VDE2
Name:		vdetelweb
Version:	1.2.1
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://downloads.sourceforge.net/vde/%{name}-%{version}.tar.bz2
# Source0-md5:	86d696891ae52fc60deb6804748cb382
URL:		http://wiki.v2.cs.unibo.it/wiki/index.php/Vdetelweb:_Telnet_and_Web_management_for_VDE
BuildRequires:	lwipv6-devel
BuildRequires:	mhash-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telnet and Web interface for VDE2.

%description -l pl.UTF-8
Telnet oraz interfejs WWW dla VDE2.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/vdetelweb
%dir %{_sysconfdir}/vde
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde/vdetelwebrc
%{_mandir}/man1/vdetelweb.1*
