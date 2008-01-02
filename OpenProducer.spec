%define	name	OpenProducer
%define	aname	Producer
%define	version	1.0.1
%define	cvsdate	200601122325
%define	release %mkrel 1

Summary:	Cross-platform libray for Opengl rendering
Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
License:	GPL
Group:		Development/C++
Source0:	%{aname}-%{version}-%{cvsdate}.tar.bz2
URL:		http://www.andesengineering.com/BlueMarbleViewer/producer_install.html
BuildRequires:	X11-devel MesaGLU-devel OpenThreads >= 1.4.1 
BuildRoot:	%{_tmppath}%{name}-%{version}-%{release}-buildroot

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
rm -rf `find -type d -name CVS`

%build
%make CXX="%{__cxx} $RPM_OPT_FLAGS -fPIC"

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

