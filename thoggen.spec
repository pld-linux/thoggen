#
Summary:	DVD backup utility
Name:		thoggen
Version:	0.4.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/thoggen/%{name}-%{version}.tar.gz
# Source0-md5:	2bc18e2a2b592d584e7e3fffca74167c
URL:		http://thoggen.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thoggen is a DVD backup utility ('DVD ripper') for Linux, based on
GStreamer and Gtk+.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
