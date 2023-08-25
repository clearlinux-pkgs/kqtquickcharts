#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kqtquickcharts
Version  : 23.08.0
Release  : 55
URL      : https://download.kde.org/stable/release-service/23.08.0/src/kqtquickcharts-23.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.0/src/kqtquickcharts-23.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.0/src/kqtquickcharts-23.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: kqtquickcharts-lib = %{version}-%{release}
Requires: kqtquickcharts-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
kqtquickcharts
==============
Beautiful and interactive charts for Qt Quick
## Installation

%package dev
Summary: dev components for the kqtquickcharts package.
Group: Development
Requires: kqtquickcharts-lib = %{version}-%{release}
Provides: kqtquickcharts-devel = %{version}-%{release}
Requires: kqtquickcharts = %{version}-%{release}

%description dev
dev components for the kqtquickcharts package.


%package lib
Summary: lib components for the kqtquickcharts package.
Group: Libraries
Requires: kqtquickcharts-license = %{version}-%{release}

%description lib
lib components for the kqtquickcharts package.


%package license
Summary: license components for the kqtquickcharts package.
Group: Default

%description license
license components for the kqtquickcharts package.


%prep
%setup -q -n kqtquickcharts-23.08.0
cd %{_builddir}/kqtquickcharts-23.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693001862
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1693001862
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kqtquickcharts
cp %{_builddir}/kqtquickcharts-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kqtquickcharts/f425e50e051b87590a5c1ac4d6f52506ff12d134 || :
cp %{_builddir}/kqtquickcharts-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kqtquickcharts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/kqtquickcharts_version.h
/usr/lib64/cmake/KQtQuickCharts/KQtQuickChartsConfig.cmake
/usr/lib64/cmake/KQtQuickCharts/KQtQuickChartsVersion.cmake

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/qml/org/kde/charts/libkqtquickcharts.so
/usr/lib64/qt5/qml/org/kde/charts/BarChart.qml
/usr/lib64/qt5/qml/org/kde/charts/Label.qml
/usr/lib64/qt5/qml/org/kde/charts/LegendItem.qml
/usr/lib64/qt5/qml/org/kde/charts/LineChart.qml
/usr/lib64/qt5/qml/org/kde/charts/LineLabel.qml
/usr/lib64/qt5/qml/org/kde/charts/XYChart.qml
/usr/lib64/qt5/qml/org/kde/charts/libkqtquickcharts.so
/usr/lib64/qt5/qml/org/kde/charts/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kqtquickcharts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kqtquickcharts/f425e50e051b87590a5c1ac4d6f52506ff12d134
