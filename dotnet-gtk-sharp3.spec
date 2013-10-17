%include	/usr/lib/rpm/macros.mono
Summary:	.NET language bindings for GTK+ 3
Summary(pl.UTF-8):	Wiązania GTK+ 3 dla .NET
Name:		dotnet-gtk-sharp3
Version:	2.99.1
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk-sharp/2.99/gtk-sharp-%{version}.tar.xz
# Source0-md5:	514fc5deb0e4b092206c0c69db6928a9
URL:		http://www.mono-project.com/GtkSharp
BuildRequires:	atk-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	glib2-devel >= 1:2.31
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 2.8
BuildRequires:	monodoc >= 2.8
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	cairo >= 1.10.0
Requires:	glib2 >= 1:2.31
Requires:	gtk+3 >= 3.0.0
Requires:	mono >= 2.8
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GTK+ 3 libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek z GTK+ 3.

%package devel
Summary:	Development part of Gtk# 3
Summary(pl.UTF-8):	Część dla programistów Gtk# 3
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	monodoc >= 2.8

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using Gtk# 3.

%description devel -l pl.UTF-8
Narzędzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystających z Gtk# 3.

%package static
Summary:	Static Gtk# 3 libraries
Summary(pl.UTF-8):	Biblioteki statyczne Gtk# 3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Gtk# 3 libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Gtk# 3.

%prep
%setup -q -n gtk-sharp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libatksharpglue-3.so
%attr(755,root,root) %{_libdir}/libgiosharpglue-3.so
%attr(755,root,root) %{_libdir}/libgtksharpglue-3.so
%attr(755,root,root) %{_libdir}/libpangosharpglue-3.so
%attr(755,root,root) %{_libdir}/libmono-profiler-gui-thread-check.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmono-profiler-gui-thread-check.so.0
# needed for DllImport on basename
%{_libdir}/libatksharpglue-3.la
%{_libdir}/libgiosharpglue-3.la
%{_libdir}/libgtksharpglue-3.la
%{_libdir}/libpangosharpglue-3.la
%{_prefix}/lib/mono/gac/atk-sharp
%{_prefix}/lib/mono/gac/cairo-sharp
%{_prefix}/lib/mono/gac/gdk-sharp
%{_prefix}/lib/mono/gac/gio-sharp
%{_prefix}/lib/mono/gac/glib-sharp
%{_prefix}/lib/mono/gac/gtk-dotnet
%{_prefix}/lib/mono/gac/gtk-sharp
%{_prefix}/lib/mono/gac/pango-sharp

%files devel
%defattr(644,root,root,755)
%doc README.generator
%attr(755,root,root) %{_bindir}/gapi3-codegen
%attr(755,root,root) %{_bindir}/gapi3-fixup
%attr(755,root,root) %{_bindir}/gapi3-parser
%attr(755,root,root) %{_libdir}/libmono-profiler-gui-thread-check.so
%{_libdir}/libmono-profiler-gui-thread-check.la
%dir %{_prefix}/lib/gapi-3.0
%attr(755,root,root) %{_prefix}/lib/gapi-3.0/gapi-fixup.exe
%attr(755,root,root) %{_prefix}/lib/gapi-3.0/gapi-parser.exe
%attr(755,root,root) %{_prefix}/lib/gapi-3.0/gapi_codegen.exe
%attr(755,root,root) %{_prefix}/lib/gapi-3.0/gapi2xml.pl
%attr(755,root,root) %{_prefix}/lib/gapi-3.0/gapi_pp.pl
%dir %{_prefix}/lib/mono/gtk-sharp-3.0
%{_prefix}/lib/mono/gtk-sharp-3.0/atk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/cairo-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/gdk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/gio-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/glib-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/gtk-dotnet.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/gtk-sharp.dll
%{_prefix}/lib/mono/gtk-sharp-3.0/pango-sharp.dll
%{_prefix}/lib/monodoc/sources/gtk-sharp-3-docs.*
%dir %{_datadir}/gapi-3.0
%{_datadir}/gapi-3.0/gapi.xsd
%{_datadir}/gapi-3.0/atk-api.xml
%{_datadir}/gapi-3.0/gdk-api.xml
%{_datadir}/gapi-3.0/gio-api.xml
%{_datadir}/gapi-3.0/glib-api.xml
%{_datadir}/gapi-3.0/gtk-api.xml
%{_datadir}/gapi-3.0/pango-api.xml
%{_pkgconfigdir}/gapi-3.0.pc
%{_pkgconfigdir}/gio-sharp-3.0.pc
%{_pkgconfigdir}/glib-sharp-3.0.pc
%{_pkgconfigdir}/gtk-dotnet-3.0.pc
%{_pkgconfigdir}/gtk-sharp-3.0.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libatksharpglue-3.a
%{_libdir}/libgiosharpglue-3.a
%{_libdir}/libgtksharpglue-3.a
%{_libdir}/libpangosharpglue-3.a
%{_libdir}/libmono-profiler-gui-thread-check.a
