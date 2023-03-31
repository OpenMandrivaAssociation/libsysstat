%define major 0
%define libname %mklibname sysstat-qt5
%define oldlibname %mklibname sysstat-qt5 0
%define devname %mklibname sysstat-qt5 -d
%define qt4libname %mklibname sysstat %{major}
%define qt4devname %mklibname sysstat -d

Name: libsysstat
Version: 0.4.6
Release: 4
Source0: https://github.com/lxqt/libsysstat/releases/download/%{version}/libsysstat-%{version}.tar.xz
Summary: System status library for LXQt
URL: http://lxqt.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(lxqt-build-tools)

%description
System status library for LXQt.

%package -n %{libname}
Summary: System status library for LXQt
Group: System/Libraries
%rename %{qt4libname}
%rename %{oldlibname}

%description -n %{libname}
System status library for LXQt.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
%rename %{qt4devname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake_qt5

%build
%make_build -C build

%install
%make_install -C build
sed -i -e 's,^libdir=.*,libdir=%{_libdir},g' %{buildroot}%{_libdir}/pkgconfig/*.pc

%files -n %{libname}
%{_libdir}/*sysstat-qt5.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/sysstat-qt5
