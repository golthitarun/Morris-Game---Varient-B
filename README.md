# NINE MEN MORRIS GAME - VARIENT B

## Game Rules

The Morris Game, Variant-B , is a variant of Nine Men’s Morris game. It is a board game between two
players: White and Black. Each player has 9 pieces, and the game board is as shown above. Pieces can
be placed on intersections of lines. (There are a total of 21 locations for pieces.) The goal is to capture
opponents pieces by getting three pieces on a single line (a mill). The winner is the first player to reduce
the opponent to only 2 pieces, or block the opponent from any further moves. The game has three distinct
phases: opening, midgame, and endgame.

Opening: Players take turns placing their 9 pieces - one at a time - on any vacant board intersection
spot.

Midgame: Players take turns moving one piece along a board line to any adjacent vacant spot.

Endgame: A player down to only three pieces may move a piece to any open spot, not just an adjacent
one (hopping).

Mills: At any stage if a player gets three of their pieces on the same straight board line (a mill), then one
of the opponent’s isolated pieces is removed from the board. An isolated piece is a piece that is not part of
a mill.

##Representing a board position

One way of representing a board position is by an array of length 21 , containing the pieces as the letters
W, B, x. (The letter x stands for a “non-piece”.) The array specifies the pieces starting from bottom-left
and continuing left-right bottom up.

Here are a two examples:
1. xxxBxWWWWWBBBBxxxxxxx
2. WWWWWWWWBBBBBBBBxxxxx

## Usage

```sh
    $ python filename.py InputboardPosition.txt OutputboardPosition.txt
```

## Standard Output Example
```sh
Input position: xxxxxxxxxWxxxxxxBxxxx Output position: xxxxxxxxxWxxWxxxBxxxx
Positions evaluated by static estimation: 9.
MINIMAX estimate: 9987
```
