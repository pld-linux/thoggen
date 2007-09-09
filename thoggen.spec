Summary:	DVD backup utility
Summary(pl.UTF-8):	Narzędzie do tworzenia kopii zapasowych DVD
Name:		thoggen
Version:	0.6.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/thoggen/%{name}-%{version}.tar.gz
# Source0-md5:	f937f3e06f98c6cc038ea90b57e35820
URL:		http://thoggen.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thoggen is a DVD backup utility ('DVD ripper') for Linux, based on
GStreamer and GTK+.

%description -l pl.UTF-8
Thoggen to narzędzie do tworzenia kopii zapasowych DVD ("DVD ripper")
dla Linuksa, oparte na GStreamerze i GTK+.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_pixmapsdir}/*png
%{_desktopdir}/*desktop
