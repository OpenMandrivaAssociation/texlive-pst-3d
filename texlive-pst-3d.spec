# revision 17257
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-3d
# catalog-date 2010-02-15 10:59:10 +0100
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-pst-3d
Version:	1.10
Release:	7
Summary:	A PSTricks package for tilting and other pseudo-3D tricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-3d.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-3d.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The pst-3d package provides basic macros for shadows, tilting
and three dimensional representations of text or graphical
objects.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-3d/pst-3d.pro
%{_texmfdistdir}/tex/generic/pst-3d/pst-3d.tex
%{_texmfdistdir}/tex/latex/pst-3d/pst-3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-3d/README
%doc %{_texmfdistdir}/doc/generic/pst-3d/pst-3d-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-3d/pst-3d-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-3d/pst-3d-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-3d/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Sun Feb 12 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.10-3
+ Revision: 773392
- Rebuild

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.10-2
+ Revision: 755197
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.10-1
+ Revision: 719328
- texlive-pst-3d
- texlive-pst-3d
- texlive-pst-3d
- texlive-pst-3d

