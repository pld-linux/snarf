Summary:	Non-interactive client for several network protocols (WWW, FTP)
Summary(pl):	Nieinteraktywny klient dla kilku protoko³ów (WWW, FTP)
Name:		snarf
Version:	7.0
Release:	9
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.mint.net/pub/snarf/%{name}-%{version}.tar.gz
# Source0-md5:	7470d8457bc0d347b5cd8668c9e735c4
Patch0:		%{name}-ipv6.patch
URL:		http://www.xach.com/snarf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snarf is a small non-interactive client for several network protocols,
like WWW, FTP, finger and some others...

%description -l pl
Snarf jest ma³ym, nieinteraktywnym klientem dla kilku protoko³ów
sieciowych, takich jak WWW, FTP, finger i kilka innych...

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-guess-winsize

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* ChangeLog TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
