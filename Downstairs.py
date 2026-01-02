"""
🎮 STAIR CLIMBING GAME - INTERACTIVE VERSION 🎮
==============================================
A fun game where you climb up and down stairs.
Learn about classes, methods, and game logic!
"""

import time  # For making the game more fun

class StairGame:
    def __init__(self, player_name=""):
        """
        Initialize the game
        - position: where you are on the stairs (starts at 0)
        - total_stairs: how many stairs to climb (10 total)
        """
        self.position = 0  # Start at the bottom (step 0)
        self.total_stairs = 10  # Need to reach step 10 to win
        self.player_name = player_name
        
    def show_stairs(self):
        """Show a visual of where you are on the stairs"""
        print("\n" + "=" * 40)
        print("CURRENT POSITION:")
        
        # Draw the stairs
        for step in range(self.total_stairs, -1, -1):
            if step == self.position:
                print(f"Step {step:2} [YOU ARE HERE] 👣")
            else:
                print(f"Step {step:2} [{'█' if step <= self.position else '░'}]")
        
        print(f"\nYou are at step {self.position} of {self.total_stairs}")
        print("=" * 40)
    
    def climb_up(self):
        """Climb one step up"""
        if self.position < self.total_stairs:
            self.position += 1
            print(f"\n⬆️  You climbed UP to step {self.position}")
            time.sleep(0.5)  # Small pause for effect
            self.show_stairs()
        else:
            print("\n🎉 You're already at the TOP!")
    
    def climb_down(self):
        """Climb one step down"""
        if self.position > 0:
            self.position -= 1
            print(f"\n⬇️  You climbed DOWN to step {self.position}")
            time.sleep(0.5)  # Small pause for effect
            self.show_stairs()
        else:
            print("\n🏁 You're already at the BOTTOM!")
    
    def jump_up(self, steps=2):
        """Jump multiple steps up"""
        if self.position + steps <= self.total_stairs:
            self.position += steps
            print(f"\n🐰 JUMPED {steps} steps UP to step {self.position}!")
            time.sleep(0.5)
            self.show_stairs()
        else:
            print(f"\n⚠️  Can't jump that high! Would go past step {self.total_stairs}")
    
    def check_win(self):
        """Check if player reached the top"""
        if self.position == self.total_stairs:
            print("\n" + "🎉" * 20)
            print("CONGRATULATIONS! 🏆")
            print(f"You reached the TOP, {self.player_name}!")
            print("YOU WIN THE GAME! 🎊")
            print("🎉" * 20)
            return True
        return False
    
    def show_help(self):
        """Show game instructions"""
        print("\n" + "?" * 40)
        print("GAME HELP:")
        print("?" * 40)
        print("Goal: Reach step 10 to win!")
        print("\nCommands:")
        print("  U  - Climb UP one step")
        print("  D  - Climb DOWN one step")
        print("  J  - JUMP up 2 steps")
        print("  S  - Show current position")
        print("  H  - Show this help")
        print("  Q  - Quit the game")
        print("?" * 40)
    
    def play_game(self):
        """Main game loop"""
        print("\n" + "🎮" * 20)
        print("WELCOME TO STAIR CLIMBING GAME!")
        print("🎮" * 20)
        
        # Get player name
        if not self.player_name:
            self.player_name = input("\nWhat's your name? ").strip() or "Player"
        
        print(f"\nHello, {self.player_name}! Let's play!")
        print(f"Goal: Climb from step 0 to step {self.total_stairs}")
        
        self.show_help()
        self.show_stairs()
        
        moves = 0  # Count how many moves player makes
        
        # Game loop
        while True:
            print("\n" + "-" * 40)
            print(f"Move #{moves + 1}")
            print("-" * 40)
            
            # Get player choice
            choice = input("\nWhat do you want to do? (U/D/J/S/H/Q): ").upper()
            
            if choice == "U":  # Up
                self.climb_up()
                moves += 1
                
            elif choice == "D":  # Down
                self.climb_down()
                moves += 1
                
            elif choice == "J":  # Jump
                self.jump_up(2)
                moves += 1
                
            elif choice == "S":  # Show
                self.show_stairs()
                
            elif choice == "H":  # Help
                self.show_help()
                
            elif choice == "Q":  # Quit
                print(f"\nThanks for playing, {self.player_name}!")
                print(f"You made {moves} moves.")
                print("Hope you had fun! 👋")
                break
                
            else:
                print("\n❌ Invalid choice! Type U, D, J, S, H, or Q")
                print("Type H for help if needed")
                continue
            
            # Check if player won
            if self.check_win():
                print(f"\n🏅 You won in {moves} moves!")
                play_again = input("\nPlay again? (Y/N): ").upper()
                if play_again == "Y":
                    # Reset game
                    self.position = 0
                    moves = 0
                    print("\n" + "🔄" * 20)
                    print("NEW GAME STARTING!")
                    print("🔄" * 20)
                    self.show_stairs()
                else:
                    print(f"\nThanks for playing, {self.player_name}!")
                    break

