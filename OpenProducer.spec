%define debug_package %{nil}

%define	name	OpenProducer
%define	aname	Producer
%define	version	1.0.1
%define	cvsdate	200601122325
%define release 6

Summary:	Cross-platform libray for Opengl rendering
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	GPL
Group:		Development/C++
Source0:	%{aname}-%{version}-%{cvsdate}.tar.bz2
Patch0:		Producer-1.0.1-gcc43.patch
URL:		http://www.andesengineering.com/BlueMarbleViewer/producer_install.html
BuildRequires:	pkgconfig(x11)
BuildRequires:	mesaglu-devel
BuildRequires:	pkgconfig(xmu)
BuildRequires:	openscenegraph-devel

%description
Open Producer (or simply Producer) is a cross-platform, C++ library
for managing OpenGL rendering contexts in a windowing system
independent manner.  Producer provides a simple, yet powerfully
scalable approach for real-time 3D applications wishing to run
within a single window to large, multidisplay systems.
Producer is highly  portable and has been tested on Linux, Windows,
Mac OSX, Solaris and IRIX.  Producer works on all Unix based OS's
(including Mac OSX) through the X11 Windowing system, and through
the native win32 on Windows. Producer is written with productivity,
performance and scalability in mind by adhering to industry standard
and employing advanced software engineering practices.  Software
developers wishing to produce 3D rendering software that can display
on a desktop, and move to a large system or clustered system of
displays by simply changing a configuration file, can depend on Open
Producer to handle all the complexity for them.
			   
%prep
%setup -q -n %{aname}
%patch0 -p0
rm -rf `find -type d -name CVS`

%build
%make CXX="%{__cxx} %optflags -fPIC"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%if "%{_lib}" == "lib64"
export ARCH_EXT=64
%endif
%make INST_LOCATION=$RPM_BUILD_ROOT%{_prefix} install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt doc
%{_libdir}/lib%{aname}.so
%{_includedir}/%{aname}



%changelog
* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 1:1.0.1-4mdv2011.0
+ Revision: 627702
- tighten br

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1:1.0.1-1mdv2008.1
+ Revision: 141036
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - import OpenProducer


* Fri Jan 13 2006 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 1.0.1-1mdk
- 1.0.1
- fix lib64 path
- %%mkrel

* Tue Jun 15 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.8.4-2mdk
- new cvs snapshot
- fix buildrequires
- compile with -fpermissive to allow build with gcc-3.4

* Mon Nov 24 2003 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 0.8.4-1mdk
- new cvs snapshot

* Sun Aug 24 2003 Michael Scherer <scherer.michael@free.fr> 0.8.2-2mdk
- Buildrequires libMesaGLU1-devel 

* Mon Jun 16 2003 Per Ã˜yvind Karlsen <peroyvind@sintrax.net> 0.8.2-1mdk
- new cvs snapshot
- use the real version, Epoch tag to handle this
- fix group

* Fri Apr 25 2003 Per Ã˜yvind Karlsen <peroyvind@sintrax.net> 20030422-2mdk
- fixed BuildRequires
- less clutter from deleting CVS stuff

* Wed Apr 23 2003 Per Ã˜yvind Karlsen <peroyvind@sintrax.net> 20030422-1mdk
- initial mdk release
