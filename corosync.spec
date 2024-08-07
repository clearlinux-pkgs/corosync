#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
# Source0 file verified with key 0xDFD015CA555CB020 (discuss@corosync.org)
#
Name     : corosync
Version  : 3.1.8
Release  : 9
URL      : https://github.com/corosync/corosync/releases/download/v3.1.8/corosync-3.1.8.tar.gz
Source0  : https://github.com/corosync/corosync/releases/download/v3.1.8/corosync-3.1.8.tar.gz
Source1  : https://github.com/corosync/corosync/releases/download/v3.1.8/corosync-3.1.8.tar.gz.asc
Source2  : DFD015CA555CB020.pkey
Summary  : corosync
Group    : Development/Tools
License  : BSD-3-Clause
Requires: corosync-bin = %{version}-%{release}
Requires: corosync-lib = %{version}-%{release}
Requires: corosync-license = %{version}-%{release}
Requires: corosync-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : doxygen
BuildRequires : gnupg
BuildRequires : graphviz
BuildRequires : groff
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(libknet)
BuildRequires : pkgconfig(libnozzle)
BuildRequires : pkgconfig(libqb)
BuildRequires : pkgconfig(libstatgrab)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SYNCHRONIZATION ALGORITHM:
-------------------------
The synchronization algorithm is used for every service in corosync to
synchronize state of the system.

%package bin
Summary: bin components for the corosync package.
Group: Binaries
Requires: corosync-license = %{version}-%{release}

%description bin
bin components for the corosync package.


%package dev
Summary: dev components for the corosync package.
Group: Development
Requires: corosync-lib = %{version}-%{release}
Requires: corosync-bin = %{version}-%{release}
Provides: corosync-devel = %{version}-%{release}
Requires: corosync = %{version}-%{release}

%description dev
dev components for the corosync package.


%package doc
Summary: doc components for the corosync package.
Group: Documentation
Requires: corosync-man = %{version}-%{release}

%description doc
doc components for the corosync package.


%package lib
Summary: lib components for the corosync package.
Group: Libraries
Requires: corosync-license = %{version}-%{release}

%description lib
lib components for the corosync package.


%package license
Summary: license components for the corosync package.
Group: Default

%description license
license components for the corosync package.


%package man
Summary: man components for the corosync package.
Group: Default

%description man
man components for the corosync package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) DFD015CA555CB020' gpg.status
%setup -q -n corosync-3.1.8
cd %{_builddir}/corosync-3.1.8
pushd ..
cp -a corosync-3.1.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719956403
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
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

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
export SOURCE_DATE_EPOCH=1719956403
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/corosync
cp %{_builddir}/corosync-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/corosync/87bb10215fd2b4c06b1ba1072ffea5ae7eae1800 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/corosync
/V3/usr/bin/corosync-cfgtool
/V3/usr/bin/corosync-cmapctl
/V3/usr/bin/corosync-cpgtool
/V3/usr/bin/corosync-keygen
/V3/usr/bin/corosync-notifyd
/V3/usr/bin/corosync-quorumtool
/usr/bin/corosync
/usr/bin/corosync-blackbox
/usr/bin/corosync-cfgtool
/usr/bin/corosync-cmapctl
/usr/bin/corosync-cpgtool
/usr/bin/corosync-keygen
/usr/bin/corosync-notifyd
/usr/bin/corosync-quorumtool

