%global tl_name texlive-zh-cn
%global tl_revision 78073

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX Live manual (Chinese)
Group:		Publishing
URL:		https://www.ctan.org/pkg/texlive-zh-cn
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-zh-cn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-zh-cn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX Live manual (Chinese)

