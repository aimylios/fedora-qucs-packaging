Summary:	Circuit simulator
Name: 		qucs
Version:	0.0.8
Release: 	1%{?dist}
Source0:	http://ovh.dl.sourceforge.net/sourceforge/qucs/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
#Patch0:		qucs-gcc4.1.diff
URL:		http://qucs.sourceforge.net/
License:	GPL 
Group: 		Applications/Engineering
BuildRoot:    	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: desktop-file-utils
BuildRequires: qt-devel
Requires: freehdl


%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.

%prep
%setup -q
#%patch0 -p1

%build
[ -n "$QTDIR" ] || . %{_sysconfdir}/profile.d/qt.sh
%if "%{?fedora}" > "4"
CXXFLAGS="${RPM_OPT_FLAGS} -ffriend-injection"
%endif
%configure
make %{?_smp_mflags}

# install will be a bit complicated because we are not assured
# that the builder has root privileges
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor fedora                            \
        --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --add-category X-Fedora                                 \
        %{SOURCE1}

%clean
rm -rf $RPM_BUILD_ROOT


%files 
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/qucs*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_mandir}/man1/*

%changelog
* Mon Jan 23 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.8-1
- Update to 0.0.8
- Add -ffriend-injection to $RPM_OPT_FLAGS for building against gcc-4.1
 
* Fri Nov 4 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-8
- Modify ctaegories in qucs.desktop

* Tue Oct 19 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-7
- Add qucs-0.0.7-2.diff for the x86_64 target

* Tue Oct 18 2005 Ralf Corsepius <rc040203@freenet.de> - 0.0.7-6
- Add qucs-0.0.7-config.diff to make configure script aware of RPM_OPT_FLAGS.

* Tue Oct 11 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-5
-add qucs.desktop
-modify buildroot

* Tue Aug 2 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.7.

* Thu Jun 23 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- rebuilt for Fedora Core 4

* Mon May 30 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.6.

* Thu Mar 3 2005 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.5.

* Fri Dec 10 2004 Wojciech Kazubski <wk@ire.pw.edu.pl>
- version 0.0.4 for Fedora Core 3

# end of file
