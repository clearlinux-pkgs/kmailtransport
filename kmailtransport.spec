#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmailtransport
Version  : 21.08.2
Release  : 35
URL      : https://download.kde.org/stable/release-service/21.08.2/src/kmailtransport-21.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.08.2/src/kmailtransport-21.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.08.2/src/kmailtransport-21.08.2.tar.xz.sig
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
BuildRequires : qtbase-dev
BuildRequires : qtkeychain-dev

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
%setup -q -n kmailtransport-21.08.2
cd %{_builddir}/kmailtransport-21.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1634413548
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
export SOURCE_DATE_EPOCH=1634413548
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmailtransport
cp %{_builddir}/kmailtransport-21.08.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmailtransport/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kmailtransport-21.08.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kmailtransport/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/kmailtransport-21.08.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kmailtransport/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kmailtransport-21.08.2/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kmailtransport/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/kmailtransport-21.08.2/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kmailtransport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
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
/usr/include/KF5/MailTransport/PrecommandJob
/usr/include/KF5/MailTransport/ServerTest
/usr/include/KF5/MailTransport/Transport
/usr/include/KF5/MailTransport/TransportAbstractPlugin
/usr/include/KF5/MailTransport/TransportComboBox
/usr/include/KF5/MailTransport/TransportConfigWidget
/usr/include/KF5/MailTransport/TransportJob
/usr/include/KF5/MailTransport/TransportManagementWidget
/usr/include/KF5/MailTransport/TransportManager
/usr/include/KF5/MailTransport/TransportType
/usr/include/KF5/MailTransportAkonadi/DispatchModeAttribute
/usr/include/KF5/MailTransportAkonadi/DispatcherInterface
/usr/include/KF5/MailTransportAkonadi/ErrorAttribute
/usr/include/KF5/MailTransportAkonadi/MessageQueueJob
/usr/include/KF5/MailTransportAkonadi/SentActionAttribute
/usr/include/KF5/MailTransportAkonadi/SentBehaviourAttribute
/usr/include/KF5/MailTransportAkonadi/TransportAttribute
/usr/include/KF5/mailtransport/mailtransport_export.h
/usr/include/KF5/mailtransport/precommandjob.h
/usr/include/KF5/mailtransport/private/transportconfigwidget_p.h
/usr/include/KF5/mailtransport/servertest.h
/usr/include/KF5/mailtransport/transport.h
/usr/include/KF5/mailtransport/transportabstractplugin.h
/usr/include/KF5/mailtransport/transportbase.h
/usr/include/KF5/mailtransport/transportcombobox.h
/usr/include/KF5/mailtransport/transportconfigwidget.h
/usr/include/KF5/mailtransport/transportjob.h
/usr/include/KF5/mailtransport/transportmanagementwidget.h
/usr/include/KF5/mailtransport/transportmanager.h
/usr/include/KF5/mailtransport/transporttype.h
/usr/include/KF5/mailtransport_version.h
/usr/include/KF5/mailtransportakonadi/dispatcherinterface.h
/usr/include/KF5/mailtransportakonadi/dispatchmodeattribute.h
/usr/include/KF5/mailtransportakonadi/errorattribute.h
/usr/include/KF5/mailtransportakonadi/mailtransportakonadi_export.h
/usr/include/KF5/mailtransportakonadi/messagequeuejob.h
/usr/include/KF5/mailtransportakonadi/sentactionattribute.h
/usr/include/KF5/mailtransportakonadi/sentbehaviourattribute.h
/usr/include/KF5/mailtransportakonadi/transportattribute.h
/usr/include/KF5/mailtransportakonadi_version.h
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
/usr/lib64/libKF5MailTransport.so.5.18.2
/usr/lib64/libKF5MailTransportAkonadi.so.5
/usr/lib64/libKF5MailTransportAkonadi.so.5.18.2
/usr/lib64/qt5/plugins/kcm_mailtransport.so
/usr/lib64/qt5/plugins/mailtransport/mailtransport_akonadiplugin.so
/usr/lib64/qt5/plugins/mailtransport/mailtransport_smtpplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmailtransport/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kmailtransport/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kmailtransport/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kmailtransport/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kmailtransport/8287b608d3fa40ef401339fd907ca1260c964123

%files locales -f libmailtransport5.lang
%defattr(-,root,root,-)

