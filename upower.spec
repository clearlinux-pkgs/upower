#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : upower
Version  : 0.99.7
Release  : 16
URL      : https://upower.freedesktop.org/releases/upower-0.99.7.tar.xz
Source0  : https://upower.freedesktop.org/releases/upower-0.99.7.tar.xz
Summary  : UPower is a system daemon for managing power devices
Group    : Development/Tools
License  : GPL-2.0
Requires: upower-bin
Requires: upower-data
Requires: upower-lib
Requires: upower-locales
Requires: upower-config
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(udev)
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Support-an-entirely-stateless-configuration.patch

%description
===============
UPower
===============
Requirements:
glib-2.0             >= 2.34.0
gio-2.0              >= 2.16.1
gudev-1.0            >= 147    (Linux)
libusb-1.0           >= 1.0.0  (Linux)
libimobiledevice-1.0 >= 0.9.7  (optional)

%package bin
Summary: bin components for the upower package.
Group: Binaries
Requires: upower-data
Requires: upower-config

%description bin
bin components for the upower package.


%package config
Summary: config components for the upower package.
Group: Default

%description config
config components for the upower package.


%package data
Summary: data components for the upower package.
Group: Data

%description data
data components for the upower package.


%package dev
Summary: dev components for the upower package.
Group: Development
Requires: upower-lib
Requires: upower-bin
Requires: upower-data
Provides: upower-devel

%description dev
dev components for the upower package.


%package lib
Summary: lib components for the upower package.
Group: Libraries
Requires: upower-data

%description lib
lib components for the upower package.


%package locales
Summary: locales components for the upower package.
Group: Default

%description locales
locales components for the upower package.


%prep
%setup -q -n upower-0.99.7
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511882259
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static --disable-man-pages
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1511882259
rm -rf %{buildroot}
%make_install
%find_lang upower
## make_install_append content
mv %{buildroot}/etc/UPower %{buildroot}/usr/share/. && mv %{buildroot}/etc/dbus-1/system.d %{buildroot}/usr/share/dbus-1/. && rmdir %{buildroot}/etc/dbus-1 && rmdir %{buildroot}/etc
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/upower
/usr/libexec/upowerd

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/upower.service
/usr/lib/udev/rules.d/95-upower-csr.rules
/usr/lib/udev/rules.d/95-upower-hid.rules
/usr/lib/udev/rules.d/95-upower-wup.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/UPowerGlib-1.0.typelib
/usr/share/UPower/UPower.conf
/usr/share/dbus-1/interfaces/org.freedesktop.UPower.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.UPower.KbdBacklight.xml
/usr/share/dbus-1/interfaces/org.freedesktop.UPower.Wakeups.xml
/usr/share/dbus-1/interfaces/org.freedesktop.UPower.xml
/usr/share/dbus-1/system-services/org.freedesktop.UPower.service
/usr/share/dbus-1/system.d/org.freedesktop.UPower.conf
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libupower-glib/up-autocleanups.h
/usr/include/libupower-glib/up-client.h
/usr/include/libupower-glib/up-device.h
/usr/include/libupower-glib/up-history-item.h
/usr/include/libupower-glib/up-stats-item.h
/usr/include/libupower-glib/up-types.h
/usr/include/libupower-glib/up-version.h
/usr/include/libupower-glib/up-wakeup-item.h
/usr/include/libupower-glib/up-wakeups.h
/usr/include/libupower-glib/upower.h
/usr/lib64/libupower-glib.so
/usr/lib64/pkgconfig/upower-glib.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libupower-glib.so.3
/usr/lib64/libupower-glib.so.3.0.1

%files locales -f upower.lang
%defattr(-,root,root,-)

