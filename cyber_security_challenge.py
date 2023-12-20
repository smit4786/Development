import random
import time

class CyberSecuritySimulator:
    def __init__(self):
        self.user_score = 0

    def display_menu(self):
        print("\nCybersecurity Training Simulator")
        print("1. Network Security Challenge")
        print("2. Password Cracking Simulation")
        print("3. Social Engineering Scenario")
        print("4. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.network_security_challenge()
            elif choice == '2':
                self.password_cracking_simulation()
            elif choice == '3':
                self.social_engineering_scenario()
            elif choice == '4':
                print("Exiting the simulator. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def network_security_challenge(self):
        print("\nNetwork Security Challenge - Identify the Vulnerability")
        # Implement a scenario with a network-related challenge
        # Provide feedback and update user's score based on their response

    def password_cracking_simulation(self):
        print("\nPassword Cracking Simulation")
        # Implement a scenario where the user needs to crack a password
        # Provide feedback and update user's score based on their success

    def social_engineering_scenario(self):
        print("\nSocial Engineering Scenario")

        # Generate a random social engineering scenario
        scenarios = [
            "You receive an email from a colleague asking for your login credentials to access a shared document.",
            "A person claiming to be from IT support calls and asks for your password to troubleshoot an issue.",
            "You receive a message on a social media platform from a new connection asking for sensitive information."
        ]

        current_scenario = random.choice(scenarios)
        print(current_scenario)

        # Prompt the user to respond to the social engineering attempt
        user_response = input("How do you respond? ")

        # Provide feedback and update user's score
        if "do not provide" in user_response.lower() or "ignore" in user_response.lower():
            print("Correct! You identified the social engineering attempt.")
            self.user_score += 10
        else:
            print("Incorrect. It's important not to share sensitive information. Be cautious in such situations.")
            self.user_score -= 5

        print(f"Your current score: {self.user_score}")

if __name__ == "__main__":
    simulator = CyberSecuritySimulator()
    simulator.run()
