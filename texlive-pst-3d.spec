# revision 17257
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-3d
# catalog-date 2010-02-15 10:59:10 +0100
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-pst-3d
Version:	1.10
Release:	1
Summary:	A PSTricks package for tilting and other pseudo-3D tricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-3d.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-3d.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The pst-3d package provides basic macros for shadows, tilting
and three dimensional representations of text or graphical
objects.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
