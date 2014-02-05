Summary:	Circuit simulator
Name: 		qucs
Version:	0.0.17
Release: 	3%{?dist}
License:	GPL+
Group: 		Applications/Engineering
URL:		http://qucs.sourceforge.net/

Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz

Patch0:		qucs-format-security.patch

BuildRequires: desktop-file-utils
BuildRequires: qt-devel
Requires: freehdl, perl, iverilog
Requires: electronics-menu


%description
Qucs is a circuit simulator with graphical user interface.  The
software aims to support all kinds of circuit simulation types,
e.g. DC, AC, S-parameter and harmonic balance analysis.

%prep
%setup -q

%patch0 -p1

# fixing the icon path
sed -i 's|Icon=/usr/share/pixmaps|Icon=/usr/share/qucs/bitmaps|' debian/%{name}.desktop

%build
%configure --disable-dependency-tracking --enable-debug
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_datadir}/applications

desktop-file-install \
    --add-category "X-Fedora" \
    --add-category "Engineering" \
    debian/%{name}.desktop

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/qucs*
%{_bindir}/ps2sp*
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_mandir}/man1/*
# the following binaries were introduced in 0.0.17 (repoquery shows no conflicts with other pkgs)
%{_bindir}/alter
%{_bindir}/asco
%{_bindir}/asco-test
%{_bindir}/log
%{_bindir}/monte
%{_bindir}/postp
%{_bindir}/rosen

%changelog
* Wed Feb 05 2014 Jaromir Capik <jcapik@redhat.com> - 0.0.17-3
- Fixing format-security flaws (#1037299)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.17-1
- Update to 0.0.17
- Fixing Source0 URL

* Fri May 24 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.16-7
- Adding electronics-menu in the requires
- Minor spec file changes according to the latest guidelines

* Mon Apr 08 2013 Jaromir Capik <jcapik@redhat.com> - 0.0.16-6
- aarch64 support (#926417)
- fixing bogus date in the changelog

* Sat Feb 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.0.16-5
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 03 2011 Bruno Wolff III <bruno@wolff.to> - 0.0.16-1
- Update to upstream 0.0.16
- Fix FTBFS - bug 631404

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-3
- Patch no longer needed with freehdl-0.0.7

* Sun May 03 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-2
- Correct a problem in digital simulation

* Fri May 01 2009 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.15-1
- Update to 0.0.15

* Sat Apr 05 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.14-1
- Update to 0.0.14

* Sat Apr 05 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.13-3
- Modify BR from qt-devel to qt3-devel

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.13-2
- Autorebuild for GCC 4.3

* Tue Jan 01 2008 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.13-1
- Update to 0.0.13

* Sun Sep 09 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-4
- Modifiy qucs.desktop BZ 283941

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.12-3
- Rebuild for selinux ppc32 issue.

* Sun Jun 17 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-2
- Add perl and iverilog as require

* Sun Jun 17 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.12-1
- Update to 0.0.12

* Sat May 05 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.11-2
- Rebuild

* Sun Mar 18 2007 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.11-1
- Update to 0.0.11

* Fri Sep 01 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.10-1
- Update to 0.0.10

* Sat Jun 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-4
- Solve typo problem in changelog

* Sat Jun 10 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-3
- Delete %{_bindir}/qucsdigi.bat which is a windows bat file and useless under linux
- add --disable-dependency-tracking to %%configure
- add --enable-debug to %%configure to make debuginfo package usefull

* Thu Jun 01 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-2
- Delete ${RPM_OPT_FLAGS} modification using -ffriend-injection for "%%{?fedora}" > "4"

* Mon May 29 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.9-1
- Update to 0.0.9

* Mon Jan 23 2006 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.8-1
- Update to 0.0.8
- Add -ffriend-injection to $RPM_OPT_FLAGS for building against gcc-4.1
 
* Fri Nov 4 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-8
- Modify ctaegories in qucs.desktop

* Wed Oct 19 2005 Eric Tanguy <eric.tanguy@univ-nantes.fr> - 0.0.7-7
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
