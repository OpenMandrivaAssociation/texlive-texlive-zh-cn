# revision 26851
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-zh-cn
Version:	20120808
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

%description
TeXLive texlive-zh-cn package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/README-live.ZH-CN
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/tex-live-zh-cn.sty
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/texlive-zh-cn.pdf
%doc %{_texmfdir}/doc/texlive/texlive-zh-cn/texlive-zh-cn.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120808-1
+ Revision: 812909
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 756725
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719704
- texlive-texlive-zh-cn
- texlive-texlive-zh-cn
- texlive-texlive-zh-cn
- texlive-texlive-zh-cn

