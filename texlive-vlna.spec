# revision 26689
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-vlna
Version:	20120809
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
%doc %{_texmfdir}/doc/man/man1/vlna.man1.pdf
%doc %{_texmfdir}/doc/vlna/vlna.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120809-1
+ Revision: 813173
- Update to latest release.

* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-3
+ Revision: 757448
- Rebuild to reduce used resources

* Sun Nov 13 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 730340
- Use rename macro instead of mix of provides/conflicts/obsoletes

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719891
- texlive-vlna
- texlive-vlna
- texlive-vlna
- texlive-vlna

