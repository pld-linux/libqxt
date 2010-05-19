Summary:	Qt extension library
Name:		libqxt
Version:	0.6.0
Release:	0.1
License:	CPL or LGPL v2
Group:		Libraries
URL:		http://www.libqxt.org/
Source0:	http://bitbucket.org/libqxt/libqxt/get/v%{version}.tar.bz2
# Source0-md5:	129527c1b18676720f59d22bb4d5ef18
BuildRequires:	QtDesigner-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSql-devel
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	avahi-devel
BuildRequires:	db-devel
BuildRequires:	openssl-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	sed >= 4.0
BuildRequires:	which
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_qt4_datadir	%{_datadir}/qt4
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
Requires:	qt4-qmake

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

rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.0.6

# We are installing these to the proper location
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES *.txt README
%attr(755,root,root) %{_libdir}/libQxtBerkeley.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQxtBerkeley.so.0
%attr(755,root,root) %{_libdir}/libQxtCore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQxtCore.so.0
%attr(755,root,root) %{_libdir}/libQxtGui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQxtGui.so.0
%attr(755,root,root) %{_libdir}/libQxtNetwork.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQxtNetwork.so.0
%attr(755,root,root) %{_libdir}/libQxtSql.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQxtSql.so.0
%attr(755,root,root) %{_libdir}/libQxtWeb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQxtWeb.so.0
%attr(755,root,root) %{_libdir}/libQxtZeroconf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libQxtZeroconf.so.0

%files devel
%defattr(644,root,root,755)
%doc examples
#%doc doc/html
%{_includedir}/QxtBerkeley
%{_includedir}/QxtCore
%{_includedir}/QxtGui
%{_includedir}/QxtNetwork
%{_includedir}/QxtSql
%{_includedir}/QxtWeb
%{_includedir}/QxtZeroconf
%{_libdir}/libQxtBerkeley.so
%{_libdir}/libQxtCore.so
%{_libdir}/libQxtGui.so
%{_libdir}/libQxtNetwork.so
%{_libdir}/libQxtSql.so
%{_libdir}/libQxtWeb.so
%{_libdir}/libQxtZeroconf.so
%{_qt4_plugindir}/designer/*.so
%{_qt4_datadir}/mkspecs/features/qxt*.prf
