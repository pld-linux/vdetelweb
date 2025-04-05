Summary:	Telnet and Web interface for VDE2
Summary(pl.UTF-8):	Telnet oraz interfejs WWW dla VDE2
Name:		vdetelweb
Version:	1.2.3
Release:	1
License:	GPL v2+
Group:		Applications/Networking
#Source0Download: https://github.com/virtualsquare/vdetelweb/tags
Source0:	https://github.com/virtualsquare/vdetelweb/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0c992b2fa55abd080dfe9f0b81a735c6
URL:		http://wiki.v2.cs.unibo.it/wiki/index.php%3Ftitle=Vdetelweb:_Telnet_and_Web_management_for_VDE.html
BuildRequires:	cmake >= 3.12
BuildRequires:	lwipv6-devel
BuildRequires:	mhash-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	vde2-devel >= 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telnet and Web interface for VDE2.

%description -l pl.UTF-8
Telnet oraz interfejs WWW dla VDE2.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# missing in cmake install
install -d $RPM_BUILD_ROOT%{_sysconfdir}/vde
cp -p vdetelwebrc $RPM_BUILD_ROOT%{_sysconfdir}/vde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/vdetelweb
%dir %{_sysconfdir}/vde
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vde/vdetelwebrc
%{_mandir}/man1/vdetelweb.1*
