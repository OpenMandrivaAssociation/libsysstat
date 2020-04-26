%define major 0
%define beta %{nil}
%define scmrev %{nil}
%define libname %mklibname sysstat-qt5 %{major}
%define devname %mklibname sysstat-qt5 -d
%define qt4libname %mklibname sysstat %{major}
%define qt4devname %mklibname sysstat -d

Name: libsysstat
Version: 0.4.3
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 1
Source0: https://github.com/lxde/%{name}/archive/%{version}.tar.gz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.1%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
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
%if "%{scmrev}" == ""
%setup -q
%else
%setup -q -n %{name}-%{scmrev}
%endif

%autopatch -p1
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
