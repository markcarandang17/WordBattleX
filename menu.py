def display_menu():
    print('============ WORD BATTLE X ============')
    print('Welcome to the Ultimate Word Challenge')

    display_menu_list = ['Start Game', 'View Leaderboard', 'Manage Word List (Admin)', 'Exit']
    count = 1
    for display in display_menu_list:
        print(f'[{count}] {display}')
        count += 1

