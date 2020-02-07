#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kmailtransport
Version  : 19.12.2
Release  : 20
URL      : https://download.kde.org/stable/release-service/19.12.2/src/kmailtransport-19.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.2/src/kmailtransport-19.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.2/src/kmailtransport-19.12.2.tar.xz.sig
Summary  : Mail Transport Service
Group    : Development/Tools
License  : LGPL-2.1
Requires: kmailtransport-data = %{version}-%{release}
Requires: kmailtransport-lib = %{version}-%{release}
Requires: kmailtransport-license = %{version}-%{release}
Requires: kmailtransport-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : ksmtp-dev
BuildRequires : libkgapi-dev

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
%setup -q -n kmailtransport-19.12.2
cd %{_builddir}/kmailtransport-19.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581087732
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1581087732
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmailtransport
cp %{_builddir}/kmailtransport-19.12.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/kmailtransport/9a1929f4700d2407c70b507b3b2aaf6226a9543c
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
/usr/lib64/libKF5MailTransport.so.5.13.2
/usr/lib64/libKF5MailTransportAkonadi.so.5
/usr/lib64/libKF5MailTransportAkonadi.so.5.13.2
/usr/lib64/qt5/plugins/kcm_mailtransport.so
/usr/lib64/qt5/plugins/mailtransport/mailtransport_akonadiplugin.so
/usr/lib64/qt5/plugins/mailtransport/mailtransport_smtpplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmailtransport/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f libmailtransport5.lang
%defattr(-,root,root,-)

