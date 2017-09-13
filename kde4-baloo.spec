# $Revision:$, $Date:$
%define         _state          stable
%define         orgname		baloo
%define         qtver           4.8.3

Summary:	A framework for searching and managing metadata
Name:		kde4-baloo
Version:	4.14.3
Release:	7
License:	LGPLv2 or LGPLv3
Group:		X11/Applications
URL:		http://www.kde.org/
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	09575539cf2c76c951a67da00bd5df5b
Patch0:		moc.patch
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	akonadi-devel >= 1.12.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	kde4-kfilemetadata-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	qjson-devel
BuildRequires:	xapian-core-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A framework for searching and managing metadata.

%package libs
Summary:	Libraries for %{name}
Group:		X11/Libraries

%description libs
Baloo libraries.

%package devel
Summary:	Developer files for %{name}
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	kde4-kfilemetadata-devel >= %{version}

%description devel
Baloo development files and libraries.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake \
		-DHTML_INSTALL_DIR=%{_kdedocdir} \
		-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
		-DKDE4_ENABLE_FINAL=OFF \
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_baloo_indexer
%attr(755,root,root) %{_bindir}/baloo_file
%attr(755,root,root) %{_bindir}/baloo_file_cleaner
%attr(755,root,root) %{_bindir}/baloo_file_extractor
%attr(755,root,root) %{_bindir}/balooctl
%attr(755,root,root) %{_bindir}/baloosearch
%attr(755,root,root) %{_bindir}/balooshow
%attr(755,root,root) %{_libdir}/kde4/akonadi/akonadi_baloo_searchplugin.so
%attr(755,root,root) %{_libdir}/kde4/baloo_*.so
%attr(755,root,root) %{_libdir}/kde4/kcm_baloofile.so
%attr(755,root,root) %{_libdir}/kde4/kio_baloosearch.so
%attr(755,root,root) %{_libdir}/kde4/kio_tags.so
%attr(755,root,root) %{_libdir}/kde4/kio_timeline.so
%attr(755,root,root) %{_libdir}/kde4/krunner_baloosearchrunner.so
%attr(755,root,root) %{_libdir}/kde4/libexec/kde_baloo_filewatch_raiselimit
%{_libdir}/kde4/akonadi/akonadibaloosearchplugin.desktop
%{_datadir}/akonadi/agents/akonadibalooindexingagent.desktop
%{_datadir}/autostart/baloo_file.desktop
%{_datadir}/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%{_datadir}/dbus-1/system-services/org.kde.baloo.filewatch.service
%{_iconsdir}/hicolor/128x128/apps/baloo.png
%{_datadir}/kde4/services/baloo_*.desktop
%{_datadir}/kde4/services/kcm_baloofile.desktop
%{_datadir}/kde4/services/plasma-runner-baloosearch.desktop
%{_datadir}/kde4/services/tags.protocol
%{_datadir}/kde4/services/timeline.protocol
%{_datadir}/kde4/servicetypes/baloosearchstore.desktop
%{_datadir}/kde4/services/baloosearch.protocol
%{_datadir}/polkit-1/actions/org.kde.baloo.filewatch.policy
/etc/dbus-1/system.d/org.kde.baloo.filewatch.conf

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbaloocore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbaloocore.so.?
%attr(755,root,root) %{_libdir}/libbaloofiles.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbaloofiles.so.?
%attr(755,root,root) %{_libdir}/libbaloopim.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbaloopim.so.?
%attr(755,root,root) %{_libdir}/libbalooqueryparser.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbalooqueryparser.so.?
%attr(755,root,root) %{_libdir}/libbalooxapian.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbalooxapian.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/baloo
%attr(755,root,root) %{_libdir}/libbaloocore.so
%attr(755,root,root) %{_libdir}/libbaloofiles.so
%attr(755,root,root) %{_libdir}/libbaloopim.so
%attr(755,root,root) %{_libdir}/libbalooqueryparser.so
%attr(755,root,root) %{_libdir}/libbalooxapian.so
%{_libdir}/cmake/Baloo
