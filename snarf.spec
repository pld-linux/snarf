# _without_embed - don't build uClibc version
Summary:	Non-interactive client for several network protocols (WWW, FTP)
Summary(pl):	Nieinteraktywny klient dla kilku protoko³ów (WWW, FTP)
Name:		snarf
Version:	7.0
Release:	6
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	ftp://ftp.mint.net/pub/snarf/%{name}-%{version}.tar.gz
Patch0:		%{name}-ipv6.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf
BuildRequires:	automake
%if %{!?_without_embed:1}%{?_without_embed:0}
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static
%endif

%define embed_path	/usr/lib/embed
%define embed_cc	%{_arch}-uclibc-cc
%define embed_cflags	%{rpmcflags} -Os

%description
Snarf is a small non-interactive client for several network protocols,
like WWW, FTP, finger and some others...

%description -l pl
Snarf jest ma³ym, nieinteraktywnym klientem dla kilku protoko³ów
sieciowych, takich jak WWW, FTP, finger i kilka innych...

%package embed
Summary:	snarf for bootdisk
Summary(pl):	snarf na bootkietkê
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários

%description embed
snarf for bootdisk.

%description embed -l pl
snarf na bootkietkê.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c

%if %{!?_without_embed:1}%{?_without_embed:0}
%configure
%{__make} \
	CFLAGS="%{embed_cflags}" \
	CC=%{embed_cc}
mv -f %{name} %{name}-embed-shared
%{__make} \
	CFLAGS="%{embed_cflags}" \
	LDFLAGS="-static" \
	CC=%{embed_cc}
mv -f %{name} %{name}-embed-static
%{__make} clean
%endif

%configure \
	--enable-guess-winsize
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%if %{!?_without_embed:1}%{?_without_embed:0}
install -d $RPM_BUILD_ROOT%{embed_path}/{shared,static}
install %{name}-embed-shared $RPM_BUILD_ROOT%{embed_path}/shared/%{name}
install %{name}-embed-static $RPM_BUILD_ROOT%{embed_path}/static/%{name}
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

%if %{!?_without_embed:1}%{?_without_embed:0}
%files embed
%defattr(644,root,root,755)
%attr(755,root,root) %{embed_path}/*/%{name}
%endif