%files dev
%defattr(-,root,root,-)
/usr/include/corosync/cfg.h
/usr/include/corosync/cmap.h
/usr/include/corosync/corodefs.h
/usr/include/corosync/corotypes.h
/usr/include/corosync/cpg.h
/usr/include/corosync/hdb.h
/usr/include/corosync/quorum.h
/usr/include/corosync/sam.h
/usr/include/corosync/votequorum.h
/usr/lib64/libcfg.so
/usr/lib64/libcmap.so
/usr/lib64/libcorosync_common.so
/usr/lib64/libcpg.so
/usr/lib64/libquorum.so
/usr/lib64/libsam.so
/usr/lib64/libvotequorum.so
/usr/lib64/pkgconfig/corosync.pc
/usr/lib64/pkgconfig/libcfg.pc
/usr/lib64/pkgconfig/libcmap.pc
/usr/lib64/pkgconfig/libcorosync_common.pc
/usr/lib64/pkgconfig/libcpg.pc
/usr/lib64/pkgconfig/libquorum.pc
/usr/lib64/pkgconfig/libsam.pc
/usr/lib64/pkgconfig/libvotequorum.pc
/usr/share/man/man3/cmap_context_get.3
/usr/share/man/man3/cmap_context_set.3
/usr/share/man/man3/cmap_dec.3
/usr/share/man/man3/cmap_delete.3
/usr/share/man/man3/cmap_dispatch.3
/usr/share/man/man3/cmap_fd_get.3
/usr/share/man/man3/cmap_finalize.3
/usr/share/man/man3/cmap_get.3
/usr/share/man/man3/cmap_inc.3
/usr/share/man/man3/cmap_initialize.3
/usr/share/man/man3/cmap_initialize_map.3
/usr/share/man/man3/cmap_iter_finalize.3
/usr/share/man/man3/cmap_iter_init.3
/usr/share/man/man3/cmap_iter_next.3
/usr/share/man/man3/cmap_overview.3
/usr/share/man/man3/cmap_set.3
/usr/share/man/man3/cmap_track_add.3
/usr/share/man/man3/cmap_track_delete.3
/usr/share/man/man3/cpg_context_get.3
/usr/share/man/man3/cpg_context_set.3
/usr/share/man/man3/cpg_dispatch.3
/usr/share/man/man3/cpg_fd_get.3
/usr/share/man/man3/cpg_finalize.3
/usr/share/man/man3/cpg_initialize.3
/usr/share/man/man3/cpg_iteration_finalize.3
/usr/share/man/man3/cpg_iteration_initialize.3
/usr/share/man/man3/cpg_iteration_next.3
/usr/share/man/man3/cpg_join.3
/usr/share/man/man3/cpg_leave.3
/usr/share/man/man3/cpg_local_get.3
/usr/share/man/man3/cpg_mcast_joined.3
/usr/share/man/man3/cpg_membership_get.3
/usr/share/man/man3/cpg_model_initialize.3
/usr/share/man/man3/cpg_overview.3
/usr/share/man/man3/cpg_zcb_alloc.3
/usr/share/man/man3/cpg_zcb_free.3
/usr/share/man/man3/cpg_zcb_mcast_joined.3
/usr/share/man/man3/quorum_context_get.3
/usr/share/man/man3/quorum_context_set.3
/usr/share/man/man3/quorum_dispatch.3
/usr/share/man/man3/quorum_fd_get.3
/usr/share/man/man3/quorum_finalize.3
/usr/share/man/man3/quorum_getquorate.3
/usr/share/man/man3/quorum_initialize.3
/usr/share/man/man3/quorum_model_initialize.3
/usr/share/man/man3/quorum_overview.3
/usr/share/man/man3/quorum_trackstart.3
/usr/share/man/man3/quorum_trackstop.3
/usr/share/man/man3/sam_data_getsize.3
/usr/share/man/man3/sam_data_restore.3
/usr/share/man/man3/sam_data_store.3
/usr/share/man/man3/sam_finalize.3
/usr/share/man/man3/sam_hc_callback_register.3
/usr/share/man/man3/sam_hc_send.3
/usr/share/man/man3/sam_initialize.3
/usr/share/man/man3/sam_mark_failed.3
/usr/share/man/man3/sam_overview.3
/usr/share/man/man3/sam_register.3
/usr/share/man/man3/sam_start.3
/usr/share/man/man3/sam_stop.3
/usr/share/man/man3/sam_warn_signal_set.3
/usr/share/man/man3/votequorum_context_get.3
/usr/share/man/man3/votequorum_context_set.3
/usr/share/man/man3/votequorum_dispatch.3
/usr/share/man/man3/votequorum_fd_get.3
/usr/share/man/man3/votequorum_finalize.3
/usr/share/man/man3/votequorum_getinfo.3
/usr/share/man/man3/votequorum_initialize.3
/usr/share/man/man3/votequorum_overview.3
/usr/share/man/man3/votequorum_qdevice_master_wins.3
/usr/share/man/man3/votequorum_qdevice_poll.3
/usr/share/man/man3/votequorum_qdevice_register.3
/usr/share/man/man3/votequorum_qdevice_unregister.3
/usr/share/man/man3/votequorum_qdevice_update.3
/usr/share/man/man3/votequorum_setexpected.3
/usr/share/man/man3/votequorum_setvotes.3
/usr/share/man/man3/votequorum_trackstart.3
/usr/share/man/man3/votequorum_trackstop.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/corosync/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcfg.so.7.3.0
/V3/usr/lib64/libcmap.so.4.1.0
/V3/usr/lib64/libcorosync_common.so.4.0.0
/V3/usr/lib64/libcpg.so.4.1.0
/V3/usr/lib64/libquorum.so.5.1.0
/V3/usr/lib64/libsam.so.4.4.0
/V3/usr/lib64/libvotequorum.so.8.0.0
/usr/lib64/libcfg.so.7
/usr/lib64/libcfg.so.7.3.0
/usr/lib64/libcmap.so.4
/usr/lib64/libcmap.so.4.1.0
/usr/lib64/libcorosync_common.so.4
/usr/lib64/libcorosync_common.so.4.0.0
/usr/lib64/libcpg.so.4
/usr/lib64/libcpg.so.4.1.0
/usr/lib64/libquorum.so.5
/usr/lib64/libquorum.so.5.1.0
/usr/lib64/libsam.so.4
/usr/lib64/libsam.so.4.4.0
/usr/lib64/libvotequorum.so.8
/usr/lib64/libvotequorum.so.8.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/corosync/87bb10215fd2b4c06b1ba1072ffea5ae7eae1800

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man5/corosync.conf.5
/usr/share/man/man5/votequorum.5
/usr/share/man/man7/cmap_keys.7
/usr/share/man/man7/corosync_overview.7
/usr/share/man/man8/corosync-blackbox.8
/usr/share/man/man8/corosync-cfgtool.8
/usr/share/man/man8/corosync-cmapctl.8
/usr/share/man/man8/corosync-cpgtool.8
/usr/share/man/man8/corosync-keygen.8
/usr/share/man/man8/corosync-notifyd.8
/usr/share/man/man8/corosync-quorumtool.8
/usr/share/man/man8/corosync.8
