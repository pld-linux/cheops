# $Revision: 1.26 $ $Date: 2002-05-13 09:55:05 $
Summary:	Network resources viewer and manager
Summary(pl):	Narzêdzie do wizualizacji i zarz±dzania zasobami sieciowymi
Name:		cheops
Version:	0.61
Release:	4
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://ftp.marko.net/pub/cheops/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.marko.net/cheops/
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	ucd-snmp-devel >= 4.2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Cheops aims to be a network "swiss army knife" used for seeing and
accessing network resources. It's written in GTK+ and uses combination
of a variety of network tools (ping, traceroute, halfscan, QueSO).
Provides system adminstrators with a simple interface to identyfying
and accessing their network hardware.

%description -l pl
Cheops ma byæ "sieciowym scyzorykiem" u¿ywanym do obrazowania i
dostêpu do zasobów sieciowych. Zosta³ napisany przy u¿yciu GTK+;
wykorzystuje ró¿ne narzêdzia sieciowe (ping, traceroute, halfscan,
QueSO), umo¿liwiaj±c administratorom prost± identyfikacjê oraz dostêp
do ich sprzêtu sieciowego.

%prep
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/cheops,%{_datadir}/cheops} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir}}

install cheops $RPM_BUILD_ROOT%{_bindir}
install pixmaps/*.xpm cheops.conf services.conf $RPM_BUILD_ROOT%{_datadir}/cheops
install plugins/*.so $RPM_BUILD_ROOT%{_libdir}/cheops

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf README Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/cheops
%dir %{_libdir}/cheops
%attr(755,root,root) %{_libdir}/cheops/*.so
%dir %{_datadir}/cheops
%config	%{_datadir}/cheops/*.conf
%{_datadir}/cheops/*.xpm
%{_applnkdir}/Network/Misc/cheops.desktop
%{_pixmapsdir}/*