# ============================================================================
# 🎯 SIMPLE VERSION (For Beginners)
# ============================================================================

class SimpleStairGame:
    """Simple version for learning"""
    
    def __init__(self):
        self.step = 0  # Start at step 0
        self.max_step = 5  # Only 5 steps to make it easier
        
    def show_position(self):
        """Show where you are"""
        print(f"\nYou are at step: {self.step}")
        print(f"Goal: Reach step {self.max_step}")
        
        # Simple visual
        print("Stairs: ", end="")
        for i in range(self.max_step + 1):
            if i == self.step:
                print("[X]", end=" ")  # You are here
            else:
                print("[ ]", end=" ")  # Empty step
        print()
    
    def simple_play(self):
        """Simple game loop"""
        print("\n=== SIMPLE STAIR GAME ===")
        print("Type 'U' to go UP")
        print("Type 'D' to go DOWN")
        print("Type 'Q' to QUIT")
        
        while True:
            self.show_position()
            
            # Check win
            if self.step == self.max_step:
                print("\n🎉 YOU WIN! You reached the top!")
                break
            
            # Get choice
            choice = input("\nYour choice (U/D/Q): ").upper()
            
            if choice == "U":
                if self.step < self.max_step:
                    self.step += 1
                    print("You went UP one step!")
                else:
                    print("You're already at the top!")
                    
            elif choice == "D":
                if self.step > 0:
                    self.step -= 1
                    print("You went DOWN one step!")
                else:
                    print("You're already at the bottom!")
                    
            elif choice == "Q":
                print("Thanks for playing!")
                break
                
            else:
                print("Please type U, D, or Q")

# ============================================================================
# 🎲 GAME WITH RANDOM EVENTS (More Fun!)
# ============================================================================

class AdventureStairGame(StairGame):
    """Stair game with random events"""
    
    def __init__(self, player_name=""):
        super().__init__(player_name)
        import random
        self.random = random
        
    def random_event(self):
        """Random things can happen when you move!"""
        event_chance = self.random.random()  # Random number 0-1
        
        if event_chance < 0.1:  # 10% chance
            print("\n💨 A strong wind pushed you UP 1 step!")
            self.position = min(self.position + 1, self.total_stairs)
            self.show_stairs()
            
        elif event_chance < 0.2:  # Another 10% chance
            print("\n🌧️  The step was wet! You slipped DOWN 1 step!")
            self.position = max(self.position - 1, 0)
            self.show_stairs()
            
        elif event_chance < 0.25:  # 5% chance
            print("\n🍀 Found a LUCKY step! Jumping UP 2 steps!")
            self.position = min(self.position + 2, self.total_stairs)
            self.show_stairs()
    
    def play_with_events(self):
        """Play with random events"""
        print("\n" + "🎲" * 20)
        print("ADVENTURE STAIR GAME!")
        print("Random events can happen!")
        print("🎲" * 20)
        
        super().play_game()  # Use parent's play method but add events

# ============================================================================
# 🚀 START THE GAME
# ============================================================================

def main():
    """Main function to start the game"""
    print("Choose your game mode:")
    print("1. Simple Game (5 steps, easy)")
    print("2. Normal Game (10 steps)")
    print("3. Adventure Game (with random events)")
    
    while True:
        try:
            choice = int(input("\nEnter 1, 2, or 3: "))
            
            if choice == 1:
                game = SimpleStairGame()
                game.simple_play()
                break
                
            elif choice == 2:
                player_name = input("Enter your name: ").strip() or "Player"
                game = StairGame(player_name)
                game.play_game()
                break
                
            elif choice == 3:
                player_name = input("Enter your name: ").strip() or "Adventurer"
                game = AdventureStairGame(player_name)
                game.play_game()
                break
                
            else:
                print("Please enter 1, 2, or 3")
                
        except ValueError:
            print("Please enter a number")

# Start the game
if __name__ == "__main__":
    main()
    print("\n" + "=" * 50)
    print("Hope you enjoyed the game! Come back soon! 🎮")
    print("=" * 50)
