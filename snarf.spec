Summary:	Non-interactive client for several network protocols (WWW, FTP)
Summary(pl):	Nieinteraktywny klient dla kilku protoko��w (WWW, FTP)
Name:		snarf
Version:	7.0
Release:	5
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios
Source0:	ftp://ftp.mint.net/pub/snarf/%{name}-%{version}.tar.gz
Patch0:		%{name}-ipv6.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf
BuildRequires:	automake
%{?BOOT:BuildRequires:	uClibc-devel-BOOT}

%description
Snarf is a small non-interactive client for several network protocols,
like WWW, FTP, finger and some others...

%description -l pl
Snarf jest ma�ym, nieinteraktywnym klientem dla kilku protoko��w
sieciowych, takich jak WWW, FTP, finger i kilka innych...

%if %{?BOOT:1}%{!?BOOT:0}
%package BOOT
Summary:	snarf for bootdisk
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narz�dzia
Group(pt_BR):	Rede/Utilit�rios

%description BOOT
%endif

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake -a -c
%if %{?BOOT:1}%{!?BOOT:0}
%configure 
%{__make} \
	CFLAGS="-m386 -I%{_libdir}/bootdisk%{_includedir} -Os" \
	LDFLAGS="-nostdlib -static -s" \
	LIBS="%{_libdir}/bootdisk%{_libdir}/crt0.o %{_libdir}/bootdisk%{_libdir}/libc.a -lgcc"
mv -f %{name} %{name}-BOOT
%{__make} clean
%endif

%configure \
	--enable-guess-winsize 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin
install %{name}-BOOT $RPM_BUILD_ROOT%{_libdir}/bootdisk/sbin/%{name}
%endif

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README* ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk/sbin/%{name}
%endif
