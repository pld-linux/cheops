# $Revision: 1.3 $ $Date: 1999-09-04 09:11:43 $
Summary: 	Network resources viewer and manager
Summary(pl):	Narzêdzie do wizualizacji i zarz±dzania zasobami sieciowymi
Name:		cheops
Version:	0.60pre5
Release:	1
Copyright:	GPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Url:		http://www.marko.net/cheops
Source0:	ftp://ftp.marko.net/pub/cheops/%{name}-%{version}.tar.gz
Source1:	cheops.desktop
BuildRequires:	XFree86-devel
BuildRequires:  gtk+-devel
BuildRequires:  glib-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
Cheops aims to be a network "swiss army knife" used for seeing and accessing
network resources. It's written in GTK+ and uses combination of a variety 
of network tools (ping, traceroute, halfscan, QueSO). Provides system 
adminstrators with a simple interface to identyfying and
accessing their network hardware.

%description -l pl
Cheops ma aspiracje bycia sieciowym "no¿em szwajcarskim" u¿ywanym do 
obrazowania i dostêpu do zasobów sieciowych. Zosta³ napisany z u¿yciem GTK+
i u¿ywa ró¿nych narzêdzi sieciowych (ping, traceroute, halfscan, QueSO) 
umo¿liwiaj±c administratorom prost± identyfikacjê oraz dostêp do 
ich sprzêtu sieciowego.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=/usr 
make 

%install
rm -rf ${RPM_BUILD_ROOT}
install -d ${RPM_BUILD_ROOT}/usr/{X11R6/bin,lib/cheops,share/cheops}
install cheops ${RPM_BUILD_ROOT}/usr/X11R6/bin
install pixmaps/*.xpm cheops.conf services.conf ${RPM_BUILD_ROOT}/usr/share/cheops
install plugins/*.so ${RPM_BUILD_ROOT}/usr/lib/cheops
strip -s ${RPM_BUILD_ROOT}/usr/{X11R6/bin/*,lib/cheops/*}
install -d $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Networking
install %{SOURCE1} ${RPM_BUILD_ROOT}/usr/X11R6/share/applnk/Networking/

gzip -9nf COPYING README Changelog

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc COPYING.gz README.gz Changelog.gz
%attr(755,root,root) /usr/X11R6/bin/cheops
%dir	/usr/share/cheops/
%config	/usr/share/cheops/*.conf
/usr/share/cheops/*.xpm
%dir	/usr/lib/cheops
%attr(755,root,root) /usr/lib/cheops/*.so
/usr/X11R6/share/applnk/Networking/cheops.desktop
