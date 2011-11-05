# revision 22954
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-zh-cn
Version:	20111104
Release:	1
Summary:	TeX Live manual (Chinese)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-zh-cn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-zh-cn.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive texlive-zh-cn package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/README-live.ZH-CN
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/tex-live-zh-cn.sty
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/texlive-zh-cn.pdf
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/texlive-zh-cn.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
