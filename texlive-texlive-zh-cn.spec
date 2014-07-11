# revision 34118
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-zh-cn
Version:	20140621
Release:	2
Summary:	TeX Live manual (Chinese)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-zh-cn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-zh-cn.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-zh-cn package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/texlive/texlive-zh-cn/Makefile
%doc %{_texmfdistdir}/doc/texlive/texlive-zh-cn/README-live.ZH-CN
%doc %{_texmfdistdir}/doc/texlive/texlive-zh-cn/tex-live-zh-cn.sty
%doc %{_texmfdistdir}/doc/texlive/texlive-zh-cn/texlive-zh-cn.pdf
%doc %{_texmfdistdir}/doc/texlive/texlive-zh-cn/texlive-zh-cn.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
