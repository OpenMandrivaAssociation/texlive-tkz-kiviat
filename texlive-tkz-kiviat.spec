# revision 22857
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-kiviat
# catalog-date 2011-06-07 15:47:15 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-tkz-kiviat
Version:	0.1
Release:	1
Summary:	Draw Kiviat graphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-kiviat
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-kiviat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-kiviat.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows the user to draw Kiviat Graphs directly, or
with data from an external file. The drawing is done with the
help of pgfplots.

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
%{_texmfdistdir}/tex/latex/tkz-kiviat/tkz-kiviat.sty
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/TKZdoc-kiviat-main.pdf
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/examples/latex/file.dat
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/examples/latex/kiviat1.tex
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/examples/latex/kiviat2.tex
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/examples/latex/kiviat3.tex
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/examples/latex/kiviat4.tex
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/examples/latex/kiviat5.tex
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/latex/TKZdoc-kiviat-main.tex
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/latex/file.dat
%doc %{_texmfdistdir}/doc/latex/tkz-kiviat/latex/file2.dat
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
