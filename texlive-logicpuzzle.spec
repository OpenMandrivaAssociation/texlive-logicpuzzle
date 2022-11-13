Name:		texlive-logicpuzzle
Version:	34491
Release:	1
Summary:	Typeset (grid-based) logic puzzles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/logicpuzzle
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicpuzzle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/logicpuzzle.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/scripts/logicpuzzle
%{_texmfdistdir}/tex/latex/logicpuzzle
%doc %{_texmfdistdir}/doc/latex/logicpuzzle

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc %{buildroot}%{_texmfdistdir}
