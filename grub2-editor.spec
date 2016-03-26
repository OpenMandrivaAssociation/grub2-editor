%define snap %nil

Summary:	Grub2 editor
Name:		grub2-editor
Version:	0.7.0
Release:	2
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		https://github.com/maz-1/grub2-editor
# git clone https://github.com/maz-1/grub2-editor.git
# git archive --format=tar --prefix grub2-editor-0.5.8-$(date +%Y%m%d)/ HEAD | xz -vf > grub2-editor-0.5.8-$(date +%Y%m%d).tar.xz

Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(MagickCore)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	grub2
Obsoletes:	kcm-grub2 <= 0.6.4-8
Provides:	kcm-grub2 = 0.6.4-9

%description
A KDE Control Module for configuring the GRUB2 bootloader.
Unofficial KF5 port.

%prep
%setup -q
%cmake_kde5 -DGRUB_INSTALL_EXE="%{_sbindir}/grub2-install" \
	    -DGRUB_MKCONFIG_EXE="%{_sbindir}/grub2-mkconfig" \
            -DGRUB_PROBE_EXE="%{_sbindir}/grub2-probe" \
            -DGRUB_SET_DEFAULT_EXE="%{_sbindir}/grub2-set-default" \
            -DGRUB_MAKE_PASSWD_EXE="%{_bindir}/grub2-mkpasswd-pbkdf2" \
            -DGRUB_MENU="/boot/grub2/grub.cfg" \
            -DGRUB_ENV="/boot/grub2/grubenv" \
            -DGRUB_CONFIG="%{_sysconfdir}/default/grub" \
            -DGRUB_MEMTEST="%{_sysconfdir}/grub.d/20_memtest86+" \
            -DGRUB_CONFIGDIR="%{_sysconfdir}/grub.d" \
            -DGRUB_SECURITY="01_header_passwd"

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kcm-grub2

%files -f kcm-grub2.lang
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmgrub2.conf
%{_libdir}/libexec/kauth/kcmgrub2helper
%{_libdir}/qt5/plugins/kcm_grub2.so
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmgrub2.service
%{_datadir}/kservices5/kcm_grub2.desktop
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmgrub2.policy
