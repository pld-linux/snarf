Summary:	Snarf
Name:		snarf
Version:	7.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
Source0:	ftp://ftp.mint.net/pub/snarf/%{name}-%{version}.tar.gz
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snarf is a non-interactive client for several network protocols.

%prep
%setup -q

%build
%configure --enable-guess-winsize 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README ChangeLog TODO

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc README.* ChangeLog.* TODO.*

%clean
rm -rf $RPM_BUILD_ROOT
