#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmailtransport
Version  : 24.12.1
Release  : 84
URL      : https://download.kde.org/stable/release-service/24.12.1/src/kmailtransport-24.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.1/src/kmailtransport-24.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.1/src/kmailtransport-24.12.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Mail Transport Service
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0 LGPL-2.1
Requires: kmailtransport-data = %{version}-%{release}
Requires: kmailtransport-lib = %{version}-%{release}
Requires: kmailtransport-license = %{version}-%{release}
Requires: kmailtransport-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : ksmtp-dev
BuildRequires : libkgapi-dev
BuildRequires : qt6base-dev
BuildRequires : qtkeychain-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Analyzing Build Performance
For debug build time:
We need ClangBuildAnalyzer
git clone https://github.com/aras-p/ClangBuildAnalyzer
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=<path> ../
make install

%package data
Summary: data components for the kmailtransport package.
Group: Data

%description data
data components for the kmailtransport package.


%package dev
Summary: dev components for the kmailtransport package.
Group: Development
Requires: kmailtransport-lib = %{version}-%{release}
Requires: kmailtransport-data = %{version}-%{release}
Provides: kmailtransport-devel = %{version}-%{release}
Requires: kmailtransport = %{version}-%{release}

%description dev
dev components for the kmailtransport package.


%package lib
Summary: lib components for the kmailtransport package.
Group: Libraries
Requires: kmailtransport-data = %{version}-%{release}
Requires: kmailtransport-license = %{version}-%{release}

%description lib
lib components for the kmailtransport package.


%package license
Summary: license components for the kmailtransport package.
Group: Default

%description license
license components for the kmailtransport package.


%package locales
Summary: locales components for the kmailtransport package.
Group: Default

%description locales
locales components for the kmailtransport package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kmailtransport-24.12.1
cd %{_builddir}/kmailtransport-24.12.1
pushd ..
cp -a kmailtransport-24.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736557418
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1736557418
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmailtransport
cp %{_builddir}/kmailtransport-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmailtransport/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kmailtransport-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmailtransport/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kmailtransport-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmailtransport/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kmailtransport-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kmailtransport/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kmailtransport-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kmailtransport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libmailtransport6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/mailtransport.kcfg
/usr/share/qlogging-categories6/kmailtransport.categories
/usr/share/qlogging-categories6/kmailtransport.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/MailTransport/MailTransport/OutlookOAuthTokenRequester
/usr/include/KPim6/MailTransport/MailTransport/PrecommandJob
/usr/include/KPim6/MailTransport/MailTransport/ServerTest
/usr/include/KPim6/MailTransport/MailTransport/Transport
/usr/include/KPim6/MailTransport/MailTransport/TransportAbstractPlugin
/usr/include/KPim6/MailTransport/MailTransport/TransportActivitiesAbstract
/usr/include/KPim6/MailTransport/MailTransport/TransportActivitiesAbstractPlugin
/usr/include/KPim6/MailTransport/MailTransport/TransportComboBox
/usr/include/KPim6/MailTransport/MailTransport/TransportConfigWidget
/usr/include/KPim6/MailTransport/MailTransport/TransportJob
/usr/include/KPim6/MailTransport/MailTransport/TransportManagementWidgetNg
/usr/include/KPim6/MailTransport/MailTransport/TransportManager
/usr/include/KPim6/MailTransport/MailTransport/TransportModel
/usr/include/KPim6/MailTransport/MailTransport/TransportType
/usr/include/KPim6/MailTransport/mailtransport/mailtransport_export.h
/usr/include/KPim6/MailTransport/mailtransport/outlookoauthtokenrequester.h
/usr/include/KPim6/MailTransport/mailtransport/precommandjob.h
/usr/include/KPim6/MailTransport/mailtransport/private/transportconfigwidget_p.h
/usr/include/KPim6/MailTransport/mailtransport/servertest.h
/usr/include/KPim6/MailTransport/mailtransport/transport.h
/usr/include/KPim6/MailTransport/mailtransport/transportabstractplugin.h
/usr/include/KPim6/MailTransport/mailtransport/transportactivitiesabstract.h
/usr/include/KPim6/MailTransport/mailtransport/transportactivitiesabstractplugin.h
/usr/include/KPim6/MailTransport/mailtransport/transportbase.h
/usr/include/KPim6/MailTransport/mailtransport/transportcombobox.h
/usr/include/KPim6/MailTransport/mailtransport/transportconfigwidget.h
/usr/include/KPim6/MailTransport/mailtransport/transportjob.h
/usr/include/KPim6/MailTransport/mailtransport/transportmanagementwidgetng.h
/usr/include/KPim6/MailTransport/mailtransport/transportmanager.h
/usr/include/KPim6/MailTransport/mailtransport/transportmodel.h
/usr/include/KPim6/MailTransport/mailtransport/transporttype.h
/usr/include/KPim6/MailTransport/mailtransport_version.h
/usr/lib64/cmake/KPim6MailTransport/KPim6MailTransportConfig.cmake
/usr/lib64/cmake/KPim6MailTransport/KPim6MailTransportConfigVersion.cmake
/usr/lib64/cmake/KPim6MailTransport/KPim6MailTransportTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6MailTransport/KPim6MailTransportTargets.cmake
/usr/lib64/libKPim6MailTransport.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6MailTransport.so.6.3.1
/V3/usr/lib64/qt6/plugins/pim6/mailtransport/mailtransport_smtpplugin.so
/usr/lib64/libKPim6MailTransport.so.6
/usr/lib64/libKPim6MailTransport.so.6.3.1
/usr/lib64/qt6/plugins/pim6/mailtransport/mailtransport_smtpplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmailtransport/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmailtransport/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kmailtransport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kmailtransport/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmailtransport/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f libmailtransport6.lang
%defattr(-,root,root,-)

