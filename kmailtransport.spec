#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmailtransport
Version  : 22.08.1
Release  : 48
URL      : https://download.kde.org/stable/release-service/22.08.1/src/kmailtransport-22.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.1/src/kmailtransport-22.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.1/src/kmailtransport-22.08.1.tar.xz.sig
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
BuildRequires : kcalendarcore-dev
BuildRequires : kcmutils-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcontacts-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kmime-dev
BuildRequires : ksmtp-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwallet-dev
BuildRequires : libkgapi-dev
BuildRequires : libsecret-dev

%description
No detailed description available

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
%setup -q -n kmailtransport-22.08.1
cd %{_builddir}/kmailtransport-22.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662781951
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1662781951
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmailtransport
cp %{_builddir}/kmailtransport-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmailtransport/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
cp %{_builddir}/kmailtransport-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kmailtransport/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/kmailtransport-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmailtransport/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kmailtransport-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmailtransport/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kmailtransport-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kmailtransport/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kmailtransport-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kmailtransport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang libmailtransport5

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/config.kcfg/mailtransport.kcfg
/usr/share/kservices5/kcm_mailtransport.desktop
/usr/share/qlogging-categories5/kmailtransport.categories
/usr/share/qlogging-categories5/kmailtransport.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/MailTransport/MailTransport/PrecommandJob
/usr/include/KF5/MailTransport/MailTransport/ServerTest
/usr/include/KF5/MailTransport/MailTransport/Transport
/usr/include/KF5/MailTransport/MailTransport/TransportAbstractPlugin
/usr/include/KF5/MailTransport/MailTransport/TransportComboBox
/usr/include/KF5/MailTransport/MailTransport/TransportConfigWidget
/usr/include/KF5/MailTransport/MailTransport/TransportJob
/usr/include/KF5/MailTransport/MailTransport/TransportManagementWidget
/usr/include/KF5/MailTransport/MailTransport/TransportManager
/usr/include/KF5/MailTransport/MailTransport/TransportType
/usr/include/KF5/MailTransport/mailtransport/mailtransport_export.h
/usr/include/KF5/MailTransport/mailtransport/precommandjob.h
/usr/include/KF5/MailTransport/mailtransport/private/transportconfigwidget_p.h
/usr/include/KF5/MailTransport/mailtransport/servertest.h
/usr/include/KF5/MailTransport/mailtransport/transport.h
/usr/include/KF5/MailTransport/mailtransport/transportabstractplugin.h
/usr/include/KF5/MailTransport/mailtransport/transportbase.h
/usr/include/KF5/MailTransport/mailtransport/transportcombobox.h
/usr/include/KF5/MailTransport/mailtransport/transportconfigwidget.h
/usr/include/KF5/MailTransport/mailtransport/transportjob.h
/usr/include/KF5/MailTransport/mailtransport/transportmanagementwidget.h
/usr/include/KF5/MailTransport/mailtransport/transportmanager.h
/usr/include/KF5/MailTransport/mailtransport/transporttype.h
/usr/include/KF5/MailTransport/mailtransport_version.h
/usr/include/KF5/MailTransportAkonadi/MailTransportAkonadi/DispatchModeAttribute
/usr/include/KF5/MailTransportAkonadi/MailTransportAkonadi/DispatcherInterface
/usr/include/KF5/MailTransportAkonadi/MailTransportAkonadi/ErrorAttribute
/usr/include/KF5/MailTransportAkonadi/MailTransportAkonadi/MessageQueueJob
/usr/include/KF5/MailTransportAkonadi/MailTransportAkonadi/SentActionAttribute
/usr/include/KF5/MailTransportAkonadi/MailTransportAkonadi/SentBehaviourAttribute
/usr/include/KF5/MailTransportAkonadi/MailTransportAkonadi/TransportAttribute
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi/dispatcherinterface.h
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi/dispatchmodeattribute.h
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi/errorattribute.h
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi/mailtransportakonadi_export.h
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi/messagequeuejob.h
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi/sentactionattribute.h
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi/sentbehaviourattribute.h
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi/transportattribute.h
/usr/include/KF5/MailTransportAkonadi/mailtransportakonadi_version.h
/usr/lib64/cmake/KF5MailTransport/KF5MailTransportConfig.cmake
/usr/lib64/cmake/KF5MailTransport/KF5MailTransportConfigVersion.cmake
/usr/lib64/cmake/KF5MailTransport/KF5MailTransportTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5MailTransport/KF5MailTransportTargets.cmake
/usr/lib64/cmake/KF5MailTransportAkonadi/KF5MailTransportAkonadiConfig.cmake
/usr/lib64/cmake/KF5MailTransportAkonadi/KF5MailTransportAkonadiConfigVersion.cmake
/usr/lib64/cmake/KF5MailTransportAkonadi/KF5MailTransportAkonadiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5MailTransportAkonadi/KF5MailTransportAkonadiTargets.cmake
/usr/lib64/libKF5MailTransport.so
/usr/lib64/libKF5MailTransportAkonadi.so
/usr/lib64/qt5/mkspecs/modules/qt_KMailTransport.pri
/usr/lib64/qt5/mkspecs/modules/qt_KMailTransportAkonadi.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5MailTransport.so.5
/usr/lib64/libKF5MailTransport.so.5.21.1
/usr/lib64/libKF5MailTransportAkonadi.so.5
/usr/lib64/libKF5MailTransportAkonadi.so.5.21.1
/usr/lib64/qt5/plugins/kcm_mailtransport.so
/usr/lib64/qt5/plugins/kf5/mailtransport/mailtransport_akonadiplugin.so
/usr/lib64/qt5/plugins/kf5/mailtransport/mailtransport_smtpplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmailtransport/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmailtransport/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kmailtransport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kmailtransport/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kmailtransport/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kmailtransport/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9

%files locales -f libmailtransport5.lang
%defattr(-,root,root,-)

