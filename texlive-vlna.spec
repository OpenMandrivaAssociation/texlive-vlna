Name:		texlive-vlna
Version:	66186
Release:	1
Summary:	TeXLive vlna package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vlna.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vlna.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
