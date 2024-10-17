%define oname SystemTray
Name:		rox-systray
Version:	0.2
Release: %mkrel 9
Summary:	Tray for rox-desktop
Group:		Graphical desktop/Other
License:	GPL
URL:		https://home.comcast.net/~andyhanton/software
Source0:	http://home.comcast.net/~andyhanton/software/%oname-%version.tar.bz2
Patch:		rox-systemtray-0.2-new-clib.patch
Requires:       rox
BuildRequires: libgtk+2-devel
BuildRequires: librox-c-devel >= 2.1.6
Buildroot: %_tmppath/%name-%version

%description
Display status icons in a rox panel applet. This implements the freedesktop.org
system tray protocol, so it's compatible with the system trays of GNOME2 and
KDE3.

%define _appsdir %{_libdir}/apps

%prep
%setup -q -n SystemTray
%patch -p1 -b .clib
cp -f %_libdir/ROX-CLib/Linux-*/bin/rox_run .

%build
export CFLAGS="$RPM_OPT_FLAGS"

./AppRun --compile

%install
rm -rf %buildroot
rm -rf ./src
mkdir -p $RPM_BUILD_ROOT%{_appsdir}
cp -a ./ $RPM_BUILD_ROOT%{_appsdir}/%{oname}

%files
%defattr(-,root,root)
%doc %{_appsdir}/%oname/Help
%dir %{_appsdir}/%oname/
%dir %{_appsdir}/%oname/Messages
%{_appsdir}/%oname/Linux*
%{_appsdir}/%oname/App*
%{_appsdir}/%oname/rox_run
%{_appsdir}/%oname/Messages
%{_appsdir}/%oname/.DirIcon
%lang(ru) %{_appsdir}/%oname/Messages/ru.gmo

%clean 
rm -rf %buildroot

