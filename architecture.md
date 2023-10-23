# Othello Game Architecture Document

```mermaid
classDiagram
class Game{
    - Player player1
    - Player player2
    - Board board
    - start()
    - end_of_game()
    - compute_scores()
}
```

```mermaid
flowchart TD

    Start((Start))
    End([End])

    Init_Players[New Players]
    Init_Board[Init Board]
    Init_Game[Init Game]

    Run_Game{Run Game}
    Players_Can_Play{Can Players Play ?}
    Select_Player[Select Player]
    Player_Place_Pawn[Player Place Pawn]

    Count_Score[Score]

    Start --> Init_Players
    Start --> Init_Board
    Init_Players & Init_Board --> Init_Game
    Init_Game --> Run_Game



    Run_Game --> Players_Can_Play
    Players_Can_Play --> |True |Select_Player
    Select_Player --> Player_Place_Pawn
    Player_Place_Pawn --> Run_Game



    Players_Can_Play --> |false| Count_Score
    
    Count_Score --> End

```


https://support.typora.io/Draw-Diagrams-With-Markdown/