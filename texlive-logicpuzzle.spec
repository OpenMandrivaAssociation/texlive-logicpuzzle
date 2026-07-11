%global tl_name logicpuzzle
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	Typeset (grid-based) logic puzzles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/logicpuzzle
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logicpuzzle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/logicpuzzle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to typeset various logic puzzles. At the
moment the following puzzles are supported: 2D-Sudoku (aka Magiequadrat,
Diagon, ...), Battleship (aka Bimaru, Marinespiel, Batalla Naval, ...),
Bokkusu (aka Kakurasu, Feldersummenratsel, ...), Bridges (akak
Bruckenbau, Hashi, ...), Chaos Sudoku, Four Winds (aka Eminent Domain,
Lichtstrahl, ...), Hakyuu (aka Seismic, Ripple Effect, ...), Hitori,
Kakuro, Kendoku (aka Mathdoku, Calcudoku, Basic, MiniPlu, Ken Ken,
Square Wisdom, Sukendo, Caldoku, ..., Killer Sudoku (aka Samunapure, Sum
Number Place, Sumdoku, Gebietssummen, ...), Laser Beam (aka Laserstrahl,
...), Magic Labyrinth (aka Magic Spiral, Magisches Labyrinth, ...),
Magnets (aka Magnetplatte, Magnetfeld, ...), Masyu (aka Mashi,
{White|Black} Pearls, ...), Minesweeper (aka Minensuche, ...), Nonogram
(aka Griddlers, Hanjie, Tsunami, Logic Art, Logimage, ...), Number Link
(aka Alphabet Link, Arukone, Buchstabenbund, ...), Resuko, Schatzsuche,
Skyline (aka Skycrapers, Wolkenkratzer, Hochhauser, ...), including
Skyline Sudoku and Skyline Sudoku (N*N) variants, Slitherlink (aka
Fences, Number Line, Dotty Dilemma, Sli-Lin, Takegaki, Great Wall of
China, Loop the Loop, Rundweg, Gartenzaun, ...), Star Battle (aka
Sternenschlacht, ...), Stars and Arrows (aka Sternenhimmel, ...),
Sudoku, Sun and Moon (aka Sternenhaufen, Munraito, ...), Tents and Trees
(aka Zeltlager, Zeltplatz, Camping, ...), and Tunnel.

