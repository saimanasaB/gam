import streamlit as st
import gambit

def display_game(game):
    st.write("Game matrix:")
    st.dataframe(game, width=300, height=300)

def run_game(player1_strategy, player2_strategy):
    game = gambit.Game.from_matrix(player1_strategy, player2_strategy)
    display_game(game)
    solver = gambit.nash.ExternalEnumMixedSolver()
    solution = solver.solve(game)
    st.write("Nash Equilibrium Strategy:")
    for player, strategy in enumerate(solution):
        st.write(f"Player {player+1}: {strategy}")

def main():
    st.title("Peace War Game")
    st.write("Welcome to the Peace War Game!")

    player1_strategy = st.text_area("Player 1 Strategy Matrix", value="3, 0\n5, 1")
    player2_strategy = st.text_area("Player 2 Strategy Matrix", value="3, 5\n0, 1")

    if st.button("Run Game"):
        player1_strategy = [[int(num) for num in row.split(',')] for row in player1_strategy.split('\n')]
        player2_strategy = [[int(num) for num in row.split(',')] for row in player2_strategy.split('\n')]
        run_game(player1_strategy, player2_strategy)

if __name__ == "__main__":
    main()
