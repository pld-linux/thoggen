Summary:	DVD backup utility
Summary(pl.UTF-8):	Narzędzie do tworzenia kopii zapasowych DVD
Name:		thoggen
Version:	0.7.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/thoggen/%{name}-%{version}.tar.gz
# Source0-md5:	e36c1ceb098f8ed51ca6c0d1e7ae8279
URL:		http://thoggen.net/
BuildRequires:	gstreamer-a52dec >= 0.10.6
BuildRequires:	gstreamer-audio-effects-base >= 0.10.14
BuildRequires:	gstreamer-dvdread >= 0.10.6
BuildRequires:	gstreamer-mpeg >= 0.10.6
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
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
