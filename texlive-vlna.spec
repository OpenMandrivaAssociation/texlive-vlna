%global tl_name vlna
%global tl_revision 73908

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	add ~ after non-syllabic preposition, for Czech/Slovak
Group:		Publishing
URL:		https://www.ctan.org/pkg/vlna
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vlna.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vlna.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(vlna.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Preprocessor for TeX source implementing the Czech/Slovak typographical
rule forbidding a non-syllabic preposition alone at the end of a line.

