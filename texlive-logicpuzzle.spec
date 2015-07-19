# revision 31024
# category Package
# catalog-ctan /graphics/pgf/contrib/logicpuzzle
# catalog-date 2013-06-07 00:26:22 +0200
# catalog-license lppl1.3
# catalog-version 2.4
Name:		texlive-logicpuzzle
Version:	2.4
Release:	9
Summary:	Typeset (grid-based) logic puzzles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/logicpuzzle
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicpuzzle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicpuzzle.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to typeset various logic puzzles.
At the moment the following puzzles are supported: - 2D-Sudoku
(aka Magiequadrat, Diagon, ...), - Battleship (aka Bimaru,
Marinespiel, Batalla Naval, ...), - Bokkusu (aka Kakurasu,
Feldersummenratsel, ...), - Bridges (akak Bruckenbau, Hashi,
...), - Chaos Sudoku, - Four Winds (aka Eminent Domain,
Lichtstrahl, ...), - Hakyuu (aka Seismic, Ripple Effect, ...),
- Hitori, - Kakuro, - Kendoku (aka Mathdoku, Calcudoku, Basic,
MiniPlu, Ken Ken, Square Wisdom, Sukendo, Caldoku, ..., -
Killer Sudoku (aka Samunapure, Sum Number Place, Sumdoku,
Gebietssummen, ...), - Laser Beam (aka Laserstrahl, ...), -
Magic Labyrinth (aka Magic Spiral, Magisches Labyrinth, ...), -
Magnets (aka Magnetplatte, Magnetfeld, ...), - Masyu (aka
Mashi, {White|Black} Pearls, ...), - Minesweeper (aka
Minensuche, ...), - Number Link, - Resuko, - Schatzsuche, -
Skyline (aka Skycrapers, Wolkenkratzer, Hochhauser, ...),
including Skyline Sudoku and Skyline Sudoku (N*N) variants, -
Slitherlink (aka Fences, Number Line, Dotty Dilemma, Sli-Lin,
Takegaki, Great Wall of China, Loop the Loop, Rundweg,
Gartenzaun, ...), - Star Battle (aka Sternenschlacht, ...), -
Stars and Arrows (aka Sternenhimmel, ...), - Sudoku, - Sun and
Moon (aka Sternenhaufen, Munraito, ...), - Tents and Trees (aka
Zeltlager, Zeltplatz, Camping, ...), and - Tunnel.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/logicpuzzle/createlpsudoku
%{_texmfdistdir}/scripts/logicpuzzle/lpsmag
%{_texmfdistdir}/scripts/logicpuzzle/simple.smc
%{_texmfdistdir}/tex/latex/logicpuzzle/battleship.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/bokkusu.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/chaossudoku.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/ddsudoku.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/hakyuu.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/hitori.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/kendoku.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/killersudoku.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/laserbeam.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/logicpuzzle.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/lpenv.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/lpsudoku.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/skyline.sty
%{_texmfdistdir}/tex/latex/logicpuzzle/slitherlink.sty
%doc %{_texmfdistdir}/doc/latex/logicpuzzle/CHANGES
%doc %{_texmfdistdir}/doc/latex/logicpuzzle/INSTALL
%doc %{_texmfdistdir}/doc/latex/logicpuzzle/README
%doc %{_texmfdistdir}/doc/latex/logicpuzzle/logicpuzzle.pdf
%doc %{_texmfdistdir}/doc/latex/logicpuzzle/logicpuzzle.tex
%doc %{_texmfdistdir}/doc/latex/logicpuzzle/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc %{buildroot}%{_texmfdistdir}
