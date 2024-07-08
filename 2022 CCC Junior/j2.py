## Fergusonball Featured List

def main():
    players = int(input())
    playerstats = 0
    
    for x in range(players):
        stars = 0
        points = int(input())
        fouls = int(input())

        stars += 5 * points
        stars -= 3 * fouls
        
        if stars > 40:
            playerstats += 1

    if playerstats == players:
        print(str(playerstats) + "+")

    else:
        print(playerstats)


if __name__ == "__main__":
    main()
