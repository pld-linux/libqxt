# NOTE
# - no longer maintained
Summary:	Qt extension library
Summary(pl.UTF-8):	Biblioteka rozszerzeń Qt
Name:		libqxt
Version:	0.6.2
Release:	1
License:	CPL v1.0 or LGPL v2.1
Group:		Libraries
Source0:	https://bitbucket.org/libqxt/libqxt/get/v%{version}.tar.bz2?/%{name}-%{version}.tar.bz2
# Source0-md5:	a859a1757dc0aaf010df1a0783e3e001
Patch0:		%{name}-linking.patch
Patch1:		%{name}-db.patch
URL:		https://bitbucket.org/libqxt/libqxt/wiki/Home
BuildRequires:	QtCore-devel >= 4.3
BuildRequires:	QtDesigner-devel >= 4.3
BuildRequires:	QtGui-devel >= 4.3
BuildRequires:	QtNetwork-devel >= 4.3
BuildRequires:	QtScript-devel >= 4.3
BuildRequires:	QtSql-devel >= 4.3
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	avahi-devel
BuildRequires:	db-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	qt4-build >= 4.3
BuildRequires:	qt4-qmake >= 4.3
BuildRequires:	sed >= 4.0
BuildRequires:	which
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt4_datadir	%{_datadir}/qt4
%define		qt4_plugindir	%{_libdir}/qt4/plugins

%description
LibQxt, an extension library for Qt, provides a suite of
cross-platform utility classes to add functionality not readily
available in the Qt toolkit.

%description
LibQxt to biblioteka rozszeszeń Qt, udostępniająca zbiór
wieloplatformowych klas narzędziowych dodających funkcje nie
dostępne w łatwy sposób w bibliotekach Qt.

%package devel
Summary:	Development files for Qxt libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek Qxt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4.3
Requires:	QtGui-devel >= 4.3
Requires:	QtNetwork-devel >= 4.3
Requires:	QtSql-devel >= 4.3
Requires:	avahi-compat-libdns_sd-devel
Requires:	avahi-devel
Requires:	db-devel
Requires:	libstdc++-devel
Requires:	qt4-qmake >= 4.3

%description devel
This package contains the header files for developing applications
that use LibQxt.

%description devel -l pl.UTF-8
Ten pakiet  zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących libQxt.

%package -n QtDesigner-plugin-qxt
Summary:	QtDesigner plugin to support Qxt libraries
Summary(pl.UTF-8):	Wtyczka QtDesignera wspomagająca korzystanie z bibliotek Qxt
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}
Requires:	QtDesigner >= 4.3

%description -n QtDesigner-plugin-qxt
QtDesigner plugin to support Qxt libraries.

%description -n QtDesigner-plugin-qxt -l pl.UTF-8
Wtyczka QtDesignera wspomagająca korzystanie z bibliotek Qxt.

%prep
%setup -q -n libqxt-libqxt-dadc327c2a6a
%patch0 -p1
%patch1 -p1

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.so.0.6

# We are installing these to the proper location
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES *.txt LICENSE README
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
%attr(755,root,root) %{_libdir}/libQxtBerkeley.so
%attr(755,root,root) %{_libdir}/libQxtCore.so
%attr(755,root,root) %{_libdir}/libQxtGui.so
%attr(755,root,root) %{_libdir}/libQxtNetwork.so
%attr(755,root,root) %{_libdir}/libQxtSql.so
%attr(755,root,root) %{_libdir}/libQxtWeb.so
%attr(755,root,root) %{_libdir}/libQxtZeroconf.so
%{_includedir}/QxtBerkeley
%{_includedir}/QxtCore
%{_includedir}/QxtGui
%{_includedir}/QxtNetwork
%{_includedir}/QxtSql
%{_includedir}/QxtWeb
%{_includedir}/QxtZeroconf
%{qt4_datadir}/mkspecs/features/qxt*.prf

%files -n QtDesigner-plugin-qxt
%defattr(644,root,root,755)
%attr(755,root,root) %{qt4_plugindir}/designer/libQxtDesignerPlugins.so
