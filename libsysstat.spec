%define major 1
%define libname %mklibname sysstat-qt6
%define devname %mklibname sysstat-qt6 -d

Name: libsysstat
Version: 1.1.0
Release: 5
Source0: https://github.com/lxqt/libsysstat/releases/download/%{version}/libsysstat-%{version}.tar.xz
Summary: System status library for LXQt
URL: https://lxqt.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: ninja

%description
System status library for LXQt.

%package -n %{libname}
Summary: System status library for LXQt
Group: System/Libraries

%description -n %{libname}
System status library for LXQt.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%build
%cmake \
	-G Ninja
%ninja_build

%install
%ninja_install -C build
sed -i -e 's,^libdir=.*,libdir=%{_libdir},g' %{buildroot}%{_libdir}/pkgconfig/*.pc

%files -n %{libname}
%{_libdir}/*sysstat-qt6.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/sysstat-qt6
