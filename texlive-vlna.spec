# revision 29764
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-vlna
Version:	20131009
Release:	1
Summary:	TeXLive vlna package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vlna.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vlna.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-vlna.bin
%rename vlna

%description
TeXLive vlna package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/vlna.1*
%doc %{_texmfdistdir}/doc/man/man1/vlna.man1.pdf
%doc %{_texmfdistdir}/doc/vlna/vlna.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
