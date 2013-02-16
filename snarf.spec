Summary:	Non-interactive client for several network protocols (WWW, FTP)
Summary(pl.UTF-8):	Nieinteraktywny klient dla kilku protokołów (WWW, FTP)
Name:		snarf
Version:	7.0
Release:	12
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://ftp.mint.net/pub/snarf/%{name}-%{version}.tar.gz
# Source0-md5:	7470d8457bc0d347b5cd8668c9e735c4
Patch0:		ftp://ftp.debian.org:/debian/pool/main/s/snarf/snarf_7.0-5.diff.gz
# Patch0-md5:	d306ec929b852f5a7b52df4aeeb0813c
Patch1:		%{name}-ipv6.patch
Patch2:		%{name}-build.patch
URL:		http://www.xach.com/snarf/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snarf is a small non-interactive client for several network protocols,
like WWW, FTP, finger and some others...

%description -l pl.UTF-8
Snarf jest małym, nieinteraktywnym klientem dla kilku protokołów
sieciowych, takich jak WWW, FTP, finger i kilka innych...

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
