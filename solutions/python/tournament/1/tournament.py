def tally(rows):
    teams = {}
    for row in rows:
        home, away, result = row.split(";")
        for name in (home, away):
            teams.setdefault(name, {"mp": 0, "w": 0, "d": 0, "l": 0, "p": 0})["mp"] += 1
        if result == "win":
            teams[home]["w"] += 1
            teams[home]["p"] += 3
            teams[away]["l"] += 1
        elif result == "draw":
            teams[home]["d"] += 1
            teams[home]["p"] += 1
            teams[away]["d"] += 1
            teams[away]["p"] += 1
        else:
            teams[home]["l"] += 1
            teams[away]["w"] += 1
            teams[away]["p"] += 3

    standings = sorted(teams.items(), key=lambda item: (-item[1]["p"], item[0]))
    table = [f"{'Team':<31}| MP |  W |  D |  L |  P"]
    for team, stats in standings:
        table.append(
            f"{team:<31}| {stats['mp']:>2} | {stats['w']:>2} "
            f"| {stats['d']:>2} | {stats['l']:>2} | {stats['p']:>2}"
        )

    return table

