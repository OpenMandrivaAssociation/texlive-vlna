# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-vlna
Version:	20111104
Release:	1
Summary:	TeXLive vlna package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vlna.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vlna.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-vlna.bin
Provides:	vlna = %{version}
Obsoletes:	vlna <= 1.4
Conflicts:	vlna <= 1.4
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive vlna package.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/vlna.1*
%doc %{_texmfdir}/doc/man/man1/vlna.man1.pdf
%doc %{_texmfdir}/doc/vlna/vlna.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
