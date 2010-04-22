Summary:	Qt extension library
Name:		libqxt
Version:	0.6.0
Release:	0.1
License:	CPL or LGPL v2
Group:		Libraries
URL:		http://www.libqxt.org/
Source0:	http://bitbucket.org/libqxt/libqxt/get/v%{version}.tar.bz2
# Source0-md5:	129527c1b18676720f59d22bb4d5ef18
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	avahi-devel
BuildRequires:	db-devel
BuildRequires:	openssl-devel
BuildRequires:	qt4-build
BuildRequires:	QtDesigner-devel
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# XXX: unify and move to rpm-build-macros
%define		_qt4_datadir	%{_datadir}/qt4
%define		_qt4_headerdir	%{_includedir}
%define		_qt4_libdir		%{_libdir}
%define		_qt4_plugindir	%{_libdir}/qt4/plugins

%description
LibQxt, an extension library for Qt, provides a suite of
cross-platform utility classes to add functionality not readily
available in the Qt toolkit.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	avahi-compat-libdns_sd-devel
Requires:	avahi-devel
Requires:	db-devel
Requires:	qt4-build

%description	devel
This package contains libraries and header files for developing
applications that use LibQxt.

%prep
%setup -q -n %{name}

# We don't want rpath
sed -i '/-rpath/d' src/qxtlibs.pri

%build
# Does not use GNU configure
./configure -verbose \
	-qmake-bin qmake-qt4 \
	-prefix %{_prefix} \
	-libdir %{_libdir}

%{__make} -j1
#%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# We are installing these to the proper location
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES *.txt README
# XXX ghost and stuff
%attr(755,root,root) %{_qt4_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc examples
#%doc doc/html
%{_qt4_headerdir}/*
%{_qt4_libdir}/*.so
%{_qt4_plugindir}/designer/*.so
%{_qt4_datadir}/mkspecs/features/qxt*.prf
